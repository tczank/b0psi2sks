#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#from basf2 import *
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

b2.use_central_database("data_reprocessing_proc9")

ma.inputMdst(environmentType='default', filename=os.environ['FILENAME'], path=mypath)

#ma.inputMdst(environmentType='default',
#             filename=b2.find_file('/mnt/nas1/yusa/mdst_000001_prod00003520_task00000001.root', 'examples', False),
#             path=mypath)

# use standard final state particle lists
#sc.stdE('good', path=mypath)
#sc.stdMu('good', path=mypath)
#sp.stdPhotons('good', path=mypath)

#ma.fillParticleList('mu+:good', '', path=mypath)
ma.fillParticleList('mu+:good', 'muonID > 0.5 and abs(d0) < 1 and abs(z0) < 3', path=mypath)
#

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
#ma.looseMCTruth(list_name='e+:uncorrected', path=mypath)
#ma.looseMCTruth(list_name='gamma:all', path=mypath)

# fsr correction
ma.correctFSR(outputListName='e+:corrected',
              inputListName='e+:uncorrected',
              gammaListName='gamma:all',
              angleThreshold=5.0,
              energyThreshold=1.0,
              writeOut=False,
              path=mypath)
#ma.looseMCTruth(list_name='e+:corrected',
#                path=mypath)

## reconstruct J/psi -> e+ e- decay
ma.reconstructDecay('J/psi:ee -> e+:corrected e-:corrected', '2.8 < M < 3.2 and nTracks > 4 and useCMSFrame(p) < 2.', path=mypath)
ma.reconstructDecay('J/psi:mumu -> mu+:good mu-:good', '2.8 < M < 3.2 and nTracks > 4 and useCMSFrame(p) < 2.', path=mypath)

#vx.vertexRave('J/psi:ee', 0., 'J/psi:ee -> ^e+ ^e-', 'ipprofile', path=mypath)
#vx.vertexRave('J/psi:mumu', 0., 'J/psi:mumu -> ^mu+ ^mu-', 'ipprofile', path=mypath)
#ma.rankByHighest('J/psi:ee',   'chiProb',numBest=3, outputVariable='jpsi_rank', path=mypath)
#ma.rankByHighest('J/psi:mumu', 'chiProb',numBest=3, outputVariable='jpsi_rank', path=mypath)
#ma.variables.addAlias('jpsi_rank', 'extraInfo(jpsi_rank)')

#ma.looseMCTruth(list_name='J/psi:ee', path=mypath)
#ma.looseMCTruth(list_name='J/psi:mumu', path=mypath)


#sc.stdPi('good')
#sc.stdK('good')
ma.fillParticleList(decayString='pi+:good',cut='chiProb > 0.001 and pionID > 0.1',path=mypath)
ma.fillParticleList(decayString='K+:good',cut='chiProb > 0.001 and kaonID > 0.1',path=mypath)

##psi(2S) reconstruction
ma.reconstructDecay(decayString='psi(2S):ee -> J/psi:ee pi+:good pi-:good', cut="3.6 < M < 3.8", path=mypath)

ma.reconstructDecay(decayString='psi(2S):den -> e+:corrected e-:corrected', cut="3.6 < M < 3.8 and nTracks > 4 and useCMSFrame(p) < 3.", path=mypath)
ma.reconstructDecay(decayString='psi(2S):gen -> mu+:good mu-:good', cut="3.6 < M < 3.8 and nTracks > 4 and useCMSFrame(p) < 3.", path=mypath)

ma.V0ListMerger("J/psi:mumu","J/psi:ee",1,path=mypath)

ma.reconstructDecay(decayString='psi(2S):mumu -> J/psi:mumu pi+:good pi-:good', cut="3.6 < M < 3.8", path=mypath)

#ma.rankByHighest('K+:good',   'kaonID',numBest=3, outputVariable='k_rank', path=mypath)
#ma.variables.addAlias('k_rank', 'extraInfo(k_rank)')
#ma.fillParticleList(decayString='pi+:good',
#                    cut='d0 < 2 and abs(z0) < 4 and chiProb > 0.001 and pionID > 0.5',
#                    path=mypath)
#ma.fillParticleList(decayString='K+:good',
#                    cut='d0 < 2 and abs(z0) < 4 and chiProb > 0.001 and kaonID > 0.5',
#                    path=mypath)

# reconstruct Ks -> pi+ pi- decay
# keep only candidates with dM<0.25
##ma.reconstructDecay('K_S0:pipi -> pi+:good pi-:good', 'dM<0.25', path=mypath)

