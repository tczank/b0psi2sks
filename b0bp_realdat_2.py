#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## to be deprecated in release 04 ####
#from basf2 import *
#from modularAnalysis import *
##########################

## new preamble for release 04 ###
import basf2 as b2
import modularAnalysis as ma
import variables.collections as vc
import variables.utils as vu
import variables as v
mypath = b2.Path()

#ma.inputMdst(environmentType='default',
#           filename=b2.find_file('/home/thczank/b0psi2sks/gsim/psi2smumu/b0_psi2s_gsim_psi2smumu_all.root'),
#           path=mypath)

#ma.inputMdstList(environmentType='default',
#                filelist=['/home/thczank/b0psi2sks/gsim/psi2smumu/b0_psi2s_gsim_psimumu_0.root','/home/thczank/b0psi2sks/gsim/psi2smumu/b0_psi2s_gsim_psimumu_1.root'],
#               path = mypath)

### FIRST TEST FOR THE REAL DATA CDST

b2.use_central_database("data_reprocessing_prompt_bucket4b")
ma.inputMdstList(environmentType='default',
                 filelist=[
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00909/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00909.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00911/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00911.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00915/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00915.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00916/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00916.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00919/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00919.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00920/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00920.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00921/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00921.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00922/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00922.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00923/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00923.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00924/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00924.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00925/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00925.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00926/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00926.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00927/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00927.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00928/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00928.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00929/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00929.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00930/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00930.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00931/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00931.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00932/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00932.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00933/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00933.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00934/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00934.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00935/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00935.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00936/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00936.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00937/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00937.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00938/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00938.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00939/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00939.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00996/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00996.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00997/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00997.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00998/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00998.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r00999/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.00999.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01000/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01000.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01001/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01001.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01002/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01002.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01003/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01003.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01004/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01004.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01005/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01005.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01135/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01135.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01136/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01136.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01140/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01140.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01141/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01141.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01143/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01143.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01144/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01144.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01145/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01145.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01146/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01146.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01147/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01147.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01148/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01148.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01149/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01149.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01150/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01150.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01151/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01151.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01152/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01152.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01153/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01153.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01154/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01154.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01155/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01155.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01216/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01216.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01217/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01217.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01218/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01218.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01219/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01219.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01220/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01220.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01221/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01221.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01222/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01222.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01223/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01223.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01224/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01224.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01225/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01225.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01226/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01226.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01227/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01227.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01228/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01228.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01230/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01230.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01231/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01231.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01232/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01232.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01233/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01233.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01234/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01234.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01235/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01235.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01299/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01299.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01300/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01300.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01302/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01302.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01303/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01303.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01304/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01304.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01305/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01305.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01306/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01306.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01307/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01307.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01308/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01308.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01309/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01309.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01310/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01310.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01311/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01311.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01312/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01312.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01313/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01313.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01314/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01314.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01315/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01315.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01316/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01316.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01317/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01317.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01318/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01318.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01319/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01319.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01320/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01320.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01321/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01321.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01322/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01322.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01323/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01323.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01324/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01324.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01325/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01325.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01326/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01326.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01327/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01327.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01328/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01328.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01352/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01352.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01353/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01353.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01355/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01355.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01356/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01356.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01357/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01357.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01358/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01358.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01359/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01359.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01360/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01360.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01363/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01363.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01364/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01364.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01367/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01367.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01368/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01368.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01369/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01369.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01370/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01370.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01371/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01371.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01372/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01372.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01373/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01373.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01374/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01374.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01375/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01375.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01376/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01376.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01401/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01401.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01402/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01402.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01409/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01409.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01410/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01410.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01411/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01411.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01417/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01417.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01418/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01418.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01419/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01419.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01420/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01420.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01421/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01421.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01422/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01422.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01423/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01423.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01424/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01424.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01425/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01425.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01426/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01426.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01427/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01427.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01428/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01428.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01429/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01429.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01430/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01430.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01480/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01480.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01481/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01481.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01482/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01482.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01483/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01483.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01484/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01484.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01485/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01485.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01486/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01486.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01487/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01487.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01488/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01488.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01489/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01489.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01490/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01490.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01491/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01491.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01492/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01492.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01494/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01494.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01495/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01495.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01496/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01496.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01497/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01497.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01498/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01498.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01499/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01499.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01500/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01500.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01501/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01501.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01502/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01502.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01503/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01503.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01504/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01504.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01505/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01505.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01506/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01506.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01507/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01507.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01509/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01509.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01513/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01513.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01514/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01514.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01515/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01515.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01516/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01516.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01561/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01561.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01562/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01562.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01563/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01563.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01564/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01564.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01565/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01565.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01566/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01566.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01568/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01568.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01573/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01573.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01578/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01578.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01584/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01584.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01585/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01585.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01586/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01586.root',
'/ghi/fs01/belle2/bdata/Data/e0007/4S/Bucket4/release-03-01-01/DB00000598/r01587/skim/hlt_hadron/cdst/sub00/cdst.physics.hlt_hadron.0007.01587.root',
                 ],
               path = mypath)

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

