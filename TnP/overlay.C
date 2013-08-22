#include "TPaveStats.h"
#include "TF1.h"
#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TLatex.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TFitResultPtr.h" 
#include "TFitResult.h" 

#include "TCanvas.h"
#include "TAxis.h"


using namespace std;


#include <sstream>
#include <iostream>
#include <fstream>

TString getEta(bool isMu, int i){
	TString str;
	if(isMu){
		if(i==1) str = "$|\\eta|$ $<=$ 1.2";
		if(i==2) str = "$|\\eta|$ $> $ 1.2";
	}
	else{
		if(i==1) str = "0.0   $<=$ $|\\eta|$ $<$  0.8   ";
		if(i==2) str = "0.8   $<=$ $|\\eta|$ $<$  1.4442";
		if(i==3) str = "1.566 $<=$ $|\\eta|$ $<$  2.0   ";
		if(i==4) str = "2.0   $<=$ $|\\eta|$ $<$  2.4   ";
	}
	return str;
}

void setHistoLabels(TH1* h,
		    TString title,
		    TString yLabel,
		    TString xLabel,
		    int color){
  h->SetTitle(title);
  h->SetTitleSize(0.06);
  h->SetLineStyle(1);
  //h->GetYaxis()->SetTitleOffset(yOffset);
  //h->GetXaxis()->SetTitleOffset(xOffset);
  h->GetYaxis()->SetTitle(yLabel);
  h->GetXaxis()->SetTitle(xLabel);
  h->SetMarkerStyle(20);
  h->SetMarkerSize(1.0);
  h->SetMarkerColor(color);
  h->GetXaxis()->SetTitleSize(0.06);
  h->GetXaxis()->SetLabelSize(0.05);
  h->GetYaxis()->SetLabelSize(0.05);
  h->GetYaxis()->SetTitleSize(0.05);
  h->GetYaxis()->SetRangeUser(0.2, 1.05);
}


void setRatioStyle(TH1F * histo){
	histo -> SetLineColor(kBlack);
    histo -> GetYaxis()->SetTitle("Data/MC");
    histo -> GetYaxis()->SetTitleSize(0.15);
    histo -> GetYaxis()->SetTitleOffset(0.30);

    histo -> GetYaxis()->SetLabelSize(0.10);
    histo -> GetYaxis()->SetRangeUser(0.88, 1.12);
    histo -> GetYaxis()->SetNdivisions(503);


    histo -> GetXaxis()->SetLabelSize(0.);
    histo -> GetXaxis()->SetTitle("p_{T} (GeV)");
    histo -> GetXaxis()->SetTitleSize(0.21);
    histo -> GetXaxis()->SetTitleOffset(0.65);

	// histo -> SetTitleSize(0.);
	histo -> SetTitle("");
}