ma.fillParticleList(decayString='K_S0:pipi -> pi+:good pi-:good', cut='0.3 < M < 0.7', path=mypath)
ma.vertexKFit(list_name='K_S0:pipi', conf_level=0.0, path=mypath)

#vx.vertexRave('K_S0:pipi', 0., 'K_S0:pipi -> ^pi+:good ^pi-:good', '', path=mypath)
#ma.rankByHighest('K_S0:pipi',   'chiProb',numBest=3, outputVariable='ks_rank', path=mypath)
#ma.variables.addAlias('ks_rank', 'extraInfo(ks_rank)')


# reconstruct B0 -> psi(2S) Ks decay
# keep only candidates with Mbc > 5.1 and abs(deltaE)<0.25
ma.reconstructDecay('B0:psi2s_eeks -> psi(2S):ee K_S0:pipi', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)
ma.reconstructDecay('B0:psi2s_mumuks -> psi(2S):mumu K_S0:pipi', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)
ma.reconstructDecay('B0:psi2s_denks -> psi(2S):den K_S0:pipi', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)
ma.reconstructDecay('B0:psi2s_genks -> psi(2S):gen K_S0:pipi', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)

# reconstruct B+ -> psi(2S) K+ decay
# keep only candidates with Mbc > 5.1 and abs(deltaE)<0.5
ma.reconstructDecay('B+:psi2s_eekp -> psi(2S):ee K+:good', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)
ma.reconstructDecay('B+:psi2s_mumukp -> psi(2S):mumu K+:good', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)
ma.reconstructDecay('B+:psi2s_denkp -> psi(2S):den K+:good', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)
ma.reconstructDecay('B+:psi2s_genkp -> psi(2S):gen K+:good', 'Mbc > 5.2 and abs(deltaE)<0.15', path=mypath)

# perform MC matching (MC truth asociation)
#ma.matchMCTruth('B0:psi2s_eeks', path=mypath)
#ma.matchMCTruth('B0:psi2s_mumuks', path=mypath)
#ma.matchMCTruth('B+:psi2s_eekp', path=mypath)
#ma.matchMCTruth('B+:psi2s_mumukp', path=mypath)

# Fit the B0 Vertex
vx.vertexRave('B0:psi2s_eeks', 0., 'B0 -> [psi(2S):ee -> [J/psi:ee -> ^e+ ^e-] ^pi+ ^pi-] K_S0:pipi', '', path=mypath)
vx.vertexRave('B0:psi2s_mumuks', 0., 'B0 -> [psi(2S):mumu -> [J/psi:mumu -> ^mu+ ^mu-] ^pi+ ^pi-] K_S0:pipi', '', path=mypath)
vx.vertexRave('B0:psi2s_denks', 0., 'B0 -> [psi(2S):den -> ^e+ ^e-] K_S0:pipi', '', path=mypath)
vx.vertexRave('B0:psi2s_genks', 0., 'B0 -> [psi(2S):gen -> ^mu+ ^mu-] K_S0:pipi','', path=mypath)

vx.vertexRave('B+:psi2s_eekp', 0., 'B+ -> [psi(2S):ee -> [J/psi:ee -> ^e+ ^e-] ^pi+ ^pi-] K+:good', '', path=mypath)
vx.vertexRave('B+:psi2s_mumukp', 0., 'B+ -> [psi(2S):mumu -> [J/psi:mumu -> ^mu+ ^mu-] ^pi+ ^pi-] K+:good', '', path=mypath)
vx.vertexRave('B+:psi2s_denkp', 0., 'B+ -> [psi(2S):den -> ^e+ ^e-]  K+:good', '', path=mypath)
vx.vertexRave('B+:psi2s_genkp', 0., 'B+ -> [psi(2S):mumu -> ^mu+ ^mu-] K+:good', '', path=mypath)

