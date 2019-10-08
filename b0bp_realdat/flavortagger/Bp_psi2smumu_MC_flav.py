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

ma.fillParticleList('mu+:good', 'muonID > 0.5 and abs(d0) < 1 and abs(z0) < 3', path=mypath)

ma.fillParticleList(decayString='K+:good',cut='chiProb > 0.001 and kaonID > 0.1',path=mypath)

##psi(2S) reconstruction

ma.reconstructDecay(decayString='psi(2S):gen -> mu+:good mu-:good', cut="3.6 < M < 3.8 and nTracks > 4 and useCMSFrame(p) < 3.", path=mypath)

ma.matchMCTruth('psi(2S):den', path=mypath)


# reconstruct B+ -> psi(2S) K+ decay
# keep only candidates with Mbc > 5.1 and abs(deltaE)<0.5
ma.reconstructDecay('B+:psi2s_genkp -> psi(2S):gen K+:good', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)

# perform MC matching (MC truth asociation)
ma.matchMCTruth('B+:psi2s_genkp', path=mypath)

# Fit the B0 Vertex
vx.vertexRave('B+:psi2s_genkp', 0., 'B+ -> [psi(2S):mumu -> ^mu+ ^mu-] K+:good', 'iptube', path=mypath)

ma.rankByHighest('B+:psi2s_genkp', 'chiProb',numBest=3, outputVariable='B_vtx_rank', path=mypath)

ma.variables.addAlias('B_vtx_rank', 'extraInfo(B_vtx_rank)')

ma.rankByHighest('B+:psi2s_genkp', 'daughter(1, kaonID)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.variables.addAlias('B_k_rank', 'extraInfo(B_k_rank)')

# build the rest of the event associated to the B0
ma.buildRestOfEvent(target_list_name='B+:psi2s_genkp', path=mypath)

ft.flavorTagger(
    particleLists=['B+:psi2s_genkp'],
    weightFiles='B2nunubarBGx1')

vx.TagV('B+:psi2s_genkp', 'breco', 0.001, 'standard_PXD', path=mypath)

buildEventKinematics(path=mypath)
buildEventShape(path=mypath)

kinematics = ['px','py','pz','pt','p','E']
cms_kinematics = create_aliases(kinematics, "useCMSFrame({variable})","CMS")
my_cluster = ['clusterE', 'clusterEoP', 'clusterTheta', 'nMatchedKLMClusters', 'klmClusterLayers']
#rank = ['chiProb','jpsi_rank','ks_rank','k_rank']
rank = ['chiProb','B_vtx_rank','B_k_rank']
#b0mcflavor = ['mcFlavorOfOtherB0']

Bpgen_vars = vc.kinematics + \
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
        decay_string='B+:psi2s_genkp -> ^psi(2S):gen ^K+:good') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.pid + my_cluster + vc.track + vc.track_hits + rank,
        decay_string='B+:psi2s_genkp -> [psi(2S):gen -> ^mu+ ^mu-]  K+:good')

################### Saving variables to ntuple ##############################
rootOutputFile = os.environ['OUTPUT']

ma.variablesToNtuple('B+:psi2s_genkp', Bpgen_vars,
                     filename=rootOutputFile,
                     treename='bpgen',
                     path=mypath)

b2.process(mypath)

# print out the summary
print(b2.statistics)