void overlay(bool isMu=true, bool setbatch = false){
  if(setbatch) gROOT->SetBatch();
  //gROOT->SetStyle("Plain");
  gStyle->SetPadGridX(kTRUE);
  gStyle->SetPadGridY(kTRUE);
  gStyle->SetPadRightMargin(0.07);
  gStyle->SetPadLeftMargin(0.13);
  //gStyle->SetOptStat("eour");
  gStyle->SetOptStat("");
  //gStyle->SetTitleXSize(0.07); 
  //gStyle->SetTitleXOffset(0.6); 
  //tyle->SetTitleYSize(0.3);
  //gStyle->SetLabelSize(0.6) 
  //gStyle->SetTextSize(0.5);


  gStyle->SetOptTitle(1);
  gStyle->SetMarkerStyle(20);

//marc   gStyle->SetErrorX(0.5);
//marc gStyle->SetTitleX(0.2);

  TFile* f = new TFile("./tnp_output.root");
  
  string flvS; if(isMu) flvS="Mu"; else flvS="El";

  int maxEtaBin;
  if(isMu) maxEtaBin=2; else maxEtaBin=4;

  ofstream OUT;
  OUT.open(isMu ? "muSF.tex" : "elSF.tex");

  OUT << "\\documentclass[25pt, a4paper]{article}" << endl;
  OUT << "\\usepackage{multirow,amsmath,fullpage}" << endl;
  OUT << "\\usepackage[margin=0.2cm, paperwidth=17.5cm, paperheight=3.2cm]{geometry}" << endl;
  OUT << "\\begin{document}" << endl;

  OUT << "\\begin{table}" << endl;
  OUT << "  \\begin{center}" << endl;
  OUT << "  \\caption{data/MC scale factors for" << (isMu ? " muons}" : " electrons}") << endl;
  OUT << "  \\label{tab:";
  OUT << (isMu ? "sfMu}" : "sfEl}") << endl;
  OUT << "  \\begin{tabular}{|l|c|c|c|c|c|c|}" << endl;
  OUT << "  \\hline" << endl;

  OUT << " p$_{T}$   & [10,15] & [15,20] & [20,30] & [30,40] & [40,50] & [50, $\\infty$[\\\\ \\hline \\hline " << endl;

  for(int i=1; i<=maxEtaBin; i++){
    stringstream nameSimID   ; nameSimID   << "eta" << i << flvS << "SimEffID"   ;
    stringstream nameSimIP   ; nameSimIP   << "eta" << i << flvS << "SimEffIP"   ;
    stringstream nameSimISO  ; nameSimISO  << "eta" << i << flvS << "SimEffISO"  ;
    stringstream nameSimALL  ; nameSimALL  << "eta" << i << flvS << "SimEffAll"  ;
    stringstream nameSimALL2  ; nameSimALL2  << "eta" << i << flvS << "SimEffAll2"  ;

    stringstream nameDataID  ; nameDataID  << "eta" << i << flvS << "DataEffID"  ;
    stringstream nameDataIP  ; nameDataIP  << "eta" << i << flvS << "DataEffIP"  ;
    stringstream nameDataISO ; nameDataISO << "eta" << i << flvS << "DataEffISO" ;
    stringstream nameDataALL ; nameDataALL << "eta" << i << flvS << "DataEffAll" ;
    stringstream nameDataALL2 ; nameDataALL2 << "eta" << i << flvS << "DataEffAll2" ;

    TH1F* hSimID   = (TH1F*) f->Get(nameSimID.str()  .c_str());
    TH1F* hSimIP   = (TH1F*) f->Get(nameSimIP.str()  .c_str());
    TH1F* hSimISO  = (TH1F*) f->Get(nameSimISO.str() .c_str());
    TH1F* hSimALL  = (TH1F*) f->Get(nameSimALL.str() .c_str());
    TH1F* hSimALL2  = (TH1F*) f->Get(nameSimALL2.str() .c_str());

    TH1F* hDataID  = (TH1F*) f->Get(nameDataID.str() .c_str());
    TH1F* hDataIP  = (TH1F*) f->Get(nameDataIP.str() .c_str());
    TH1F* hDataISO = (TH1F*) f->Get(nameDataISO.str().c_str());
    TH1F* hDataALL = (TH1F*) f->Get(nameDataALL.str().c_str());
    TH1F* hDataALL2 = (TH1F*) f->Get(nameDataALL2.str().c_str());

	float xbins[7]={10,15,20,30,40,50,80};
    TH1F* rID   = new TH1F("ratio_ID" , "ratio_ID" , 6, xbins); rID   ->Sumw2(); rID  -> Divide(hDataID , hSimID );
    TH1F* rIP   = new TH1F("ratio_IP" , "ratio_IP" , 6, xbins); rIP   ->Sumw2(); rIP  -> Divide(hDataIP , hSimIP );
    TH1F* rISO  = new TH1F("ratio_ISO", "ratio_ISO", 6, xbins); rISO  ->Sumw2(); rISO -> Divide(hDataISO, hSimISO);
    TH1F* rALL  = new TH1F("ratio_ALL", "ratio_ALL", 6, xbins); rALL  ->Sumw2(); rALL -> Divide(hDataALL, hSimALL);
    TH1F* rALL2  = new TH1F("ratio_ALL2", "ratio_ALL2", 6, xbins); rALL2  ->Sumw2(); rALL2 -> Divide(hDataALL2, hSimALL2);

	OUT << Form(getEta(isMu,i)+" & %.2f (%.2f) & %.2f (%.2f)  & %.2f (%.2f)  & %.2f (%.2f)  & %.2f (%.2f)  & %.2f (%.2f) \\\\  \\hline \n", 
	rALL->GetBinContent(1), rALL2->GetBinContent(1),
    rALL->GetBinContent(2), rALL2->GetBinContent(2),
    rALL->GetBinContent(3), rALL2->GetBinContent(3),
    rALL->GetBinContent(4), rALL2->GetBinContent(4),
    rALL->GetBinContent(5), rALL2->GetBinContent(5),
    rALL->GetBinContent(6), rALL2->GetBinContent(6)  );


    setRatioStyle(rID );
    setRatioStyle(rIP );
    setRatioStyle(rISO);
    setRatioStyle(rALL);
    setRatioStyle(rALL2);

	// TLegend
    TLegend* l = new TLegend(0.40,0.20,0.55,0.35);
    l->SetTextSize(0.04);
    l->SetLineColor(0);
    l->SetFillColor(0);
    l->AddEntry(hSimID,"DY-MC","P");
    l->AddEntry(hDataID,"DATA","P");
    l->SetShadowColor(0);

    TCanvas* c = new TCanvas("foo", "bar", 0, 0, 500, 500);
	c->cd();
	TPad* p = new TPad("plotpad",  "plotpad", 0.00, 0.23, 1.00, 1.00, 0, 0);
	p->SetBottomMargin(0.015);
	p->SetBottomMargin(0.05);
	p->Draw();
	TPad* r = new TPad("ratiopad",  "ratiopad", 0.00, 0.00, 1.00, 0.2, 0, 0);
	r->SetTopMargin(0.025);
	r->SetBottomMargin(0.37);
	r->Draw();

    stringstream title;
    title << "ID vs all probes, etaBin " << i ;
    setHistoLabels(hSimID  , title.str() , "Efficiency" , "p_{T} (GeV)" , 2);
    setHistoLabels(hDataID , title.str() , "Efficiency" , "p_{T} (GeV)" , 1);
	r->cd(); rID->DrawCopy("X1");
	p->cd();
    hSimID->SetLineColor(kRed)    ; hSimID ->Draw()       ;
    hDataID->SetLineColor(kBlack) ; hDataID->Draw("same") ;
    l->Draw();
    c->Print((nameSimID.str()+".pdf").c_str());

    title.str(""); title << "IP vs ID, etaBin " << i ;
    setHistoLabels(hSimIP  , title.str() , "Efficiency" , "p_{T} (GeV)" , 2);
    setHistoLabels(hDataIP , title.str() , "Efficiency" , "p_{T} (GeV)" , 1);
	r->cd(); rIP->DrawCopy("X1");
	p->cd();
    hSimIP->SetLineColor(kRed)    ; hSimIP ->Draw()       ;
    hDataIP->SetLineColor(kBlack) ; hDataIP->Draw("same") ;
    l->Draw();
    c->Print((nameSimIP.str()+".pdf").c_str());

    title.str(""); title << "ISO vs ID+IP, etaBin " << i ;
    setHistoLabels(hSimISO  , title.str() , "Efficiency" , "p_{T} (GeV)" , 2);
    setHistoLabels(hDataISO , title.str() , "Efficiency" , "p_{T} (GeV)" , 1);
	r->cd(); rISO->DrawCopy("X1");
	p->cd();
    hSimISO->SetLineColor(kRed)    ; hSimISO ->Draw()       ;
    hDataISO->SetLineColor(kBlack) ; hDataISO->Draw("same") ;
    l->Draw();
    c->Print((nameSimISO.str()+".pdf").c_str());

    title.str(""); title << "FullID vs all probes, etaBin " << i ;
    setHistoLabels(hSimALL  , title.str() , "Efficiency" , "p_{T} (GeV)" , 2);
    setHistoLabels(hDataALL , title.str() , "Efficiency" , "p_{T} (GeV)" , 1);
	r->cd(); rALL->DrawCopy("X1");
	p->cd();
    hSimALL->SetLineColor(kRed)    ; hSimALL ->Draw("E")      ;
    hDataALL->SetLineColor(kBlack) ; hDataALL->Draw("E same") ;
    l->Draw();
    c->Print((nameSimALL.str()+".pdf").c_str());

    title.str(""); title << "Full everything at the same time, etaBin " << i ;
    setHistoLabels(hSimALL2  , title.str() , "Efficiency" , "p_{T} (GeV)" , 2);
    setHistoLabels(hDataALL2 , title.str() , "Efficiency" , "p_{T} (GeV)" , 1);
	r->cd(); rALL2->DrawCopy("X1");
	p->cd();
    hSimALL2->SetLineColor(kRed)    ; hSimALL2 ->Draw("E")      ;
    hDataALL2->SetLineColor(kBlack) ; hDataALL2->Draw("E same") ;
    l->Draw();
    c->Print((nameSimALL2.str()+".pdf").c_str());

  }
  OUT << "  \\hline" << endl;
  OUT << "  \\end{tabular}" << endl;
  OUT << "  \\end{center}" << endl;
  OUT << "\\end{table}" << endl;

  OUT << "\\end{document}" << endl;

  OUT.close();



}

