#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## to be deprecated in release 04 ####
#from basf2 import *
#from modularAnalysis import *
##########################

## new preamble for release 04 ###
import basf2 as b2
import modularAnalysis as ma
import variables.collections as vc
import variables.utils as vu
mypath = b2.Path()

print(mypath)
# input mdst file
#ma.inputMdst(environmentType='default',
 #            filename=b2.find_file('/home/thczank/b0psi2sks/gsim/psi2smumu/b0_psi2s_gsim_psi2smumu_all.root'),
  #           path=mypath)

ma.inputMdstList(environmentType='default',
                 filelist=['/home/thczank/b0psi2sks/gsim/psi2smumu/b0_psi2s_gsim_psimumu_0.root','/home/thczank/b0psi2sks/gsim/psi2smumu/b0_psi2s_gsim_psimumu_1.root'],
                 path = mypath)


# create a ROOT file
#ntupleFile('psi2smumu_ana_all_iptube.root');

################################################################################
ma.fillParticleList('K+:all',  '',path=mypath)
ma.fillParticleList('mu+:all', '',path=mypath)
ma.fillParticleList('pi+:all', '',path=mypath)
ma.fillParticleList('e+:all', '',path=mypath)
ma.fillParticleList('gamma:all', '',path=mypath)
################################################################################

########## MC TRUTH MATCHING ###############################################
ma.cutAndCopyList("mu+:gen", "mu+:all", "charge>0",path=mypath)
ma.cutAndCopyList("mu-:gen", "mu+:all", "charge<0",path=mypath)
ma.reconstructDecay(decayString="psi(2S):gen -> mu+:gen mu-:gen",
                    cut="",
                    path=mypath)
#ma.matchMCTruth(list_name="psi(2S):gen",path=mypath)

ma.cutAndCopyList("mu+:gen", "mu+:all", "charge>0",path=mypath)
ma.cutAndCopyList("mu-:gen", "mu+:all", "charge<0",path=mypath)
ma.reconstructDecay(decayString="J/psi:gen -> mu+:gen mu-:gen",
                    cut="",
                    path=mypath)
#ma.matchMCTruth(list_name="J/psi:gen",path=mypath)

ma.correctFSR("e+:cor","e+:all","gamma:all",angleThreshold=2.8647889756541,path=mypath) #from 2012 Belle 1 paper
ma.cutAndCopyList("e+:gen", "e+:cor", "charge>0",path=mypath)
ma.cutAndCopyList("e-:gen", "e+:cor", "charge<0",path=mypath)
ma.reconstructDecay(decayString="psi(2S):den -> e+:gen e-:gen",
                    cut="genMotherPDG == 100443",
                    path=mypath)
ma.reconstructDecay(decayString="J/psi:den -> e+:gen e-:gen",
                    cut=" genMotherPDG == 443",
                    path=mypath)
#ma.matchMCTruth(list_name="psi(2S):den",path=mypath)
#ma.matchMCTruth(list_name="J/psi:den",path=mypath)

chiProb=["chiProb"]
EoP=['clusterEoP']
piid=['pionID']

psi2s_vars = vc.mc_truth + vc.kinematics + vc.inv_mass + vc.mc_variables + chiProb
pi_vars = vc.mc_truth + vc.kinematics + vc.inv_mass + vc.mc_variables + chiProb + EoP + piid

ma.cutAndCopyList("pi+:rec", "pi+:all", "charge>0",path=mypath)
ma.cutAndCopyList("pi-:rec", "pi+:all", "charge<0",path=mypath)
ma.reconstructDecay("K_S0:rec -> pi+:rec pi-:rec","",path=mypath)
#ma.matchMCTruth("K_S0:rec",path=mypath)

ma.cutAndCopyList("pi+:psi", "pi+:rec", "genMotherPDG == 100443 and mcErrors == 0",path=mypath)
ma.cutAndCopyList("pi-:psi", "pi-:rec", "genMotherPDG == 100443 and mcErrors == 0",path=mypath)
ma.cutAndCopyList("J/psi:tru", "J/psi:gen", "mcErrors == 0", path=mypath)
ma.reconstructDecay("psi(2S):jpsi -> J/psi:tru pi+:psi pi-:psi","",path=mypath)
#ma.matchMCTruth("psi(2S):gen",path=mypath)

ma.cutAndCopyList("J/psi:truden", "J/psi:den", "mcErrors == 0", path=mypath)
ma.reconstructDecay("psi(2S):jpsiden -> J/psi:truden pi+:psi pi-:psi","",path=mypath)

