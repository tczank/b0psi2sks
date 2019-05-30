#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basf2        import *
from thIF         import *
from flavorTagger import *
from stdCharged   import *
from stdPhotons   import stdPhotons
import variables.collections as vc


################################################################################
# input mdst file
inputMdstList(
	environmentType='default',
	filelist=[
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.0.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.1.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.2.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.3.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.4.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.5.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.6.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.7.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.8.root',
	'/home/belle2/higuchit/wrk/belle2/physics/mcprod/practice_jpsikc/gsim/practice_jpsikc_gsim_recon.9.root']
)


################################################################################
# create ab output ROOT file
ntupleFile('/tmp/kani/AAA_dame.root');
# ntupleFile('/dev/null');


################################################################################
drawLine(100);


################################################################################
# printMCTree();


################################################################################
# use standard final state particle lists
stdE('all')
stdMu('all')
stdPi('95eff')
stdK('95eff')


################################################################################
# correct electron momentum
# fillParticleList('gamma:all', 'E < 1.0', False)
# correctFSR("e+:corrected", "e+:all", "gamma:all", 5.0, 1.0, False)


################################################################################
# fill other charged particles
# fillParticleList('K+:good', 'kaonID > 0.1')
fillParticleList('mu+:good','muonID >= 0.1')


################################################################################
# reconstrcut J/psi
# reconstructDecay('J/psi:elel -> e+:corrected e-:corrected', '3.0 < M < 3.2')
reconstructDecay('J/psi:mumu -> mu+:good     mu-:good',     '3.0 < M < 3.2')
# matchMCTruth('J/psi:elel')
matchMCTruth('J/psi:mumu')

# dump J/psi to root
# tools_jpsi_elel  = ['EventMetaData', '^J/psi:elel']
# tools_jpsi_elel += ['Kinematics',    '^J/psi:elel -> ^e+  ^e- ']
# tools_jpsi_elel += ['PID',           ' J/psi:elel -> ^e+  ^e- ']
# tools_jpsi_elel += ['InvMass',       '^J/psi:elel'             ]
# tools_jpsi_elel += ['MCTruth',       '^J/psi:elel'             ]
# ntupleTree('tree_jpsi_elel', 'J/psi:elel', tools_jpsi_elel)

# tools_jpsi_mumu  = ['EventMetaData', '^J/psi:mumu']
# tools_jpsi_mumu += ['Kinematics',    '^J/psi:mumu -> ^mu+ ^mu-']
# tools_jpsi_mumu += ['PID',           ' J/psi:mumu -> ^mu+ ^mu-']
# tools_jpsi_mumu += ['InvMass',       '^J/psi:mumu'             ]
# tools_jpsi_mumu += ['MCTruth',       '^J/psi:mumu'             ]
# ntupleTree('tree_jpsi_mumu', 'J/psi:mumu', tools_jpsi_mumu)


################################################################################
# reconstruct B
# reconstructDecay('B+:jpsielel_kc -> J/psi:elel K+:95eff', '')
# reconstructDecay('B+:jpsimumu_kc -> J/psi:mumu K+:95eff', 'Mbc > 0.0 and abs(deltaE) < 999')
reconstructDecay('B+:jpsimumu_kc -> J/psi:mumu K+:95eff', 'Mbc > 5.2 and abs(deltaE) < 0.2')
# matchMCTruth('B+:jpsielel_kc')
matchMCTruth('B+:jpsimumu_kc')

# rankByHighest('B+:jpsimumu_kc', variable='chiProb', numBest=1)


################################################################################
# vertex reconstruction and flavor tagging
# vertexKFit('B+:jpsielel_kc', -1e10, 'B+ -> [J/psi:elel -> ^e+  ^e- ]', '')
# vertexKFit('B+:jpsimumu_kc', -1e10, 'B+ -> [J/psi:mumu -> ^mu+ ^mu-]', '')
# vertexTree('B+:jpsielel_kc', -1e10)
# vertexTree('B+:jpsimumu_kc', -1e10)
# vertexRave('B+:jpsielel_kc', -1e10, 'B+ -> [J/psi:elel -> ^e+  ^e- ]', '')
# vertexRave('B+:jpsimumu_kc', -1e10, 'B+ -> [J/psi:mumu -> ^mu+ ^mu-]', 'iptube')

# buildRestOfEvent('B+:jpsielel_kc')
buildRestOfEvent('B+:jpsimumu_kc')

flavorTagger(particleLists=['B+:jpsimumu_kc'], weightFiles='B2JpsiKs_muBGx1', workingDirectory='/tmp/kani')

# TagV('B+:jpsielel_kc', 'breco', 0.001, 'standard_PXD')
# TagV('B+:jpsimumu_kc', 'breco', 0.001, 'standard_PXD')

applyCuts('B+:jpsimumu_kc', cut='qrOutput(FBDT) > -2')


################################################################################
# cpfitvtx.so
cpFitVtx('B+:jpsimumu_kc', decayMode=5010, constraintType='iptube')


################################################################################
tools_bc_mumu  = ['EventMetaData',              '^B+:jpsimumu_kc']
ntupleTree('tree_bc_jpsimumu_kc',  'B+:jpsimumu_kc',  tools_bc_mumu)


################################################################################
# process the events    
dt_vars = ['DeltaT','MCDeltaT','MCTagBFlavor','DeltaTErr','DeltaZ','LBoost','LBoostErr','DeltaBoost','OBoost','OBoostErr'] 

Bc_vars = vc.reco_stats + \
	vc.deltae_mbc + \
	vc.mc_truth + \
	dt_vars + vc.flavor_tagging

variablesToNtuple('B+:jpsimumu_kc', 
	variables=Bc_vars, 
	filename='/tmp/kani/AAA_kani.root',
	treename='Bc_JpsiKc')


################################################################################
# dump to root (w_muid, w_Egamma_cut)
process(analysis_main)


################################################################################
# print out the summary
print(statistics)