ma.cutAndCopyList("mu+:gen", "mu+:all", "charge>0",path=mypath)
ma.cutAndCopyList("mu-:gen", "mu+:all", "charge<0",path=mypath)
ma.reconstructDecay(decayString="J/psi:gen -> mu+:gen mu-:gen",
                    cut="2.9 < M < 3.2",
                    path=mypath)
#ma.matchMCTruth(list_name="J/psi:gen",path=mypath)

ma.correctFSR("e+:cor","e+:all","gamma:all",angleThreshold=5., energyThreshold=1., writeOut=False,path=mypath) #from Yusa-san's steering
ma.cutAndCopyList("e+:gen", "e+:cor", "charge>0",path=mypath)
ma.cutAndCopyList("e-:gen", "e+:cor", "charge<0",path=mypath)
ma.reconstructDecay(decayString="psi(2S):den -> e+:gen e-:gen",
                    cut="3.5 < M < 3.8",
                    path=mypath)

v.variables.addAlias('e_EoP','daughter(0,clusterEoP)')
v.variables.addAlias('psi2smuid','daughter(0,muonID)')
v.variables.addAlias('psi2seid','daughter(0,electronID)')


ma.reconstructDecay(decayString="J/psi:den -> e+:gen e-:gen",
                    cut="2.9 < M < 3.2",
                    path=mypath)
#ma.matchMCTruth(list_name="psi(2S):den",path=mypath)
#ma.matchMCTruth(list_name="J/psi:den",path=mypath)


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

ma.cutAndCopyList("pi+:rec", "pi+:all", "charge>0",path=mypath)
ma.cutAndCopyList("pi-:rec", "pi+:all", "charge<0",path=mypath)
ma.reconstructDecay("K_S0:rec -> pi+:rec pi-:rec",cut="0.3 < M < 0.7",path=mypath)
#ma.matchMCTruth("K_S0:rec",path=mypath)

v.variables.addAlias('pi1_ID','daughter(0, pionID)')
pi1id=['pi1_ID']
k0s_vars =  vc.kinematics + vc.inv_mass + chiProb + pi1id

ma.reconstructDecay("psi(2S):jpsi -> J/psi:gen pi+:rec pi-:rec",cut="3.5 < M < 3.8",path=mypath)
#ma.matchMCTruth("psi(2S):gen",path=mypath)

v.variables.addAlias('mujpsieop','daughter(0,daughter(0,clusterEoP))')
v.variables.addAlias('psi2spi','daughter(1,pionID)')

mujpsieop=['mujpsieop']
psi2spi=['psi2spi']

psi2sjpsi_vars = vc.kinematics + vc.inv_mass + chiProb + mujpsieop + psi2spi

ma.reconstructDecay("psi(2S):jpsiden -> J/psi:den pi+:rec pi-:rec",cut="3.5 < M < 3.8",path=mypath)

ma.cutAndCopyList("K+:pos","K+:all", "charge > 0", path=mypath)

