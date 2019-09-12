#!/bin/bash

rname_map=(/home/thczank/b0psi2sks/gsim/B0/psi2see/b0_psi2s_gsim_psi2see_all
/home/thczank/b0psi2sks/gsim/B0/psi2sjpsiee/b0_psi2s_gsim_psi2sjpsiee_all
/home/thczank/b0psi2sks/gsim/B0/psi2sjpsimumu/b0_psi2s_gsim_psi2sjpsimumu_all
/home/thczank/b0psi2sks/gsim/B0/psi2smumu/b0_psi2s_gsim_psi2smumu_all
/home/thczank/b0psi2sks/gsim/Bp/psi2smumu/bppsi2smumu_gsim_all
/home/thczank/b0psi2sks/gsim/Bp/psi2see/bppsi2see_gsim_all
/home/thczank/b0psi2sks/gsim/Bp/psi2sjpsiee/bppsi2sjpsiee_gsim_all
/home/thczank/b0psi2sks/gsim/Bp/psi2sjpsimumu/bppsi2sjpsimumu_gsim_all
          )


for namap in "${rname_map[@]}";do
       export FILENAME=${namap}'.root'
       export OUTPUT=${namap}'_MC_iptube.root'
       basf2 ./B0_psi2s_yusamod_MC.py -p4
done


