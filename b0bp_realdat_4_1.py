#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## new preamble for release 04 ###
import basf2 as b2
import modularAnalysis as ma
import variables.collections as vc
import variables.utils as vu
import variables as v
mypath = b2.Path()

### FIRST TEST FOR THE REAL DATA CDST

## LOADING FILES WITH CENTRAL DATABASE FOR BUCKET 6 // Check Yusa-san's email for any doubts
b2.use_central_database("data_reprocessing_prompt_bucket6_cdst")
ma.inputMdstList(environmentType='default',
                 filelist=[
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r00055/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.r00055.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01026/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01026.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01027/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01027.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01028/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01028.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01029/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01029.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01030/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01030.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01031/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01031.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01036/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01036.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01038/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01038.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01039/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01039.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01040/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01040.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01041/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01041.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01053/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01053.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01058/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01058.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01059/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01059.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01060/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01060.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01061/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01061.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01064/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01064.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01065/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01065.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01068/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01068.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01069/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01069.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01070/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01070.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01071/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01071.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01090/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01090.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01092/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01092.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01095/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01095.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01098/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01098.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01099/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01099.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01103/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01103.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01105/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01105.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01116/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01116.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01117/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01117.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01124/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01124.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01125/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01125.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01126/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01126.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01135/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01135.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01143/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01143.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01144/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01144.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01145/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01145.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01147/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01147.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01148/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01148.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01149/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01149.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01150/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01150.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01156/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01156.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01157/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01157.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01160/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01160.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01161/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01161.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01162/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01162.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01163/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01163.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01164/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01164.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01165/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01165.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01169/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01169.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01171/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01171.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01172/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01172.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01174/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01174.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01200/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01200.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01201/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01201.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01202/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01202.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01207/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01207.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01208/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01208.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01209/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01209.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01210/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01210.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01211/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01211.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01213/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01213.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01215/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01215.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01216/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01216.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01225/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01225.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01226/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01226.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01228/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01228.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01230/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01230.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01232/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01232.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01234/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01234.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01235/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01235.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01236/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01236.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01237/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01237.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01239/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01239.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01240/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01240.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01245/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01245.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01248/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01248.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01262/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01262.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01263/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01263.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01265/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01265.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01266/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01266.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01273/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01273.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01274/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01274.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01275/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01275.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01276/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01276.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01277/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01277.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01278/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01278.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01286/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01286.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01288/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01288.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01289/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01289.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01291/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01291.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01293/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01293.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01295/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01295.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01296/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01296.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01308/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01308.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01316/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01316.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01322/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01322.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01325/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01325.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01326/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01326.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01327/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01327.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01329/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01329.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01332/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01332.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01333/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01333.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01334/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01334.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01336/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01336.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01413/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01413.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01418/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01418.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01518/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01518.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01522/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01522.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01524/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01524.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01525/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01525.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01533/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01533.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01540/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01540.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01540/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01540.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01540/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01540.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01540/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01540.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01540/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01540.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01541/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01541.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01541/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01541.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01541/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01541.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01541/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01541.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01541/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01541.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01542/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01542.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01544/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01544.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01544/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01544.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01544/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01544.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01544/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01544.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01544/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01544.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01546/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01546.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01547/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01547.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01549/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01549.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01550/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01550.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01550/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01550.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01550/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01550.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01550/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01550.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01550/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01550.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01551/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01551.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01551/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01551.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01551/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01551.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01551/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01551.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01551/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01551.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01554/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01554.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01703/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01703.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01703/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01703.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01703/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01703.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01703/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01703.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01703/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01703.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01704/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01704.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01704/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01704.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01704/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01704.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01704/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01704.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01704/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01704.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01707/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01707.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01707/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01707.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01707/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01707.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01707/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01707.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01707/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01707.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01716/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01716.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01716/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01716.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01716/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01716.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01716/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01716.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01716/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01716.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01720/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01720.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01720/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01720.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01720/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01720.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01720/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01720.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01720/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01720.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01726/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01726.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01726/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01726.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01726/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01726.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01726/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01726.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01726/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01726.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01729/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01729.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01729/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01729.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01729/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01729.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01729/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01729.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01729/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01729.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01730/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01730.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01731/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01731.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01731/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01731.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01731/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01731.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01731/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01731.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01731/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01731.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01736/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01736.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01736/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01736.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01736/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01736.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01736/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01736.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01736/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01736.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01737/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01737.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01737/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01737.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01737/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01737.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01737/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01737.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01737/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01737.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01739/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01739.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01767/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01767.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01767/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01767.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01767/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01767.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01767/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01767.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01767/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01767.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01770/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01770.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01770/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01770.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01770/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01770.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01770/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01770.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01770/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01770.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01772/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01772.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01772/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01772.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01772/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01772.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01772/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01772.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01772/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01772.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01777/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01777.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01777/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01777.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01777/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01777.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01777/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01777.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01777/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01777.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01778/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01778.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01778/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01778.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01778/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01778.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01778/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01778.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01778/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01778.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01788/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01788.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01788/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01788.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01788/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01788.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01788/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01788.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01788/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01788.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01789/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01789.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01789/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01789.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01789/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01789.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01789/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01789.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01789/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01789.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01793/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01793.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01794/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01794.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01796/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01796.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01797/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01797.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01797/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01797.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01797/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01797.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01797/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01797.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01797/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01797.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01799/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01799.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01799/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01799.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01799/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01799.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01799/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01799.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01799/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01799.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01800/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01800.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01800/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01800.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01800/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01800.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01800/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01800.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01800/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01800.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01802/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01802.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01802/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01802.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01802/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01802.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01802/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01802.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01802/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01802.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01803/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01803.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01804/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01804.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01806/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01806.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01807/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01807.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01807/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01807.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01807/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01807.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01807/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01807.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01807/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01807.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01808/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01808.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01808/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01808.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01808/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01808.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01808/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01808.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01808/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01808.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01809/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01809.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01810/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01810.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01811/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01811.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01812/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01812.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01812/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01812.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01812/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01812.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01812/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01812.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01812/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01812.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01814/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01814.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01814/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01814.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01814/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01814.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01814/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01814.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01814/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01814.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01817/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01817.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01817/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01817.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01817/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01817.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01817/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01817.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01817/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01817.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01818/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01818.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01818/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01818.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01818/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01818.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01818/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01818.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01818/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01818.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01820/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01820.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01822/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01822.HLT0.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01826/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01826.HLT1.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01826/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01826.HLT2.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01826/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01826.HLT3.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01826/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01826.HLT4.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01826/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01826.HLT5.hlt_hadron.root',
'/ghi/fs01/belle2/bdata/Data/e0008/4S/Unofficial/release-03-01-02/DB00000607/r01827/skim/hlt_hadron/cdst/sub00/cdst.physics.0008.01827.HLT0.hlt_hadron.root',
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

ma.cutAndCopyList("pi+:rec", "pi+:all", "charge>0",path=mypath)
ma.cutAndCopyList("pi-:rec", "pi+:all", "charge<0",path=mypath)
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

ma.cutAndCopyList("K+:pos","K+:all", "charge > 0", path=mypath)

# Fit the B0 Vertex
ma.reconstructDecay("B0:recgen -> psi(2S):gen K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recden -> psi(2S):den K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recjpsi -> psi(2S):jpsi K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)
ma.reconstructDecay("B0:recjpsiden -> psi(2S):jpsiden K_S0:rec",cut="Mbc > 5.2 and abs(deltaE)<0.15",path=mypath)

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
rootOutputFile = "B0Bp_realdat_bucket6_unofficial.root"

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