ma.rankByHighest('B0:psi2s_eeks',   'chiProb',numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B0:psi2s_mumuks', 'chiProb',numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B0:psi2s_denks', 'chiProb', numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B0:psi2s_genks', 'chiProb', numBest=3, outputVariable='B_vtx_rank', path=mypath)

ma.rankByHighest('B+:psi2s_eekp',   'chiProb',numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B+:psi2s_mumukp', 'chiProb',numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B+:psi2s_denkp',   'chiProb',numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B+:psi2s_genkp', 'chiProb',numBest=3, outputVariable='B_vtx_rank', path=mypath)

ma.variables.addAlias('B_vtx_rank', 'extraInfo(B_vtx_rank)')

vx.vertexRave('B0:psi2s_eeks', 0., 'B0 -> psi(2S):ee [K_S0:pipi -> ^pi+ ^pi-]', '', path=mypath)
vx.vertexRave('B0:psi2s_mumuks', 0., 'B0 -> psi(2S):mumu [K_S0:pipi -> ^pi+ ^pi-]', '', path=mypath)
vx.vertexRave('B0:psi2s_denks', 0., 'B0 -> psi(2S):den  [K_S0:pipi -> ^pi+ ^pi-]', '', path=mypath)
vx.vertexRave('B0:psi2s_genks', 0., 'B0 -> psi(2S):gen  [K_S0:pipi -> ^pi+ ^pi-]','', path=mypath)

ma.rankByHighest('B0:psi2s_eeks',   'daughter(1, chiProb)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.rankByHighest('B0:psi2s_mumuks', 'daughter(1, chiProb)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.rankByHighest('B0:psi2s_denks',   'daughter(1, chiProb)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.rankByHighest('B0:psi2s_genks', 'daughter(1, chiProb)',numBest=3, outputVariable='B_k_rank', path=mypath)

ma.rankByHighest('B+:psi2s_eekp',   'daughter(1, kaonID)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.rankByHighest('B+:psi2s_mumukp', 'daughter(1, kaonID)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.rankByHighest('B+:psi2s_denkp',   'daughter(1, kaonID)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.rankByHighest('B+:psi2s_genkp', 'daughter(1, kaonID)',numBest=3, outputVariable='B_k_rank', path=mypath)
ma.variables.addAlias('B_k_rank', 'extraInfo(B_k_rank)')

# build the rest of the event associated to the B0
ma.buildRestOfEvent(target_list_name='B0:psi2s_eeks', path=mypath)
ma.buildRestOfEvent(target_list_name='B0:psi2s_mumuks', path=mypath)
ma.buildRestOfEvent(target_list_name='B0:psi2s_denks', path=mypath)
ma.buildRestOfEvent(target_list_name='B0:psi2s_genks', path=mypath)

ma.buildRestOfEvent(target_list_name='B+:psi2s_eekp', path=mypath)
ma.buildRestOfEvent(target_list_name='B+:psi2s_mumukp', path=mypath)
ma.buildRestOfEvent(target_list_name='B+:psi2s_denkp', path=mypath)
ma.buildRestOfEvent(target_list_name='B+:psi2s_genkp', path=mypath)

# Before using the Flavor Tagger you need at least the default weight files. If you do not set
# any parameter the flavorTagger downloads them automatically from the database.
# You just have to use a special global tag of the conditions database. Check in
# https://confluence.desy.de/display/BI/Physics+FlavorTagger
# E.g. for release-00-09-01
#use_central_database("GT_gen_prod_003.11_release-00-09-01-FEI-a")
# The default working directory is '.'
# If you have an own analysis package it is recomended to use
# workingDirectory = os.environ['BELLE2_LOCAL_DIR'] + '/analysis/data'.
# Note that if you also train by yourself the weights of the trained Methods are saved therein.
# To save CPU time the weight files should be saved in the same server were you run.
#
# NEVER set uploadToDatabaseAfterTraining to True if you are not a librarian!!!
#
# Flavor Tagging Function. Default Expert mode to use the default weight files for the B2JpsiKs_mu channel.
#flavorTagger(
#    particleLists=['B0:jpsiks'],
#    weightFiles='B2JpsiKs_muBGx1',
#    workingDirectory=os.environ['BELLE2_LOCAL_DIR'] + '/analysis/data')
#
## You can apply cuts using the flavor Tagger: qrOutput(FBDT) > -2 rejects all events which do not
## provide flavor information using the tag side
#applyCuts('B0:jpsiks', 'qrOutput(FBDT) > -2')
#
## If you applied the cut on qrOutput(FBDT) > -2 before then you can rank by highest r- factor
#rankByHighest('B0:jpsiks', 'abs(qrOutput(FBDT))', 0, 'Dilution_rank')

# Fit Vertex of the B0 on the tag side
vx.TagV('B0:psi2s_eeks', 'breco', 0.001, 'standard_PXD', path=mypath)
vx.TagV('B0:psi2s_mumuks', 'breco', 0.001, 'standard_PXD', path=mypath)
vx.TagV('B0:psi2s_denks', 'breco', 0.001, 'standard_PXD', path=mypath)
vx.TagV('B0:psi2s_genks', 'breco', 0.001, 'standard_PXD', path=mypath)

vx.TagV('B+:psi2s_eekp', 'breco', 0.001, 'standard_PXD', path=mypath)
vx.TagV('B+:psi2s_mumukp', 'breco', 0.001, 'standard_PXD', path=mypath)
vx.TagV('B+:psi2s_denkp', 'breco', 0.001, 'standard_PXD', path=mypath)
vx.TagV('B+:psi2s_genkp', 'breco', 0.001, 'standard_PXD', path=mypath)

buildEventKinematics(path=mypath)
buildEventShape(path=mypath)

kinematics = ['px','py','pz','pt','p','E']
cms_kinematics = create_aliases(kinematics, "useCMSFrame({variable})","CMS")
my_cluster = ['clusterE', 'clusterEoP', 'clusterTheta', 'nMatchedKLMClusters', 'klmClusterLayers']
#rank = ['chiProb','jpsi_rank','ks_rank','k_rank']
rank = ['chiProb','B_vtx_rank','B_k_rank']

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
           vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
               decay_string='B0:psi2s_eeks -> ^psi(2S):ee ^K_S0:pipi') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass +  vc.pid + my_cluster + vc.track + vc.track_hits,
        decay_string='B0:psi2s_eeks -> [psi(2S):ee -> [^J/psi:ee -> [^e+:corrected -> ^e+:uncorrected gamma:all] [^e-:corrected -> ^e-:uncorrected gamma:all]] ^pi+:good ^pi-:good] [K_S0:pipi -> ^pi+ ^pi-]')

B0den_vars = vc.kinematics + \
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
           vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
               decay_string='B0:psi2s_denks -> ^psi(2S):den ^K_S0:pipi') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.pid + my_cluster + vc.track + vc.track_hits,
        decay_string='B0:psi2s_denks -> [^psi(2S):den -> [^e+:corrected -> ^e+:uncorrected gamma:all] [^e-:corrected -> ^e-:uncorrected gamma:all]] [K_S0:pipi -> ^pi+ ^pi-]')

B0m_vars = vc.kinematics + \
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
           vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics  + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
               decay_string='B0:psi2s_mumuks -> ^psi(2S):mumu ^K_S0:pipi') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.pid + my_cluster + vc.track + vc.track_hits,
        decay_string='B0:psi2s_mumuks -> [^psi(2S):mumu -> [^J/psi:mumu -> ^mu+ ^mu-] ^pi+:good ^pi-:good] [K_S0:pipi -> ^pi+ ^pi-]')

