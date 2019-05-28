#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basf2 import *
from modularAnalysis import *

# input mdst file
inputMdst('default',
	    '/home/thczank/b0psi2sks/gsim/psi2sjpsiee/b0_psi2s_gsim_psi2sjpsiee_all.root'
	)

# create a ROOT file
ntupleFile('psi2sjpsiee_ana_all.root');

################################################################################
fillParticleList('K+:all',  '')
fillParticleList('mu+:all', '')
fillParticleList('pi+:all', '')
fillParticleList('e+:all', '')
fillParticleList('gamma:all', '')

################################################################################

########## MC TRUTH MATCHING ###############################################
from modularAnalysis import matchMCTruth
correctFSR("e+:cor","e+:all","gamma:all",angleThreshold=2.8647889756541)
cutAndCopyList("e+:gen", "e+:cor", "charge>0")
cutAndCopyList("e-:gen", "e+:cor", "charge<0")
reconstructDecay("J/psi:gen -> e+:gen e-:gen","")
matchMCTruth("J/psi:gen")

jpsiee_gen =  ['EventMetaData', '^J/psi']
jpsiee_gen += ['Kinematics', '^J/psi -> ^e+ ^e-']
jpsiee_gen += ['PID', 'J/psi -> ^e+ ^e-']
jpsiee_gen += ['InvMass', '^J/psi']
jpsiee_gen += ['MCTruth', '^J/psi']
ntupleTree("jpsi_from_genee", "J/psi:gen", jpsiee_gen)

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

cutAndCopyList("pi+:psi", "pi+:rec", "genMotherPDG != 310 and genMotherPDG != -310 and mcPDG == 211")
cutAndCopyList("pi-:psi", "pi-:rec", "genMotherPDG != 310 and genMotherPDG != -310 and mcPDG == -211")
reconstructDecay("psi(2S):gen -> J/psi:gen pi+:psi pi-:psi","")
matchMCTruth("psi(2S):gen")

psi2mumu_gen =  ['EventMetaData', '^psi(2S)']
psi2mumu_gen += ['Kinematics', '^psi(2S) -> ^J/psi ^pi+ ^pi-']
psi2mumu_gen += ['PID', 'psi(2S) -> ^J/psi ^pi+ ^pi-']
psi2mumu_gen += ['InvMass', '^psi(2S)']
psi2mumu_gen += ['MCTruth', '^psi(2S)']
ntupleTree("psi2_from_genmumu", "psi(2S):gen", psi2mumu_gen)

cutAndCopyList("K_S0:rectru", "K_S0:rec", "mcErrors == 0")
cutAndCopyList("psi(2S):rectru", "psi(2S):gen", "mcErrors == 0")
reconstructDecay("B0:recgen -> psi(2S):rectru K_S0:rectru","")
matchMCTruth("B0:recgen")
vertexRave("B0:recgen",-1)

variablesToNtuple("B0:recgen",["Mbc","deltaE","mcPDG",'distance', 'significanceOfDistance', 'dx', 'dy', 'dz', 'x', 'y', 'z', 'x_uncertainty', 'y_uncertainty', 'z_uncertainty', 'dr', 'dphi', 'dcosTheta', 'prodVertexX', 'prodVertexY', 'prodVertexZ', 'prodVertexXErr', 'prodVertexYErr', 'prodVertexZErr', 'chiProb'] ,"B0_Mbc","psi2See_b0mbc.root")
recgen_b0_all  = ['EventMetaData', '^B0'             ]
recgen_b0_all += ['Kinematics',    '^B0 -> ^psi(2S) ^K_S0']
recgen_b0_all += ['PID',           'B0 -> ^psi(2S) ^K_S0' ]
recgen_b0_all += ['InvMass',       '^B0'             ]
#recgen_b0_all += ['Mbc', '^B0']
recgen_b0_all += ['MCTruth',       '^B0'             ]
ntupleTree("B0_rec_gen", "B0:recgen", recgen_b0_all)

############################################################################


# process the events
process(analysis_main)

# print out the summary
print(statistics)
