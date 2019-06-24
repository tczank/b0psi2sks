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
ma.inputMdst(environmentType='default',
             filename=b2.find_file('/home/thczank/b0psi2sks/gsim/psi2sjpsiee/b0_psi2s_gsim_psi2sjpsiee_all.root'),
             path=mypath)

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
ma.correctFSR("e+:cor","e+:all","gamma:all",angleThreshold=2.8647889756541,path=mypath) #from 2012 Belle 1 paper
ma.cutAndCopyList("e+:gen", "e+:all", "charge>0",path=mypath)
ma.cutAndCopyList("e-:gen", "e+:all", "charge<0",path=mypath)
ma.reconstructDecay(decayString="J/psi:gen -> e+:gen e-:gen",
                    cut="",
                    path=mypath)
ma.matchMCTruth(list_name="J/psi:gen",path=mypath)

chiProb=["chiProb"]

psi2s_vars = vc.mc_truth + vc.kinematics + vc.inv_mass + vc.mc_variables + chiProb

ma.cutAndCopyList("pi+:rec", "pi+:all", "charge>0",path=mypath)
ma.cutAndCopyList("pi-:rec", "pi+:all", "charge<0",path=mypath)
ma.reconstructDecay("K_S0:rec -> pi+:rec pi-:rec","",path=mypath)
ma.matchMCTruth("K_S0:rec",path=mypath)

ma.cutAndCopyList("pi+:psi", "pi+:rec", "genMotherPDG == 100443 and mcErrors == 0",path=mypath)
ma.cutAndCopyList("pi-:psi", "pi-:rec", "genMotherPDG == 100443 and mcErrors == 0",path=mypath)
ma.cutAndCopyList("J/psi:tru", "J/psi:gen", "mcErrors == 0", path=mypath)
ma.reconstructDecay("psi(2S):gen -> J/psi:tru pi+:psi pi-:psi","",path=mypath)
ma.matchMCTruth("psi(2S):gen",path=mypath)

ma.cutAndCopyList("K_S0:rectru", "K_S0:rec", "mcErrors == 0",path=mypath)
#ma.cutAndCopyList("psi(2S):rectru", "psi(2S):gen", "mcErrors == 0",path=mypath)

ma.reconstructDecay("B0:recgen -> psi(2S):gen K_S0:rectru","",path=mypath)

b0_vars = vc.mc_truth + vc.kinematics + vc.deltae_mbc + vc.mc_variables + vc.mc_vertex + vc.mc_tag_vertex + vc.tag_vertex + vc.track + vc.vertex + chiProb

######################################################################################

##################### RAVE FITTING ############################################


ma.vertexRave("B0:recgen",-1, "B0:recgen -> [psi(2S):gen -> [J/psi:tru -> ^e+ ^e-] ^pi+ ^pi-  ]", "iptube",path=mypath)

ma.matchMCTruth("B0:recgen",path=mypath)
ma.buildRestOfEvent("B0:recgen",path=mypath)
ma.TagV("B0:recgen", "breco", 0.001, "standard_PXD",path=mypath)



#############################################################################

########################### Saving variables to ntuple ##############################
rootOutputFile = "B0psi2Sjpsiee_recon_iptube.root"

ma.variablesToNtuple(decayString="psi(2S):gen",
                  variables=psi2s_vars,
                  treename="psi2Sjpsi_psi2S",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="J/psi:gen",
                  variables=psi2s_vars,
                  treename="psi2Sjpsi_jpsi",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="K_S0:rec",
                  variables=psi2s_vars,
                  treename="psi2Smumu_K_S0",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recgen",
                  variables=b0_vars,
                  treename="B0_recgen",
                  filename=rootOutputFile,
                  path=mypath)
############################################################################

# process the events
b2.process(mypath)

# print out the summary
print(b2.statistics)
