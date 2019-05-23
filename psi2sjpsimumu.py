#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basf2 import *
from modularAnalysis import *

# input mdst file
inputMdst('default',
	'/home/thczank/b0psi2sks/gsim/psi2sjpsimumu/b0_psi2s_gsim_psijpsimumu_0.root'
	)

# create a ROOT file
ntupleFile('psi2sjpsimumu_ana.root');

################################################################################
fillParticleList('K+:all',  '')
fillParticleList('mu+:all', '')
fillParticleList('pi+:all', '')
fillParticleList('e+:all', '')

################################################################################

########## MC TRUTH MATCHING ###############################################
from modularAnalysis import matchMCTruth

cutAndCopyList("mu+:gen", "mu+:all", "charge>0")
cutAndCopyList("mu-:gen", "mu+:all", "charge<0")
reconstructDecay("J/psi:gen -> mu+:gen mu-:gen","")
matchMCTruth("J/psi:gen")

jpsimumu_gen =  ['EventMetaData', '^J/psi']
jpsimumu_gen += ['Kinematics', '^J/psi -> ^mu+ ^mu-']
jpsimumu_gen += ['PID', 'J/psi -> ^mu+ ^mu-']
jpsimumu_gen += ['InvMass', '^J/psi']
jpsimumu_gen += ['MCTruth', '^J/psi']
ntupleTree("jpsi_from_genmumu", "J/psi:gen", jpsimumu_gen)

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
