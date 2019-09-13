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
import variables as v
mypath = b2.Path()

print(mypath)
# input mdst file
# the flavor tagger weighting file only works from kekcc
#b2.use_central_database("analysis_tools_release-03-01-00")
ma.inputMdst(environmentType='default',
             filename=b2.find_file('/home/thczank/b0psi2sks/gsim/B0/psi2smumu/b0_psi2s_gsim_psi2smumu_all.root'),
             path=mypath)

# create a ROOT file
#ntupleFile('psi2smumu_ana_all_iptube.root');


################################################################################
ma.fillParticleList('K+:all',  '',path=mypath)
ma.fillParticleList('mu+:all', cut='muonID > 0.01',path=mypath)
ma.fillParticleList('pi+:all', '',path=mypath)
ma.fillParticleList('e+:all', cut='electronID > 0.01 and d0 < 2 and abs(z0) < 4',path=mypath)

################################################################################

########## MC TRUTH MATCHING ###############################################
ma.cutAndCopyList("mu+:gen", "mu+:all", "charge>0 and muonID > 0.1",path=mypath)
ma.cutAndCopyList("mu-:gen", "mu+:all", "charge<0 and muonID > 0.1",path=mypath)
ma.reconstructDecay(decayString="psi(2S):gen -> mu+:gen mu-:gen",
                    cut="",
                    path=mypath)
ma.matchMCTruth(list_name="psi(2S):gen",path=mypath)
ma.reconstructDecay(decayString="psi(2S):mom -> mu+:gen mu-:gen",
                    cut="genMotherPDG==443",
                    path=mypath)
ma.matchMCTruth(list_name="psi(2S):mom",path=mypath)


v.variables.addAlias('mu_EoP','daughter(0,clusterEoP)')
v.variables.addAlias('psi2smuid','daughter(0,muonID)')

chiProb=["chiProb"]
EoP=['clusterEoP']
piid=['pionID']
costheta=['cosTheta']
p123=['px','py','pz']
issig=['isSignal']

psi2s_vars = vc.mc_truth + vc.kinematics + vc.inv_mass + vc.mc_variables + chiProb + EoP + piid + p123 + issig

ma.cutAndCopyList("pi+:rec", "pi+:all", "charge>0",path=mypath)
ma.cutAndCopyList("pi-:rec", "pi+:all", "charge<0",path=mypath)
ma.reconstructDecay("K_S0:rec -> pi+:rec pi-:rec",cut="0.3 < M < 0.7 ",path=mypath)
ma.matchMCTruth("K_S0:rec",path=mypath)

ma.cutAndCopyList("K_S0:rectru", "K_S0:rec", cut="",path=mypath)
ma.cutAndCopyList("psi(2S):rectru", "psi(2S):gen", cut="",path=mypath)

ma.reconstructDecay("B0:recgen -> psi(2S):rectru K_S0:rectru",cut="Mbc > 5.2 and abs(deltaE)<0.15 ",path=mypath)


#b0mcflavor = ['mcFlavorOfOtherB0']

b0_vars = vc.mc_truth + vc.kinematics + vc.deltae_mbc + vc.mc_variables + vc.mc_vertex + vc.mc_tag_vertex + vc.tag_vertex + vc.track + vc.vertex + chiProb + EoP + piid + issig #+ b0mcflavor

######################################################################################

##################### RAVE FITTING ############################################


ma.vertexRave("B0:recgen",-1, "B0:recgen -> [psi(2S):rectru -> ^mu+ ^mu- ]", "ipprofile",path=mypath)

#ma.vertexRave("B0:recgen",0.0,path=mypath) suggested at the release example


ma.matchMCTruth("B0:recgen",path=mypath)
ma.buildRestOfEvent(target_list_name='B0:recgen',path=mypath)
ma.TagV("B0:recgen", "breco", 0.001, "standard_PXD",path=mypath)

#############################################################################

########################### Saving variables to ntuple ##############################
rootOutputFile = "LLPpsi2Smumu_morii_test.root"

ma.variablesToNtuple(decayString="psi(2S):gen",
                  variables=psi2s_vars,
                  treename="psi2Smumu_psi2S",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="psi(2S):mom",
                  variables=psi2s_vars,
                  treename="aJpsi",
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