B0gen_vars = vc.kinematics + \
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
           vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics  + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
               decay_string='B0:psi2s_genks -> ^psi(2S):gen ^K_S0:pipi') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.pid + my_cluster + vc.track + vc.track_hits,
        decay_string='B0:psi2s_genks -> [psi(2S):gen -> ^mu+ ^mu-]  [K_S0:pipi -> ^pi+ ^pi-]')

Bpe_vars = vc.kinematics + \
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
           vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
               decay_string='B+:psi2s_eekp -> ^psi(2S):ee ^K+:good') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.pid + my_cluster + vc.track + vc.track_hits + rank,
        decay_string='B+:psi2s_eekp -> [psi(2S):ee -> [^J/psi:ee -> [^e+:corrected -> ^e+:uncorrected gamma:all] [^e-:corrected -> ^e-:uncorrected gamma:all]] pi+:good pi-:good] K+:good')

Bpden_vars = vc.kinematics + \
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
           vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
               decay_string='B+:psi2s_denkp -> ^psi(2S):den ^K+:good') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.pid + my_cluster + vc.track + vc.track_hits + rank,
        decay_string='B+:psi2s_eekp -> [psi(2S):den -> [^e+:corrected -> ^e+:uncorrected gamma:all] [^e-:corrected -> ^e-:uncorrected gamma:all]] K+:good')

Bpm_vars = vc.kinematics + \
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
    vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
        decay_string='B+:psi2s_mumukp -> ^psi(2S):mumu ^K+:good') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.pid + my_cluster + vc.track + vc.track_hits + rank,
        decay_string='B+:psi2s_mumukp -> [psi(2S):mumu -> [^J/psi:mumu -> ^mu+ ^mu-] pi+:good pi-:good]  K+:good')

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
    vu.create_aliases_for_selected(
    list_of_variables=vc.kinematics + cms_kinematics + vc.inv_mass + vc.mc_truth + vc.mc_kinematics,
        decay_string='B+:psi2s_genkp -> ^psi(2S):gen ^K+:good') + \
    vu.create_aliases_for_selected(
        list_of_variables=vc.kinematics + cms_kinematics + vc.pid + my_cluster + vc.track + vc.track_hits + rank,
        decay_string='B+:psi2s_genkp -> [psi(2S):gen -> ^mu+ ^mu-]  K+:good')

