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
ma.fillParticleList('mu+:all', cut='muonID > 0.01',path=mypath)
ma.fillParticleList('e+:all', cut='electronID > 0.01 and d0 < 2 and abs(z0) < 4',path=mypath)
ma.fillParticleList('gamma:all', cut='E < 1.0',writeOut=False,path=mypath)
################################################################################

ma.reconstructDecay(decayString="J/psi:gen -> mu+:gen mu-:gen",
                    cut="2.9 < M < 3.2",
                    path=mypath)

ma.correctFSR("e+:cor","e+:all","gamma:all",angleThreshold=5., energyThreshold=1., writeOut=False,path=mypath) #from Yusa-san's steering
ma.cutAndCopyList("e+:gen", "e+:cor", "charge>0",path=mypath)
ma.cutAndCopyList("e-:gen", "e+:cor", "charge<0",path=mypath)

ma.reconstructDecay(decayString="J/psi:den -> e+:gen e-:gen",
                    cut="2.9 < M < 3.2",
                    path=mypath)

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

ma.variablesToNtuple(decayString="J/psi:den",
                  variables=psi2s_vars,
                  treename="J/psi(ee)",
                  filename=rootOutputFile,
                  path=mypath)

####################################################################

# process the events
b2.process(mypath)

# print out the summary
print(b2.statistics)