ma.cutAndCopyList("K_S0:rectru", "K_S0:rec", "mcErrors == 0",path=mypath)

ma.cutAndCopyList("psi(2S):rectru", "psi(2S):gen", "mcErrors == 0",path=mypath)
ma.cutAndCopyList("psi(2S):recden", "psi(2S):den", "mcErrors == 0",path=mypath)
ma.cutAndCopyList("psi(2S):recjpsi", "psi(2S):jpsi", "mcErrors == 0",path=mypath)
ma.cutAndCopyList("psi(2S):recjpsiden", "psi(2S):jpsiden", "mcErrors == 0",path=mypath)

ma.cutAndCopyList("K+:pos","K+:all", "charge > 0", path=mypath)

ma.reconstructDecay("B0:recgen -> psi(2S):rectru K_S0:rectru","",path=mypath)
ma.reconstructDecay("B0:recden -> psi(2S):recden K_S0:rectru","",path=mypath)
ma.reconstructDecay("B0:recjpsi -> psi(2S):recjpsi K_S0:rectru","",path=mypath)
ma.reconstructDecay("B0:recjpsiden -> psi(2S):recjpsiden K_S0:rectru","",path=mypath)

ma.reconstructDecay("B+:recgen -> psi(2S):rectru K+:pos","",path=mypath)
ma.reconstructDecay("B+:recden -> psi(2S):recden K+:pos","",path=mypath)
ma.reconstructDecay("B+:recjpsi -> psi(2S):recjpsi K+:pos","",path=mypath)
ma.reconstructDecay("B+:recjpsiden -> psi(2S):recjpsiden K+:pos","",path=mypath)

b0_vars = vc.mc_truth + vc.kinematics + vc.deltae_mbc + vc.mc_variables + vc.mc_vertex + vc.mc_tag_vertex + vc.tag_vertex + vc.track + vc.vertex + chiProb + EoP + piid

##############################################################################

#################### RAVE FITTING ############################################
#
#
#ma.vertexRave("B0:recgen",-1, "B0:recgen -> [psi(2S):rectru -> ^mu+ ^mu- ]", "ipprofile",path=mypath)

#ma.vertexRave("B0:recgen",0.0,path=mypath) suggested at the release example


#ma.matchMCTruth("B0:recgen",path=mypath)
#ma.buildRestOfEvent("B0:recgen",path=mypath)
#ma.TagV("B0:recgen", "breco", 0.001, "standard_PXD",path=mypath)


#############################################################################

################### Saving variables to ntuple ##############################
rootOutputFile = "B0Bp_realdat_mctest.root"

ma.variablesToNtuple(decayString="psi(2S):rectru",
                  variables=psi2s_vars,
                  treename="psi2Smumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="psi(2S):recden",
                  variables=psi2s_vars,
                  treename="psi2See",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="psi(2S):recjpsi",
                  variables=psi2s_vars,
                  treename="psi2Sjpsimumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="psi(2S):recjpsiden",
                  variables=psi2s_vars,
                  treename="psi2Sjpsiee",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="J/psi:gen",
                  variables=psi2s_vars,
                  treename="jpsimumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="J/psi:den",
                  variables=psi2s_vars,
                  treename="jpsiee",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="K_S0:rectru",
                  variables=psi2s_vars,
                  treename="K_S0",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="pi+:all",
                  variables=pi_vars,
                  treename="pi",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="e+:cor",
                  variables=pi_vars,
                  treename="e",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="mu+:all",
                  variables=pi_vars,
                  treename="mu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="K+:all",
                  variables=pi_vars,
                  treename="Kp",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recgen",
                  variables=b0_vars,
                  treename="B0_recgen_psi2smumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recden",
                  variables=b0_vars,
                  treename="B0_recden_psi2see",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recjpsi",
                  variables=b0_vars,
                  treename="B0_recgen_psi2sjpsimumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recjpsiden",
                  variables=b0_vars,
                  treename="B0_recden_psi2sjpsiee",
                  filename=rootOutputFile,
                  path=mypath)
ma.variablesToNtuple(decayString="B+:recgen",
                  variables=b0_vars,
                  treename="Bp_recgen_psi2smumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recden",
                  variables=b0_vars,
                  treename="Bp_recden_psi2see",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recjpsi",
                  variables=b0_vars,
                  treename="Bp_recgen_psi2sjpsimumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recjpsiden",
                  variables=b0_vars,
                  treename="Bp_recden_psi2sjpsiee",
                  filename=rootOutputFile,
                  path=mypath)
####################################################################

# process the events
b2.process(mypath)

# print out the summary
print(b2.statistics)
