void trainBDT(TString name) {

    TFile *fOut = new TFile(name+".root","RECREATE");
    TMVA::Factory *factory = new TMVA::Factory(name, fOut, "!V:!Color");

    TFile *fSig = TFile::Open("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/DPSWW_Yields.root");
    TTree *tSig = (TTree *) fSig->Get("SigEvents");
    //tSig.AddFriend("tree_passedEvents", "THq_tHqLeptonic_mH125_8TeV_testtest_00_presel_CSV_friend.root");
    factory->AddSignalTree(tSig, 1.0);

    // TCut cuts = "SystFlag==0 && pT1>20. && pT1>10. && TLCat==0 && Flavor==0 && PassZVeto==1 && Pass3rdVeto==1";
    TCut cuts = "TLCat==0 && Flavor==0";
    TCut cuts = "";

    //TFile *fBkg1 = TFile::Open("THq_TTbarGG_0Jet_Summer12-PU_S7_START52_V9-v1_presel_CSV.root");
    //TTree *tBkg1 = (TTree *) fBkg1->Get("tree_passedEvents");
    //tBkg1.AddFriend("BDT_lept/t", "THq_TTbarGG_0Jet_Summer12-PU_S7_START52_V9-v1_presel_CSV_plusBDT.root");
    //factory->AddBackgroundTree(tBkg1, 1.0);
    //tBkg2.AddFriend("tree_passedEvents", "THq_TTH_HToGG_M-125_8TeV-pythia6_Summer12-PU_S7_START52_V9-v2_presel_CSV_friend.root");

	// TChain* tBkg = new TChain("SigEvents");
	// tBkg->Add("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/WGstarMu_Yields.root");
	// tBkg->Add("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/W+W+_Yields.root");
	// tBkg->Add("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/W-W-_Yields.root");
	// tBkg->Add("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/TTbarW_Yields.root");
	// tBkg->Add("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/WZTo3LNu_Yields.root");
	// tBkg->Add("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/HWW_Yields.root");
	// tBkg->Add("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/TTJets_Yields.root");
	// tBkg->Add("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/DYJets_Yields.root");
	
    TFile *fBkg = TFile::Open("/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jun13_DPS/YieldsFiles/WZTo3LNu_Yields.root");
    TTree *tBkg = (TTree *) fBkg->Get("SigEvents");

    factory->AddBackgroundTree(tBkg, 1.0);


    //VARIABLES
	factory->AddVariable( "HT"     , 'F');
	factory->AddVariable( "pT1"    , 'F');
	factory->AddVariable( "pT2"    , 'F');
	factory->AddVariable( "NJ"     , 'I');
	factory->AddVariable( "Mll"    , 'F');
	factory->AddVariable( "MT1"    , 'F');
	factory->AddVariable( "MET"    , 'F');
	factory->AddVariable( "Jet0Pt" , 'F');
	factory->AddVariable( "eta1"   , 'F');
	factory->AddVariable( "NbJ"    , 'I');
	factory->AddVariable( "NbJmed" , 'I');
	factory->AddVariable( "MT2"    , 'F');
	factory->AddVariable( "dPhiMLs", 'I');
	factory->AddVariable( "NMus"   , 'I');
	factory->AddVariable( "PFIso1" , 'F');
	factory->AddVariable( "PFIso2" , 'F');
	factory->AddVariable( "Charge" , 'I');


    factory->SetWeightExpression("1./SLumi");
    factory->PrepareTrainingAndTestTree( cuts, cuts, "SplitMode=Random" );

    //factory->BookMethod( TMVA::Types::kLD, "LD", "!H:!V:VarTransform=None" );

    TString BDTGopt = "!H:!V:NTrees=500:BoostType=Grad:Shrinkage=0.05:!UseBaggedGrad:nCuts=200:nEventsMin=100:NNodesMax=5";

    BDTGopt += ":CreateMVAPdfs"; // Create Rarity distribution
    factory->BookMethod( TMVA::Types::kBDT, "BDTG", BDTGopt);


    factory->TrainAllMethods();
    factory->TestAllMethods();
    factory->EvaluateAllMethods();

    fOut->Close();
}

