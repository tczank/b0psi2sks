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

void b0bp_ntuplehistadd_v0()
{

  TFile * b0psi2smumu = new TFile("../b0psi2sks/b0bp_psi2s_realdat_072019/b0psi2smumu.root");
  TFile * b0psi2see = new TFile("../b0psi2sks/b0bp_psi2s_realdat_072019/b0psi2see.root");
  TFile * b0psi2sjpsimumu = new TFile("../b0psi2sks/b0bp_psi2s_realdat_072019/b0psi2sjpsimumu.root");
  TFile * b0psi2sjpsiee = new TFile("../b0psi2sks/b0bp_psi2s_realdat_072019/b0psi2sjpsiee.root");

  TFile * bppsi2smumu = new TFile("../b0psi2sks/b0bp_psi2s_realdat_072019/bppsi2smumu.root");
  TFile * bppsi2see = new TFile("../b0psi2sks/b0bp_psi2s_realdat_072019/bppsi2see.root");
  TFile * bppsi2sjpsimumu = new TFile("../b0psi2sks/b0bp_psi2s_realdat_072019/bppsi2sjpsimumu.root");
  TFile * bppsi2sjpsiee = new TFile("../b0psi2sks/b0bp_psi2s_realdat_072019/bppsi2sjpsiee.root");

  TH1 * psi2smumu = (TH1F*)b0psi2smumu->Get("c1");
  TH1 * psi2see = (TH1F*)b0psi2see->Get("c1");
  TH1 * psi2sjpsimumu = (TH1F*)b0psi2sjpsimumu->Get("c1");
  TH1 * psi2sjpsiee = (TH1F*)b0psi2sjpsiee->Get("c1");

  TH1 * ppsi2smumu = (TH1F*)bppsi2smumu->Get("c1");
  TH1 * ppsi2see = (TH1F*)bppsi2see->Get("c1");
  TH1 * ppsi2sjpsimumu = (TH1F*)bppsi2sjpsimumu->Get("c1");
  TH1 * ppsi2sjpsiee = (TH1F*)bppsi2sjpsiee->Get("c1");

  psi2smumu->Add(psi2see);
  psi2smumu->Add(psi2sjpsimumu);
  psi2smumu->Add(psi2sjpsiee);
  psi2smumu->Add(ppsi2smumu);
  psi2smumu->Add(ppsi2see);
  psi2smumu->Add(ppsi2sjpsimumu);
  psi2smumu->Add(ppsi2sjpsiee);

  psi2smumu->Draw();
}