ma.reconstructDecay("B0:recgen -> psi(2S):gen K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recden -> psi(2S):den K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recjpsi -> psi(2S):jpsi K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recjpsiden -> psi(2S):jpsiden K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)

# Fit the B0 Vertex
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

v.variables.addAlias('b0psi2smuEoP','daughter(0,daughter(0,clusterEoP))')
v.variables.addAlias('b0psi2smuID','daughter(0,daughter(0,muonID))')
v.variables.addAlias('b0psi2seID','daughter(0,daughter(0,electronID))')

v.variables.addAlias('b0psi2sjpsimuEoP','daughter(0,daughter(0,daughter(0,clusterEoP)))')
v.variables.addAlias('b0psi2sjpsimuID','daughter(0,daughter(0,daughter(0,muonID)))')
v.variables.addAlias('b0psi2sjpsieID','daughter(0,daughter(0,daughter(0,electronID)))')


v.variables.addAlias('b0psi2sjpsipiID','daughter(0,daughter(1,pionID))')

v.variables.addAlias('b0k0spiID','daughter(1,daughter(0,pionID))')
v.variables.addAlias('bpkaID','daughter(1,kaonID)')

rankB0 = ['B_vtx_rank']
rankBp = ['Bp_vtx_rank']

b0psi2smu=['b0psi2smuEoP']
b0psi2smuID=['b0psi2smuID']
b0psi2seID=['b0psi2seID']

b0psi2sjpsimu=['b0psi2sjpsimuEoP']
b0psi2sjpsimuID=['b0psi2sjpsimuID']
b0psi2sjpsieID=['b0psi2sjpsieID']

b0k0spi=['b0k0spiID']
b0psi2sjpsipi=['b0psi2sjpsipiID']

bpka=['bpkaID']

b0_vars = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2smu + b0psi2smuID + b0psi2seID + b0k0spi + rankB0

b0_jpsi_vars = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2sjpsimu + b0psi2sjpsimuID + b0psi2sjpsieID + b0psi2sjpsipi + b0k0spi + rankB0

bp_vars = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2smu + b0psi2smuID + b0psi2seID + bpka + rankBp
bp_jpsi_vars = vc.kinematics + vc.deltae_mbc + vc.track + chiProb + b0psi2sjpsimu + b0psi2sjpsimuID + b0psi2sjpsieID + b0psi2sjpsipi + bpka + rankBp

##############################################################################

################### Saving variables to ntuple ##############################
rootOutputFile = "B0Bp_realdat_bucket4_2ndtest.root"

#ma.variablesToNtuple(decayString="psi(2S):gen",
#                  variables=psi2s_vars,
#                  treename="psi2Smumu",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="psi(2S):den",
#                  variables=psi2s_vars,
#                  treename="psi2See",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="psi(2S):jpsi",
#                  variables=psi2sjpsi_vars,
#                  treename="psi2Sjpsimumu",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="psi(2S):jpsiden",
#                  variables=psi2sjpsi_vars,
#                   treename="psi2Sjpsiee",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="J/psi:gen",
#                  variables=psi2s_vars,
#                  treename="jpsimumu",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="J/psi:den",
#                  variables=psi2s_vars,
#                  treename="jpsiee",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="K_S0:rec",
#                  variables=k0s_vars,
#                  treename="K_S0",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="pi+:all",
#                  variables=pion_vars,
#                  treename="pi",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="e+:cor",
#                  variables=lep_vars,
#                  treename="e",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="mu+:all",
#                  variables=lep_vars,
#                  treename="mu",
#                  filename=rootOutputFile,
#                  path=mypath)

#ma.variablesToNtuple(decayString="K+:all",
#                  variables=kp_vars,
#                  treename="Kp",
#                  filename=rootOutputFile,
#                  path=mypath)

ma.variablesToNtuple(decayString="B0:recgen",
                  variables=b0_vars,
                  treename="B0_recgen_psi2smumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recden",
                  variables=b0_vars,
                  treename="B0_recden_psi2see",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recjpsi",
                  variables=b0_jpsi_vars,
                  treename="B0_recgen_psi2sjpsimumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B0:recjpsiden",
                  variables=b0_jpsi_vars,
                  treename="B0_recden_psi2sjpsiee",
                  filename=rootOutputFile,
                  path=mypath)
ma.variablesToNtuple(decayString="B+:recgen",
                  variables=bp_vars,
                  treename="Bp_recgen_psi2smumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recden",
                  variables=bp_vars,
                  treename="Bp_recden_psi2see",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recjpsi",
                  variables=bp_jpsi_vars,
                  treename="Bp_recgen_psi2sjpsimumu",
                  filename=rootOutputFile,
                  path=mypath)

ma.variablesToNtuple(decayString="B+:recjpsiden",
                  variables=bp_jpsi_vars,
                  treename="Bp_recden_psi2sjpsiee",
                  filename=rootOutputFile,
                  path=mypath)
####################################################################

# process the events
b2.process(mypath)

# print out the summary
print(b2.statistics)
