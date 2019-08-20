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
ma.fillParticleList('mu+:loose', cut='muonID > 0.01',path=mypath)
ma.fillParticleList('mu+:tight', cut='muonID > 0.95', path=mypath)
ma.fillParticleList('e+:loose', cut='electronID > 0.01 and d0 < 2 and abs(z0) < 4',path=mypath)
ma.fillParticleList('e+:tight', cut='electronID > 0.95 and abs(dr) < 2 and abs(dz) < 5 and useLabFrame(p) > 0.1', path=mypath)
ma.fillParticleList('gamma:all', cut='E < 1.0',writeOut=False,path=mypath)
ma.fillParticleList('pi+:all', cut='pionID > 0.1', path=mypath)
################################################################################

ma.reconstructDecay(decayString="J/psi:gen -> mu+:loose mu-:loose",
                    cut="2.9 < M < 3.2 and foxWolframR2 < 0.4 and useRestFrame(p) < 2",
                    path=mypath)

ma.reconstructDecay(decayString="psi(2S):gen -> mu+:loose mu-:loose", cut="3.5 < M < 3.8", path=mypath)

ma.reconstructDecay(decayString='psi(2S):jpsim -> J/psi:gen pi+:all pi-:all', cut="3.5 < M < 3.8", path=mypath)

ma.correctFSR("e+:loosecor","e+:loose","gamma:all",angleThreshold=5., energyThreshold=1., writeOut=False,path=mypath) #correction from Takeo-san (mu+ and mu- not needed)
ma.correctFSR("e+:tightcor","e+:tight","gamma:all",angleThreshold=5., energyThreshold=1., writeOut=False,path=mypath) #from Yusa-san's steering

ma.reconstructDecay(decayString="J/psi:den -> e+:loosecor e-:loosecor",
                    cut="2.9 < M < 3.2",
                    path=mypath)

ma.reconstructDecay(decayString="psi(2S):den -> e+:loosecor e-:loosecor", cut="3.5 < M < 3.8", path=mypath)

ma.reconstructDecay(decayString='psi(2S):jpsie -> J/psi:den pi+:all pi-:all', cut="3.5 < M < 3.8", path=mypath)

chiProb=["chiProb"]
EoP=['clusterEoP']
costheta=['cosTheta']
p123=['px','py','pz']

psi2s_vars = vc.mc_truth + vc.kinematics + vc.inv_mass + vc.mc_variables + chiProb + EoP+ p123

##############################################################################

################### Saving variables to ntuple ##############################
rootOutputFile =os.environ['OUTPUT']

ma.variablesToNtuple(decayString="J/psi:gen",
                  variables=psi2s_vars,
                  treename="J/psi(mumu)",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="psi(2S):gen",
		  variables=psi2s_vars,
		  treename="psi(2S)(mumu)",
		  filename=rootOutputFile,
		  path=mypath)

ma.variablesToNtuple(decayString="psi(2S):jpsim",
		  variables=psi2s_vars,
		  treename="psi(2S)(jpsimpipi)",
		  filename=rootOutputFile,
		  path=mypath)

ma.variablesToNtuple(decayString="J/psi:den",
                  variables=psi2s_vars,
                  treename="J/psi(ee)",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="psi(2S):den",
		  variables=psi2s_vars,
		  treename="psi(2S)(ee)",
	   	  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="psi(2S):jpsie",
		  variables=psi2s_vars,
		  treename="psi(2S)(jpsiepipi)",
	   	  filename=rootOutputFile,
                  path=mypath)

####################################################################

# process the events
b2.process(mypath)

# print out the summary
print(b2.statistics)