rootOutputFile = os.environ['OUTPUT']

ma.variablesToNtuple('B0:psi2s_eeks', B0e_vars,
                     filename=rootOutputFile,
                     treename='b0e',
                     path=mypath)
ma.variablesToNtuple('B0:psi2s_mumuks', B0m_vars,
                     filename=rootOutputFile,
                     treename='b0m',
                     path=mypath)
ma.variablesToNtuple('B0:psi2s_denks', B0den_vars,
                     filename=rootOutputFile,
                     treename='b0den',
                     path=mypath)
ma.variablesToNtuple('B0:psi2s_genks', B0gen_vars,
                     filename=rootOutputFile,
                     treename='b0gen',
                     path=mypath)
ma.variablesToNtuple('B+:psi2s_eekp', Bpe_vars,
                     filename=rootOutputFile,
                     treename='bpe',
                     path=mypath)
ma.variablesToNtuple('B+:psi2s_mumukp', Bpm_vars,
                     filename=rootOutputFile,
                     treename='bpm',
                     path=mypath)
ma.variablesToNtuple('B+:psi2s_denkp', Bpden_vars,
                     filename=rootOutputFile,
                     treename='bpden',
                     path=mypath)
ma.variablesToNtuple('B+:psi2s_genkp', Bpgen_vars,
                     filename=rootOutputFile,
                     treename='bpgen',
                     path=mypath)

## create and fill flat Ntuple with MCTruth and kinematic information
##ma.toolsDST_ee = ['EventMetaData', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['InvMass[BeforeFit]', 'B0:jpsi_eeks -> ^J/psi:ee K_S0:pipi']
##ma.toolsDST_ee += ['CMSKinematics', 'B0:jpsi_eeks -> ^J/psi:ee ^K_S0:pipi']
##ma.toolsDST_ee += ['RecoStats', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['DeltaEMbc', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['Vertex', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['MCVertex', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['TagVertex', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['PID', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['Track', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['MCTruth', '^B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [^K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['TagVertex', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['DeltaT', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['MCTagVertex', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['MCDeltaT', '^B0:jpsi_eeks']
##ma.toolsDST_ee += ['CustomFloats[d0]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[d0Err]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[omega]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[omegaErr]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[phi0]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[phi0Err]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[tanlambda]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[tanlambdaErr]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[z0]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[z0Err]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[mcPX]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[mcPY]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[mcPZ]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[px]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[py]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[pz]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[pxErr]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[pyErr]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[pzErr]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##
##ma.toolsDST_ee += ['CustomFloats[mcDX]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[mcDY]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[mcDZ]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[x]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[y]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[z]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[x_uncertainty]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[y_uncertainty]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[z_uncertainty]', 'B0:jpsi_eeks -> [^J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##
##ma.toolsDST_ee += ['CustomFloats[nPXDHits]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[nSVDHits]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[firstPXDLayer]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_ee += ['CustomFloats[firstSVDLayer]', 'B0:jpsi_eeks -> [J/psi:ee -> ^e+ ^e-] [K_S0:pipi -> ^pi+ ^pi-]']
##
##ma.toolsDST_mumu = ['EventMetaData', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['InvMass[BeforeFit]', 'B0:jpsi_mumuks -> ^J/psi:mumu K_S0:pipi']
##ma.toolsDST_mumu += ['CMSKinematics', 'B0:jpsi_mumuks -> ^J/psi:mumu ^K_S0:pipi']
##ma.toolsDST_mumu += ['RecoStats', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['DeltaEMbc', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['Vertex', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['MCVertex', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['TagVertex', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['PID', 'B0:jpsi_mumuks -> [J/psi:mumu -> ^mu+ ^mu-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_mumu += ['Track', 'B0:jpsi_mumuks -> [J/psi:mumu -> ^mu+ ^mu-] [K_S0:pipi -> ^pi+ ^pi-]']
##ma.toolsDST_mumu += ['MCTruth', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['TagVertex', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['DeltaT', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['MCTagVertex', '^B0:jpsi_mumuks']
##ma.toolsDST_mumu += ['MCDeltaT', '^B0:jpsi_mumuks']
##
### write out the flat ntuple
##ma.ntupleFile('B0-KFit-VertexFit_mdst_000001_prod00003520_task00000001.root')
##ma.ntupleTree('B0tree_e', 'B0:jpsi_eeks', toolsDST_ee)
##ma.ntupleTree('B0tree_mu', 'B0:jpsi_mumuks', toolsDST_mumu)
#
## Process the events
##process(analysis_main)
b2.process(mypath)

# print out the summary
print(b2.statistics)
