#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## new preamble for release 04 ###
import basf2 as b2
import modularAnalysis as ma
import variables.collections as vc
import variables.utils as vu
import variables as v
mypath = b2.Path()
import sys
import os

### FIRST TEST FOR THE REAL DATA CDST

## LOADING FILES WITH CENTRAL DATABASE FOR BUCKET 6 // Check Yusa-san's email for any doubts
b2.use_central_database("data_reprocessing_proc9")
#ma.inputMdstList(environmentType='default',
#                 filelist=[
#                 ],
#               path = mypath)
ma.inputMdst(environmentType='default',
             filename=os.environ['FILENAME'],
			 path=mypath)


################################################################################
ma.fillParticleList('K+:all',  '',path=mypath)
ma.fillParticleList('mu+:all', cut='muonID > 0.01',path=mypath)
ma.fillParticleList('pi+:all', '',path=mypath)
ma.fillParticleList('e+:all', cut='electronID > 0.01 and d0 < 2 and abs(z0) < 4',path=mypath)
ma.fillParticleList('gamma:all', cut='E < 1.0',writeOut=False,path=mypath)
################################################################################

########## MC TRUTH MATCHING ###############################################
ma.cutAndCopyList("mu+:gen", "mu+:all", "charge>0",path=mypath)
ma.cutAndCopyList("mu-:gen", "mu+:all", "charge<0",path=mypath)
ma.reconstructDecay(decayString="psi(2S):gen -> mu+:gen mu-:gen",
                    cut="3.5 < M < 3.8 ",
                    path=mypath)

v.variables.addAlias('mu_EoP','daughter(0,clusterEoP)')
v.variables.addAlias('psi2smuid','daughter(0,muonID)')

ma.reconstructDecay(decayString="J/psi:gen -> mu+:gen mu-:gen",
                    cut="2.9 < M < 3.2",
                    path=mypath)

ma.correctFSR("e+:cor","e+:all","gamma:all",angleThreshold=5., energyThreshold=1., writeOut=False,path=mypath) #from Yusa-san's steering
ma.cutAndCopyList("e+:gen", "e+:cor", "charge>0",path=mypath)
ma.cutAndCopyList("e-:gen", "e+:cor", "charge<0",path=mypath)
ma.reconstructDecay(decayString="psi(2S):den -> e+:gen e-:gen",
                    cut="3.5 < M < 3.8",
                    path=mypath)

v.variables.addAlias('e_EoP','daughter(0,clusterEoP)')
v.variables.addAlias('psi2seid','daughter(0,electronID)')


ma.reconstructDecay(decayString="J/psi:den -> e+:gen e-:gen",
                    cut="2.9 < M < 3.2",
                    path=mypath)


chiProb=["chiProb"]
EoP=['clusterEoP']
piid=['pionID']
mueop=['mu_EoP']
kaid=['kaonID']
psi2smuid=['psi2smuid']
psi2seid=['psi2seid']

psi2s_vars = vc.kinematics + vc.inv_mass +  chiProb + mueop + psi2smuid + psi2seid

kp_vars = vc.kinematics + vc.inv_mass + chiProb + kaid

lep_vars = EoP

pion_vars = piid

ma.cutAndCopyList("pi+:rec", "pi+:all", "charge>0 and pionID > 0.1",path=mypath)
ma.cutAndCopyList("pi-:rec", "pi+:all", "charge<0 and pionID > 0.1",path=mypath)
ma.reconstructDecay("K_S0:rec -> pi+:rec pi-:rec",cut="0.3 < M < 0.7",path=mypath)

v.variables.addAlias('pi1_ID','daughter(0, pionID)')
pi1id=['pi1_ID']
k0s_vars =  vc.kinematics + vc.inv_mass + chiProb + pi1id

ma.reconstructDecay("psi(2S):jpsi -> J/psi:gen pi+:rec pi-:rec",cut="3.5 < M < 3.8",path=mypath)

v.variables.addAlias('mujpsieop','daughter(0,daughter(0,clusterEoP))')
v.variables.addAlias('psi2spi','daughter(1,pionID)')

mujpsieop=['mujpsieop']
psi2spi=['psi2spi']

psi2sjpsi_vars = vc.kinematics + vc.inv_mass + chiProb + mujpsieop + psi2spi

ma.reconstructDecay("psi(2S):jpsiden -> J/psi:den pi+:rec pi-:rec",cut="3.5 < M < 3.8",path=mypath)

ma.cutAndCopyList("K+:pos","K+:all", "charge > 0 and kaonID > 0.1", path=mypath)

