#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import stdCharged as sc
import stdPhotons as sp
import basf2 as b2
import modularAnalysis as ma
import variables.collections as vc
import variables.utils as vu
import vertex as vx
from variables.utils import create_aliases
from modularAnalysis import buildEventKinematics
from modularAnalysis import buildEventShape
mypath = b2.create_path() # create your own path (call it what you like)
import sys
import os

#for the flavor tagger in kekcc
b2.use_central_database("analysis_tools_release-03-02-00")
import flavorTagger as ft

ma.inputMdst(environmentType='default', filename=os.environ['FILENAME'], path=mypath)

## radiative photon correction
ma.fillParticleList(decayString='e+:uncorrected',
                   # cut='electronID > 0.01 and d0 < 2 and abs(z0) < 4',
                    cut='electronID > 0.5 and abs(d0) < 1 and abs(z0) < 3',
                    path=mypath)
ma.fillParticleList(decayString='gamma:all',
                    cut='E < 1.0',
                    writeOut=False,
                    path=mypath)

# loose mc matching (recommended)
ma.looseMCTruth(list_name='e+:uncorrected', path=mypath)
ma.looseMCTruth(list_name='gamma:all', path=mypath)

# fsr correction
ma.correctFSR(outputListName='e+:corrected',
              inputListName='e+:uncorrected',
              gammaListName='gamma:all',
              angleThreshold=5.0,
              energyThreshold=1.0,
              writeOut=False,
              path=mypath)
ma.looseMCTruth(list_name='e+:corrected',
                path=mypath)

## reconstruct J/psi -> e+ e- decay
ma.reconstructDecay('J/psi:ee -> e+:corrected e-:corrected', '2.8 < M < 3.2 and nTracks > 4 and useCMSFrame(p) < 2. ', path=mypath)

ma.looseMCTruth(list_name='J/psi:ee', path=mypath)

ma.fillParticleList(decayString='pi+:good',cut='chiProb > 0.001 and pionID > 0.1',path=mypath)

##psi(2S) reconstruction
ma.reconstructDecay(decayString='psi(2S):ee -> J/psi:ee pi+:good pi-:good', cut="3.5 < M < 3.8 ", path=mypath)

ma.matchMCTruth('psi(2S):ee', path=mypath)

ma.fillParticleList(decayString='K_S0:pipi -> pi+:good pi-:good', cut='0.3 < M < 0.7 ', path=mypath)
ma.vertexKFit(list_name='K_S0:pipi', conf_level=0.0, path=mypath)

ma.reconstructDecay('B0:psi2s_eeks -> psi(2S):ee K_S0:pipi', 'Mbc > 5.2 and abs(deltaE)<0.15 ', path=mypath)

# perform MC matching (MC truth asociation)
ma.matchMCTruth('B0:psi2s_eeks', path=mypath)

# Fit the B0 Vertex
vx.vertexRave('B0:psi2s_eeks', 0., 'B0 -> [psi(2S):ee -> [J/psi:ee -> ^e+ ^e-] ^pi+ ^pi-] K_S0:pipi', 'iptube', path=mypath)

ma.rankByHighest('B0:psi2s_eeks',   'chiProb',numBest=3, outputVariable='B_vtx_rank', path=mypath)

ma.variables.addAlias('B_vtx_rank', 'extraInfo(B_vtx_rank)')

ma.rankByHighest('B0:psi2s_eeks',   'daughter(1, chiProb)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.variables.addAlias('B_k_rank', 'extraInfo(B_k_rank)')

# build the rest of the event associated to the B0
ma.buildRestOfEvent(target_list_name='B0:psi2s_eeks', path=mypath)

ft.flavorTagger(
    particleLists=['B0:psi2s_eeks'],
    weightFiles='B2nunubarBGx1')

# Fit Vertex of the B0 on the tag side
vx.TagV('B0:psi2s_eeks', 'breco', 0.001, 'standard_PXD', path=mypath)

buildEventKinematics(path=mypath)
buildEventShape(path=mypath)

kinematics = ['px','py','pz','pt','p','E']
cms_kinematics = create_aliases(kinematics, "useCMSFrame({variable})","CMS")
my_cluster = ['clusterE', 'clusterEoP', 'clusterTheta', 'nMatchedKLMClusters', 'klmClusterLayers']
#rank = ['chiProb','jpsi_rank','ks_rank','k_rank']
rank = ['chiProb','B_vtx_rank','B_k_rank']
#b0mcflavor = ['mcFlavorOfOtherB0']


B0e_vars = vc.kinematics + \
           cms_kinematics +\
           vc.deltae_mbc + \
           vc.event_shape + \
           rank + \
           vc.vertex + \
           vc.tag_vertex + \
           vc.mc_truth + \
           vc.mc_kinematics + \
           vc.mc_vertex + \
           vc.mc_tag_vertex + \
           ft.flavor_tagging + \
           vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
               decay_string='B0:psi2s_eeks -> ^psi(2S):ee ^K_S0:pipi') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.pid + my_cluster + vc.track + vc.track_hits,
        decay_string='B0:psi2s_eeks -> [psi(2S):ee -> [^J/psi:ee -> [^e+:corrected -> ^e+:uncorrected gamma:all] [^e-:corrected -> ^e-:uncorrected gamma:all]] ^pi+:good ^pi-:good] [K_S0:pipi -> ^pi+ ^pi-]')

################### Saving variables to ntuple ##############################
rootOutputFile = os.environ['OUTPUT']

ma.variablesToNtuple('B0:psi2s_eeks', B0e_vars,
                     filename=rootOutputFile,
                     treename='b0e',
                     path=mypath)

b2.process(mypath)

# print out the summary
print(b2.statistics)
