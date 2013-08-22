//
// Compare all plots in two files
//

#include <iostream>

#include <TStyle.h>
#include <TString.h>
#include <TH1F.h>
#include <TTree.h>
#include <TFile.h>
#include <TPaveStats.h>
#include <TPad.h>
#include <TPRegexp.h>
#include <TMath.h>
#include <TCanvas.h>
#include <TLorentzVector.h>

#include "mt2.C"
//#include "../src/helper/Davismt2.cc"

using namespace std;

float DeltaPhi(float phi1, float phi2){
    double result = phi1 - phi2;
    while( result >   TMath::Pi() ) result -= TMath::TwoPi();
    while( result <= -TMath::Pi() ) result += TMath::TwoPi();
    return TMath::Abs(result);
}
float DeltaEta(float eta1, float eta2){
    double result = eta1 - eta2;
    return TMath::Abs(result);
}
float DeltaR(float eta1, float eta2, float phi1, float phi2){
    float deta = eta1 - eta2;
    float dphi = DeltaPhi(phi1, phi2);
    return sqrt( deta*deta + dphi*dphi );
}

float getMETi(float pt1, float phi1, float pt2, float phi2, float met, float metphi, int flag = 1){
	float phia = phi1 < 0. ? phi1+TMath::Pi() : phi1 -TMath::Pi();
	float phib = phi2 < 0. ? phi2+TMath::Pi() : phi2 -TMath::Pi();
	// std::cout << " =============================================================" << std::endl;
	// std::cout << Form("phi1: %.2f phia %.2f  ||   phi2: %.2f phib: %.2f", phi1, phia, phi2, phib) << std::endl;
	TLorentzVector MET;
	MET.SetPtEtaPhiM(met, 0., metphi, 0.);
	float metx = MET.Px();
	float mety = MET.Py();

	// std::cout << Form("    metx: %.2f mety %.2f metphi: %.2f", metx, mety, metphi) << std::endl;

	// get x component of meta and then all the others:
	float ax = (metx*TMath::Tan(phib) - mety) / (TMath::Tan(phib) - TMath::Tan(phia));
	float ay = ax * TMath::Tan(phia);
	float bx = metx - ax;
	float by = mety - ay;

	// std::cout << Form("phia: %.2f atan2(ay,ax) %.2f  ||   phib: %.2f atan2(by,bx): %.2f", phia, TMath::ATan2(ay,ax), phib, TMath::ATan2(by,bx) ) << std::endl;
	// std::cout << Form("    ax: %.2f ay %.2f  ||   bx: %.2f by: %.2f", ax, ay, bx, by) << std::endl;

	float a = TMath::Sqrt(ax*ax + ay*ay);
	float b = TMath::Sqrt(bx*bx + by*by);
	TLorentzVector meta, metb;
	meta.SetPtEtaPhiM(a, 0., TMath::ATan2(ay, ax), 0.);
	metb.SetPtEtaPhiM(b, 0., TMath::ATan2(by, bx), 0.);

	// std::cout << "originalMET: " << met << " (meta+metb).Pt(): " << (meta+metb).Pt() << std::endl;

	if (fabs( met - (meta+metb).Pt() ) > 0.01  ) return 0.;
	
	if (flag == 1) return TMath::Sqrt(4*pt1*meta.Pt()) ;
	return TMath::Sqrt(4*pt2*metb.Pt());
}


float CalcMT2(float testmass, bool massive, float v1pt, float v1eta, float v1phi, float v2pt, float v2eta, float v2phi,  float met, float metphi ){

  double pa[3];
  double pb[3];
  double pmiss[3];

  TLorentzVector MET, v1, v2;
  MET.SetPtEtaPhiM(met, 0., metphi, 0.);
  v1 .SetPtEtaPhiM(v1pt, v1eta, v1phi, 0.105);
  v2 .SetPtEtaPhiM(v2pt, v2eta, v2phi, 0.105);
  
  pmiss[0] = 0;
  pmiss[1] = MET.Px();
  pmiss[2] = MET.Py();
  
  pa[0] = massive ? v1.M() : 0;
  pa[1] = v1.Px();
  pa[2] = v1.Py();
  
  pb[0] = massive ? v2.M() : 0;
  pb[1] = v2.Px();
  pb[2] = v2.Py();
  
  Davismt2 *mt2 = new Davismt2();
  mt2->set_momenta(pa, pb, pmiss);
  mt2->set_mn(testmass);
  float MT2=mt2->get_mt2();
  delete mt2;
  return MT2;

}

