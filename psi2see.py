#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basf2 import *
from modularAnalysis import *

# input mdst file
inputMdst('default',
	'/home/thczank/b0psi2sks/gsim/psi2see/b0_psi2s_gsim_psiee_0.root'
	)

# create a ROOT file
ntupleFile('psi2see_ana.root');

################################################################################
fillParticleList('K+:all',  '')
fillParticleList('mu+:all', '')
fillParticleList('pi+:all', '')
fillParticleList('e+:all', '')

################################################################################

########## MC TRUTH MATCHING ###############################################
from modularAnalysis import matchMCTruth
cutAndCopyList("e+:gen", "e+:all", "charge>0")
cutAndCopyList("e-:gen", "e+:all", "charge<0")
reconstructDecay("psi(2S):gen -> e+:gen e-:gen","")
matchMCTruth("psi(2S):gen")

psi2ee_gen =  ['EventMetaData', '^psi(2S)']
psi2ee_gen += ['Kinematics', '^psi(2S) -> ^e+ ^e-']
psi2ee_gen += ['PID', 'psi(2S) -> ^e+ ^e-']
psi2ee_gen += ['InvMass', '^psi(2S)']
psi2ee_gen += ['MCTruth', '^psi(2S)']
ntupleTree("psi2S_from_genee", "psi(2S):gen", psi2ee_gen)

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

cutAndCopyList("K_S0:rectru", "K_S0:rec", "mcPDG == 310")
cutAndCopyList("psi(2S):rectru", "psi(2S):gen", "mcPDG == 100443")
reconstructDecay("B0:recgen -> psi(2S):rectru K_S0:rectru","")
#reconstructDecay("B0:recgen -> psi(2S):gen K_S0:rec", "")
matchMCTruth("B0:recgen")
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
