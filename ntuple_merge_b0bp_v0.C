#include "TChain.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TH1F.h"
#include "TVirtualFitter.h"
#include "TRandom.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TMath.h"
#include "TFile.h"
#include <cmath>

void ntuple_merge_b0bp_v0()
{

  TString bucket_name[] = { "../b0psi2sks/b0bp_psi2s_realdat_072019/B0Bp_realdat_bucket4_maybecorrect.root","../b0psi2sks/b0bp_psi2s_realdat_072019/B0Bp_realdat_bucket6.root","../b0psi2sks/b0bp_psi2s_realdat_072019/B0Bp_realdat_bucket6_unofficial_1.root"};

  TString B0ntuple_name[] = { "B0_recgen_psi2smumu", "B0_recden_psi2see", "B0_recgen_psi2sjpsimumu", "B0_recden_psi2sjpsiee"};
  TString Bpntuple_name[]={"Bp_recgen_psi2smumu", "Bp_recden_psi2see", "Bp_recgen_psi2sjpsimumu", "Bp_recden_psi2sjpsiee"};


    TFile * buckets[3];

    TH1F *hnseg = new TH1F("hnseg",
                          "Mbc all B0 decay channels;Mbc;entries",
                           1000,5.2,5.29);
    TH1F *hpsi2sinvm = new TH1F("#psi(2S) inv M",
                           "M all B0 decay channels;M;entries",
                           1000,3.5,3.8);
    TH1F *hpsi2smuEoP = new TH1F("#psi(2S) #mu(e) EoP",
                                "EoP all B0 decay channels;EoP;entries",

                                 1000,0.0,1.9);

    TNtuple * merged_B0 = new TNtuple("B0_alldec","Mbc, EoP, #psi(2S)invM","Mbc:psi2sinvM:EoP");

    TNtuple *B0psi2s[4];
    TNtuple *Bppsi2s[4];

    for(int i = 0; i < 3; i++){
      Int_t psi2seflag =0;
      Int_t psi2sjpsiflag = 0;
      buckets[i] = new TFile(bucket_name[i]);
      for(int j = 0; j< 4; j++){
        B0psi2s[j] = (TNtuple*)buckets[i]->Get(B0ntuple_name[j]);
        //  Bppsi2s[j] = (TNtuple*)buckets[i]->Get(Bpntuple_name[j]);
        Int_t entries = (Int_t)B0psi2s[j]->GetEntries();
        cout<<"Number of Entries: "<<entries<< endl;
        Double_t Mbc=0;
        Double_t b0psi2sinvM=0;
        Double_t b0psi2sjpsiinvM=0;
        B0psi2s[j]->SetBranchAddress("Mbc",&Mbc);
        if(B0psi2s[j]->GetBranchStatus("b0psi2sinvM") == 1){
          B0psi2s[j]->SetBranchAddress("b0psi2sinvM",&b0psi2sinvM);}
        else{
          B0psi2s[j]->SetBranchAddress("b0psi2sjpsiinvM",&b0psi2sjpsiinvM);
          psi2sjpsiflag = 1;}
        Double_t b0psi2smuEoP = 0;
        Double_t b0psi2sjpsimuEoP = 0;
        Double_t b0psi2seEoP = 0;
        Double_t b0psi2sjpsieEoP = 0;
        if(B0psi2s[j]->GetBranchStatus("b0psi2smuEoP") == 1){
          B0psi2s[j]->SetBranchAddress("b0psi2smuEoP",&b0psi2smuEoP);}
        else if(B0psi2s[j]->GetBranchStatus("b0psi2seEoP")==1){
          B0psi2s[j]->SetBranchAddress("b0psi2seEoP",&b0psi2seEoP);
          psi2seflag = 1;
        }
        else if(B0psi2s[j]->GetBranchStatus("b0psi2sjpsimuEoP")==1){
          B0psi2s[j]->SetBranchAddress("b0psi2sjpsimuEoP",&b0psi2seEoP);
          psi2sjpsiflag = 1;
        }
        else{B0psi2s[j]->SetBranchAddress("b0psi2sjpsieEoP",&b0psi2sjpsieEoP);}
        for(Int_t ki = 1; ki < entries;ki++){
          B0psi2s[j]->GetEntry(ki);
          hnseg->Fill(Mbc);
          if(psi2sjpsiflag == 0 && psi2seflag ==0){
            merged_B0->Fill(Mbc,b0psi2sinvM,b0psi2smuEoP);
          hpsi2sinvm->Fill(b0psi2sinvM);
          hpsi2smuEoP->Fill(b0psi2smuEoP);}
          else if(psi2sjpsiflag == 1 && psi2seflag == 0){
            merged_B0->Fill(Mbc,b0psi2sjpsiinvM,b0psi2sjpsimuEoP);
            hpsi2sinvm->Fill(b0psi2sjpsiinvM);
          hpsi2smuEoP->Fill(b0psi2sjpsimuEoP);}
          else if(psi2sjpsiflag == 0 && psi2seflag == 1){
            merged_B0->Fill(Mbc,b0psi2sinvM,b0psi2seEoP);
            hpsi2sinvm->Fill(b0psi2sinvM);
            hpsi2smuEoP->Fill(b0psi2seEoP);
          }
          else{
            merged_B0->Fill(Mbc,b0psi2sjpsiinvM,b0psi2sjpsieEoP);
            hpsi2sinvm->Fill(b0psi2sjpsiinvM);
            hpsi2smuEoP->Fill(b0psi2sjpsieEoP);
          }
      }
    }
      buckets[i]->Close();
    }

    TFile *f = new TFile("mergedB0_all.root","RECREATE");

    merged_B0->Write();
    f->Write();
    f->Close();
    //   hnseg->Draw();
    // TCanvas * c1 = new TCanvas;
    // hpsi2sinvm->Draw();
    // TCanvas * c2 = new TCanvas;
    // hpsi2smuEoP->Draw();
}