# Fit the B0 Vertex
ma.reconstructDecay("B0:recgen -> psi(2S):gen K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recden -> psi(2S):den K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recjpsi -> psi(2S):jpsi K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recjpsiden -> psi(2S):jpsiden K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)

ma.vertexRave("B0:recgen", 0., "B0 -> [psi(2S):gen -> ^mu+ ^mu-] K_S0:rec", "",path=mypath)
ma.vertexRave("B0:recden", 0., "B0 -> [psi(2S):den -> ^e+ ^e-] K_S0:rec", "",path=mypath)
ma.vertexRave("B0:recjpsi", 0., "B0 -> [psi(2S):jpsi -> [J/psi:gen -> ^mu+ ^mu-] ^pi+ ^pi-] K_S0:rec", "",path=mypath)
ma.vertexRave("B0:recjpsiden", 0., "B0 -> [psi(2S):jpsiden -> [J/psi:den -> ^e+ ^e-] ^pi+ ^pi-] K_S0:rec", "",path=mypath)

ma.rankByHighest('B0:recgen', 'chiProb', numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B0:recden', 'chiProb', numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B0:recjpsi', 'chiProb', numBest=3, outputVariable='B_vtx_rank', path=mypath)
ma.rankByHighest('B0:recjpsiden', 'chiProb', numBest=3, outputVariable='B_vtx_rank', path=mypath)
v.variables.addAlias('B_vtx_rank', 'extraInfo(B_vtx_rank)')

ma.reconstructDecay("B+:recgen -> psi(2S):gen K+:pos",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B+:recden -> psi(2S):den K+:pos",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B+:recjpsi -> psi(2S):jpsi K+:pos",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B+:recjpsiden -> psi(2S):jpsiden K+:pos",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)

# Fit the B+ Vertex
ma.vertexRave("B+:recgen", 0., "B+ -> [psi(2S):gen -> ^mu+ ^mu-] K+:pos", "",path=mypath)
ma.vertexRave("B+:recden", 0., "B+ -> [psi(2S):den -> ^e+ ^e-] K+:pos", "",path=mypath)
ma.vertexRave("B+:recjpsi", 0., "B+ -> [psi(2S):jpsi -> [J/psi:gen -> ^mu+ ^mu-] ^pi+ ^pi-] K+:pos", "",path=mypath)
ma.vertexRave("B+:recjpsiden", 0., "B+ -> [psi(2S):jpsiden -> [J/psi:den -> ^e+ ^e-] ^pi+ ^pi-] K+:pos", "",path=mypath)

ma.rankByHighest('B+:recgen', 'chiProb', numBest=3, outputVariable='Bp_vtx_rank', path=mypath)
ma.rankByHighest('B+:recden', 'chiProb', numBest=3, outputVariable='Bp_vtx_rank', path=mypath)
ma.rankByHighest('B+:recjpsi', 'chiProb', numBest=3, outputVariable='Bp_vtx_rank', path=mypath)
ma.rankByHighest('B+:recjpsiden', 'chiProb', numBest=3, outputVariable='Bp_vtx_rank', path=mypath)
v.variables.addAlias('Bp_vtx_rank', 'extraInfo(Bp_vtx_rank)')

#################### B0 -> [psi(2S) -> l+ l-] K_S0 daughter variables ######################
v.variables.addAlias('b0psi2smuEoP','daughter(0,daughter(0,clusterEoP))')
v.variables.addAlias('b0psi2seEoP','daughter(0,daughter(0,daughter(0,clusterEoP)))')
v.variables.addAlias('b0psi2sinvM','daughter(0,M)')
v.variables.addAlias('b0psi2sp','daughter(0,p)')
v.variables.addAlias('b0psi2spx','daughter(0,px)')
v.variables.addAlias('b0psi2spy','daughter(0,py)')
v.variables.addAlias('b0psi2spz','daughter(0,pz)')
v.variables.addAlias('b0psi2spt','daughter(0,pt)')
v.variables.addAlias('b0psi2scostheta','daughter(0,cosTheta)')
v.variables.addAlias('b0psi2smuID','daughter(0,daughter(0,muonID))')
v.variables.addAlias('b0psi2seID','daughter(0,daughter(0,daughter(0,electronID)))')
###########################################################################################

#################### B0 -> [psi(2S) -> [J/psi -> l+ l-] pi+ pi-] K_S0 daughter variables ######################
v.variables.addAlias('b0psi2sjpsimuEoP','daughter(0,daughter(0,daughter(0,clusterEoP)))')
v.variables.addAlias('b0psi2sjpsieEoP','daughter(0,daughter(0,daughter(0,daughter(0,clusterEoP))))')
v.variables.addAlias('b0psi2sjpsiinvM','daughter(0,daughter(0,M))')
v.variables.addAlias('b0psi2sjpsip','daughter(0,p)')
v.variables.addAlias('b0psi2sjpsipx','daughter(0,daughter(0,px))')
v.variables.addAlias('b0psi2sjpsipy','daughter(0,daughter(0,py))')
v.variables.addAlias('b0psi2sjpsipz','daughter(0,daughter(0,pz))')
v.variables.addAlias('b0psi2sjpsipt','daughter(0,daughter(0,pt))')
v.variables.addAlias('b0psi2sjpsicostheta','daughter(0,daughter(0,cosTheta))')
v.variables.addAlias('b0psi2sjpsimuID','daughter(0,daughter(0,daughter(0,muonID)))')
v.variables.addAlias('b0psi2sjpsieID','daughter(0,daughter(0,daughter(0,daughter(0,electronID))))')
v.variables.addAlias('b0psi2sjpsipiID','daughter(0,daughter(1,pionID))')
################################################################################################################

################### Common daughthers ##################################
v.variables.addAlias('b0k0spiID','daughter(1,daughter(0,pionID))')
v.variables.addAlias('b0k0sM','daughter(1,M)')
v.variables.addAlias('b0k0sp','daughter(1,p)')
v.variables.addAlias('b0k0spx','daughter(1,px)')
v.variables.addAlias('b0k0spy','daughter(1,py)')
v.variables.addAlias('b0k0spz','daughter(1,pz)')
v.variables.addAlias('b0k0spt','daughter(1,pt)')
v.variables.addAlias('b0k0scostheta','daughter(1,cosTheta)')

v.variables.addAlias('bpkaID','daughter(1,kaonID)')
v.variables.addAlias('bpkaM','daughter(1,M)')
v.variables.addAlias('bpkap','daughter(1,p)')
v.variables.addAlias('bpkapx','daughter(1,px)')
v.variables.addAlias('bpkapy','daughter(1,py)')
v.variables.addAlias('bpkapz','daughter(1,pz)')
v.variables.addAlias('bpkapt','daughter(1,pt)')
v.variables.addAlias('bpkacostheta','daughter(1,cosTheta)')
#######################################################################

rankB0 = ['B_vtx_rank']
rankBp = ['Bp_vtx_rank']

b0psi2smu=['b0psi2smuEoP']
b0psi2se=['b0psi2seEoP']
b0psi2skin=['b0psi2sinvM','b0psi2sp','b0psi2spx','b0psi2spy','b0psi2spz','b0psi2spt','b0psi2scostheta']
b0psi2smuID=['b0psi2smuID']
b0psi2seID=['b0psi2seID']

b0psi2sjpsimu=['b0psi2sjpsimuEoP']
b0psi2sjpsie=['b0psi2sjpsieEoP']
b0psi2sjpsikin=['b0psi2sjpsiinvM','b0psi2sjpsip','b0psi2sjpsipx','b0psi2sjpsipy','b0psi2sjpsipz','b0psi2sjpsipt','b0psi2sjpsicostheta']
b0psi2sjpsimuID=['b0psi2sjpsimuID']
b0psi2sjpsieID=['b0psi2sjpsieID']

b0k0spi=['b0k0spiID','b0k0sM','b0k0sp','b0k0spx','b0k0spy','b0k0spz','b0k0spt','b0k0scostheta']
b0psi2sjpsipi=['b0psi2sjpsipiID']

bpka=['bpkaID','bpkaM','bpkap','bpkapx','bpkapy','bpkapz','bpkapt','bpkacostheta']

#b0_vars = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2smu + b0psi2smuID + b0psi2seID + b0k0spi + rankB0 + b0psi2skin

b0_jpsi_vars_mu = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2sjpsimu + b0psi2sjpsimuID + b0psi2sjpsipi + b0k0spi + rankB0 + b0psi2sjpsikin
b0_jpsi_vars_e = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2sjpsie + b0psi2sjpsieID + b0psi2sjpsipi + b0k0spi + rankB0 + b0psi2sjpsikin

b0_vars_mu =  vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2smu + b0psi2smuID + b0k0spi + rankB0 + b0psi2skin
b0_vars_e =  vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2se + b0psi2seID + b0k0spi + rankB0 + b0psi2skin

bp_vars_mu = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2smu + b0psi2smuID + bpka + rankBp + b0psi2skin
bp_vars_e = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2se + b0psi2seID + bpka + rankBp + b0psi2skin

bp_jpsi_vars_mu = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2sjpsimu + b0psi2sjpsimuID + b0psi2sjpsipi + bpka + rankBp + b0psi2sjpsikin
bp_jpsi_vars_e = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2sjpsie + b0psi2sjpsieID + b0psi2sjpsipi + bpka + rankBp + b0psi2sjpsikin

##############################################################################

################### Saving variables to ntuple ##############################
rootOutputFile =os.environ['OUTPUT']


ma.variablesToNtuple(decayString="B0:recgen",
                  variables=b0_vars_mu,
                  treename="B0_recgen_psi2smumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recden",
                  variables=b0_vars_e,
                  treename="B0_recden_psi2see",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recjpsi",
                  variables=b0_jpsi_vars_mu,
                  treename="B0_recgen_psi2sjpsimumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recjpsiden",
                  variables=b0_jpsi_vars_e,
                  treename="B0_recden_psi2sjpsiee",
                  filename=rootOutputFile,
                  path=mypath)
ma.variablesToNtuple(decayString="B+:recgen",
                  variables=bp_vars_mu,
                  treename="Bp_recgen_psi2smumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recden",
                  variables=bp_vars_e,
                  treename="Bp_recden_psi2see",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recjpsi",
                  variables=bp_jpsi_vars_mu,
                  treename="Bp_recgen_psi2sjpsimumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recjpsiden",
                  variables=bp_jpsi_vars_e,
                  treename="Bp_recden_psi2sjpsiee",
                  filename=rootOutputFile,
                  path=mypath)
####################################################################

# process the events
b2.process(mypath)

# print out the summary
print(b2.statistics)
