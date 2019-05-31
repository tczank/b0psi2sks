#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basf2 import *
from modularAnalysis import *

# input mdst file
inputMdst('default',
          '/home/thczank/b0psi2sks/gsim/psi2smumu/b0_psi2s_gsim_psi2smumu_all.root'
	)

# create a ROOT file
ntupleFile('psi2smumu_ana_all_iptube.root');

################################################################################
fillParticleList('K+:all',  '')
fillParticleList('mu+:all', '')
fillParticleList('pi+:all', '')
fillParticleList('e+:all', '')

################################################################################

########## MC TRUTH MATCHING ###############################################
from modularAnalysis import matchMCTruth
from modularAnalysis import variablesToNtuple
cutAndCopyList("mu+:gen", "mu+:all", "charge>0")
cutAndCopyList("mu-:gen", "mu+:all", "charge<0")
reconstructDecay("psi(2S):gen -> mu+:gen mu-:gen","")
matchMCTruth("psi(2S):gen")

psi2mumu_gen =  ['EventMetaData', '^psi(2S)']
psi2mumu_gen += ['Kinematics', '^psi(2S) -> ^mu+ ^mu-']
psi2mumu_gen += ['PID', 'psi(2S) -> ^mu+ ^mu-']
psi2mumu_gen += ['InvMass', '^psi(2S)']
psi2mumu_gen += ['MCTruth', '^psi(2S)']
ntupleTree("psi2S_from_genmumu", "psi(2S):gen", psi2mumu_gen)

cutAndCopyList("pi+:rec", "pi+:all", "charge>0")
cutAndCopyList("pi-:rec", "pi+:all", "charge<0")
reconstructDecay("K_S0:rec -> pi+:rec pi-:rec","")
matchMCTruth("K_S0:rec")
ks0pipi_rec = ["EventMetaData", "K_S0"]
ks0pipi_rec += ["Kinematics", "^K_S0 -> ^pi+ ^pi-"]
ks0pipi_rec += ["PID", "K_S0 -> ^pi+ ^pi-"]
ks0pipi_rec += ["InvMass", "^K_S0"]
ks0pipi_rec += ["MCTruth", "^K_S0"]
ntupleTree("K_S0_from_recpipi", "K_S0:rec",ks0pipi_rec)

#cutAndCopyList("K_S0:rectru", "K_S0:rec", "mcPDG == 310")
#cutAndCopyList("psi(2S):rectru", "psi(2S):gen", "mcPDG == 100443")

cutAndCopyList("K_S0:rectru", "K_S0:rec", "mcErrors == 0")
cutAndCopyList("psi(2S):rectru", "psi(2S):gen", "mcErrors == 0")

reconstructDecay("B0:recgen -> psi(2S):rectru K_S0:rectru","")
matchMCTruth("B0:recgen")
buildRestOfEvent("B0:recgen")

TagV("B0:recgen", "breco", 0.001, "standard_PXD")

#vertexRaveDaughtersUpdate("B0:recgen",-1,"B0 -> [psi(2S) -> ^mu+ ^mu-] K_S0")
vertexRave("B0:recgen",-1, "B0:recgen -> [psi(2S):rectru -> ^mu+ ^mu- ]", "iptube")

variablesToNtuple("B0:recgen",["Mbc","deltaE","mcPDG",'distance', 'significanceOfDistance', 'dx', 'dy', 'dz', 'x', 'y', 'z', 'x_uncertainty', 'y_uncertainty', 'z_uncertainty', 'dr', 'dphi', 'dcosTheta', 'prodVertexX', 'prodVertexY', 'prodVertexZ', 'prodVertexXErr', 'prodVertexYErr', 'prodVertexZErr', 'chiProb', "mcDX", "mcDY", "mcDZ", "pValue",'MCDeltaT', 'TagVmcLBoost', 'TagVmcOBoost', 'mcLBoost', 'mcOBoost', 'mcTagVx', 'mcTagVy', 'mcTagVz','DeltaT', 'DeltaTErr', 'DeltaZ','DeltaBoost','TagVLBoost', 'TagVLBoostErr', 'TagVOBoost', 'TagVOBoostErr', 'TagVpVal', 'TagVx', 'TagVxErr', 'TagVy', 'TagVyErr', 'TagVz', 'TagVzErr',"nTracks"] ,"B0_Mbc","psi2Smumu_b0mbc_iptube.root")
recgen_b0_all  = ['EventMetaData', '^B0'             ]
recgen_b0_all += ['Kinematics',    '^B0 -> ^psi(2S) ^K_S0']
recgen_b0_all += ['PID',           'B0 -> ^psi(2S) ^K_S0' ]
recgen_b0_all += ['InvMass',       '^B0'             ]
#recgen_b0_all += ['Mbc', '^B0']
recgen_b0_all += ['MCTruth',       '^B0'             ]
ntupleTree("B0_rec_gen", "B0:recgen", recgen_b0_all)

##vertex.fitVertex("B0:recgen",0,"B0 -> psi(2S) K_S0", "rave", "vertex", "",True,basf2.Path)

#vertexTree("B0:recgen", ipConstraint=True)


############################################################################


# process the events
process(analysis_main)

# print out the summary
print(statistics)
