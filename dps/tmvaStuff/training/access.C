#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"

TMVA::Reader *reader = new TMVA::Reader( "!Color:!Silent" ); 

float HT_bdt     ;
float pT1_bdt    ;
float pT2_bdt    ;
float NJ_bdt     ;
float Mll_bdt    ;
float MT1_bdt    ;
float MET_bdt    ;
float Jet0Pt_bdt ;
float eta1_bdt   ;
float NbJ_bdt    ;
float NbJmed_bdt ;
float MT2_bdt    ;
float dPhiMLs_bdt;
float NMus_bdt   ;
float PFIso1_bdt ;
float PFIso2_bdt ;
float Charge_bdt ;


reader->AddVariable("HT"     , &HT_bdt      ); 
reader->AddVariable("pT1"    , &pT1_bdt     ); 
reader->AddVariable("pT2"    , &pT2_bdt     ); 
reader->AddVariable("NJ"     , &NJ_bdt      ); 
reader->AddVariable("Mll"    , &Mll_bdt     ); 
reader->AddVariable("MT1"    , &MT1_bdt     ); 
reader->AddVariable("MET"    , &MET_bdt     ); 
reader->AddVariable("Jet0Pt" , &Jet0Pt_bdt  ); 
reader->AddVariable("eta1"   , &eta1_bdt    ); 
reader->AddVariable("NbJ"    , &NbJ_bdt     ); 
reader->AddVariable("NbJmed" , &NbJmed_bdt  ); 
reader->AddVariable("MT2"    , &MT2_bdt     ); 
reader->AddVariable("dPhiMLs", &dPhiMLs_bdt );
reader->AddVariable("NMus"   , &NMus_bdt    ); 
reader->AddVariable("PFIso1" , &PFIso1_bdt  ); 
reader->AddVariable("PFIso2" , &PFIso2_bdt  ); 
reader->AddVariable("Charge" , &Charge_bdt  ); 

TString methodName = "BDTG method";
TString weightfile = "/shome/mdunser/finalRA5/CMSSW_5_3_7_patch5/src/DiLeptonAnalysis/NTupleProducer/macros/dps/tmvaStuff/training/weights/provaNEW_BDTG.weights.xml";

std::cout << "-> Booking BDT" << std::endl;
reader->BookMVA( methodName, weightfile ); 

// // and then once the variables are all set (in the loop) do:
// BDT_lept_t = reader->EvaluateMVA( "BDTG method" );
