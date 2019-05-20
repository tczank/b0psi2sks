#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basf2 import *
from modularAnalysis import *


# input mdst file
inputMdst('default',
	'../gsim/test_b0_psi2s_gsim_0.root'
	)

# create a ROOT file
ntupleFile('test_ana_psi2sks_0.root');

################################################################################
fillParticleList('K+:all',  '')
fillParticleList('mu+:all', '')
fillParticleList('pi+:all', '')
fillParticleList('e+:all', '')

################################################################################
# reconstruct psi(2S) with no pid cut ...

cutAndCopyList('mu+:posi_no_muid', 'mu+:all', 'charge>0'                 )
cutAndCopyList('mu-:nega_no_muid', 'mu-:all', 'charge<0'                 )
reconstructDecay('psi(2S):no_muid -> mu+:posi_no_muid mu-:nega_no_muid', '')

# dump to root (no_muid)
tools_psi_no_muid  = ['EventMetaData', '^psi(2S)']
tools_psi_no_muid += ['Kinematics',    '^psi(2S) -> ^mu+ ^mu-']
tools_psi_no_muid += ['PID',           ' psi(2S) -> ^mu+ ^mu-']
tools_psi_no_muid += ['InvMass',       '^psi(2S)'             ]
tools_psi_no_muid += ['MCTruth',       '^psi(2S)'             ]
ntupleTree('psitree_no_muid', 'psi(2S):no_muid', tools_psi_no_muid)

cutAndCopyList('e+:posi_no_eid', 'e+:all', 'charge>0'                    )
cutAndCopyList('e-:nega_no_eid', 'e-:all', 'charge<0'                    )
reconstructDecay('J/psi:no_eid -> e+:posi_no_eid e-:nega_no_eid',       '')

# dump to root (no_eid)
tools_psi_no_eid  = ['EventMetaData', '^J/psi']
tools_psi_no_eid += ['Kinematics',    '^J/psi -> ^e+ ^e-']
tools_psi_no_eid += ['PID',           ' J/psi -> ^e+ ^e-']
tools_psi_no_eid += ['InvMass',       '^J/psi'             ]
tools_psi_no_eid += ['MCTruth',       '^J/psi'             ]
ntupleTree('J/psitree_no_eid', 'J/psi:no_eid', tools_psi_no_eid)

cutAndCopyList('pi+:posi_no_piid', 'pi+:all', 'charge>0'                 )
cutAndCopyList('pi-:nega_no_piid', 'pi-:all', 'charge<0'                 )
reconstructDecay('psi(2S):no_piid -> J/psi:no_eid pi+:posi_no_piid pi-:nega_no_piid', '' )

# attempt to reconstruct psi(2S) with J/psi and dipion
# dump to root (no_piid)
tools_psi_no_piid  = ['EventMetaData', '^psi(2S)']
tools_psi_no_piid += ['Kinematics',    '^psi(2S) -> ^J/psi ^pi+ ^pi-']
tools_psi_no_piid += ['PID',           ' psi(2S) -> ^J/psi ^pi+ ^pi-']
tools_psi_no_piid += ['InvMass',       '^psi(2S)'             ]
tools_psi_no_piid += ['MCTruth',       '^psi(2S)'             ]
ntupleTree('psitree_no_piid', 'psi(2S):no_piid', tools_psi_no_piid)

################################################################################
# reconstruct J/psi with muid > 0.90
cutAndCopyList('mu+:posi_w_muid',  'mu+:all', 'charge>0 and muonID>0.90' )
cutAndCopyList('mu-:nega_w_muid',  'mu-:all', 'charge<0 and muonID>0.90' )
reconstructDecay('psi(2S):w_muid  -> mu+:posi_w_muid  mu-:nega_w_muid',  '')

# dump to root (w_muid)
tools_psi_w_muid  = ['EventMetaData',  '^psi(2S)']
tools_psi_w_muid += ['Kinematics',     '^psi(2S) -> ^mu+ ^mu-']
tools_psi_w_muid += ['PID',            ' psi(2S) -> ^mu+ ^mu-']
tools_psi_w_muid += ['InvMass',        '^psi(2S)'             ]
tools_psi_w_muid += ['MCTruth',        '^psi(2S)'             ]
ntupleTree('psitree_w_muid',  'psi(2S):w_muid',  tools_psi_w_muid)


################################################################################
#	reconstruct K_S0
cutAndCopyList('pi+:posi_no_piid',  'pi+:all', 'charge>0' )
cutAndCopyList('pi-:nega_no_piid',  'pi-:all', 'charge<0' )
reconstructDecay('K_S0:no_piid  -> pi+:posi_no_piid  pi-:nega_no_piid',  '')

# dump to root (w_muid)
tools_ks_no_piid  = ['EventMetaData',  '^K_S0']
tools_ks_no_piid += ['Kinematics',     '^K_S0 -> ^pi+ ^pi-']
tools_ks_no_piid += ['PID',            ' K_S0 -> ^pi+ ^pi-']
tools_ks_no_piid += ['InvMass',        '^K_S0'             ]
tools_ks_no_piid += ['MCTruth',        '^K_S0'             ]
ntupleTree('kstree_no_piid',  'K_S0:no_piid',  tools_ks_no_piid)
################################################################################

# reconstruct B
cutAndCopyList('K+:not_a_muon',    'K+:all',  'kaonID>0.90 and muonID<=0.90'   )
reconstructDecay('B0:psi2S_ks -> psi(2S):w_muid K_S0:no_piid',           '')
matchMCTruth('B0:psi2S_ks')

# dump to root (w_muid)
tools_B_jpsiks  = ['EventMetaData',  '^B0']
tools_B_jpsiks += ['Kinematics',     '^B0 -> ^psi(2S) ^K_S0']
tools_B_jpsiks += ['PID',            ' B0 ->  ^psi(2S) ^K_S0']
tools_B_jpsiks += ['InvMass',        '^B0'              ]
tools_B_jpsiks += ['MCTruth',        '^B0:psi2S_ks'      ]
ntupleTree('Btree_psi2Skc',  'B0:psi2S_ks',  tools_B_jpsiks)


# process the events
process(analysis_main)

# print out the summary
print(statistics)