float deltaPhiLepsMET(float pt1, float eta1, float phi1, float pt2, float eta2, float phi2, float metphi){
	TLorentzVector a,b;
	a.SetPtEtaPhiM(pt1, eta1, phi1, 0.105);
	b.SetPtEtaPhiM(pt2, eta2, phi2, 0.105);
	return DeltaPhi(metphi, (a+b).Phi() );
}


// DPS - WW:
// dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/mdunser/SSDLTrees/2013/Apr07/MC/WW-DoubleScattering-8TeV-pythia8-Summer12-DR53X-PU-S10-START53-V7A-v1.root
// W+W+:
// dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/mdunser/SSDLTrees/2013/Apr07/MC/WpWpqq-8TeV-madgraph-Summer12-DR53X-PU-S10-START53-V7A-v1.root
// TTJets:
// dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/mdunser/SSDLTrees/2013/Apr07/MC/TT-CT10-TuneZ2star-8TeV-powheg-tauola-Summer12-DR53X-PU-S10-START53-V7A-v2/output_14.root
// WGstarMu:
// dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/mdunser/SSDLTrees/2013/Apr07/MC/WGstarToLNu2Mu-TuneZ2star-7TeV-madgraph-tauola-Summer12-DR53X-PU-S10-START53-V7A-v1.root
// WZ:
// dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/mdunser/SSDLTrees/2013/Apr07/MC/WZJetsTo3LNu-TuneZ2-8TeV-madgraph-tauola-Summer12-DR53X-PU-S10-START53-V7A-v1/output_15.root

int compareMarc( const TString& file1, const TString& file2, 
             const TString tname1="Analysis", const TString tname2="Analysis") {

  gStyle->SetOptStat(1111);

  // Open files
  TFile* f1 = TFile::Open(file1);
  if ( !f1->IsOpen() ) return -1;
  TFile* f2 = TFile::Open(file2);
  if ( !f2->IsOpen() ) return -1;

  // Get the trees
  TTree* tree1 = (TTree*)f1->Get(tname1);
  if ( !tree1 ) {
    std::cerr << "Couldn't find tree " << tname1 
              << " in file " << file1 << std::endl;
    return -2;
  }
  TTree* tree2 = (TTree*)f2->Get(tname2);
  if ( !tree2 ) {
    std::cerr << "Couldn't find tree " << tname2 
              << " in file " << file2 << std::endl;
    return -2;
  }

  // Loop over all branches and draw distributions
  tree1->SetLineColor(kBlue);
  tree2->SetLineColor(kRed);

  tree1->SetLineWidth(2);
  tree2->SetLineWidth(2);

  // float w1 = 19500*0.5879/832839;
  // float w2 = 19500*0.2482/98780;

  std::cout << "Blue:  " << file1 << std::endl 
            << "Red: " << file2 << std::endl;

  TCanvas * c = new TCanvas("foo", "bar", 1200, 1000);
  c->Divide(3,4);
  c->cd(1);
  tree1->Draw("DeltaPhi(MuPhi[0], pfMETType1Phi)", "(NMus > 1 && (MuCharge[0] == MuCharge[1]) )", "norm");
  tree2->Draw("DeltaPhi(MuPhi[0], pfMETType1Phi)", "(NMus > 1 && (MuCharge[0] == MuCharge[1]) )", "normsame");

  c->cd(2);
  tree1->Draw("pfMETType1", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("pfMETType1", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(3);
  tree1->Draw("MuPt[0]", "NMus > 1 && MuPt[0] < 150 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("MuPt[0]", "NMus > 1 && MuPt[0] < 150 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(4);
  tree1->Draw("MuPt[1]", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("MuPt[1]", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(5);
  tree1->Draw("NJets", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("NJets", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(6);
  tree1->Draw("Sum$(JetPt>30)", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("Sum$(JetPt>30)", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(7);
  tree1->Draw("Sum$(JetPt>40)", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("Sum$(JetPt>40)", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(8);
  tree1->Draw("JetPt", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("JetPt", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(9);
  tree1->Draw("MuMT[0]", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("MuMT[0]", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(10);
  tree1->Draw("MuMT[1]", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("MuMT[1]", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(11);
  tree1->Draw("JetPt[0]", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("JetPt[0]", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  c->cd(12);
  tree1->Draw("deltaPhiLepsMET(MuPt[0], MuEta[0], MuPhi[0], MuPt[1], MuEta[1], MuPhi[1], pfMETType1Phi)", "NMus > 1 && MuCharge[0] == MuCharge[1]", "norm");
  tree2->Draw("deltaPhiLepsMET(MuPt[0], MuEta[0], MuPhi[0], MuPt[1], MuEta[1], MuPhi[1], pfMETType1Phi)", "NMus > 1 && MuCharge[0] == MuCharge[1]", "normsame");

  
  return 0;

}
