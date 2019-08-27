#!/bin/bash

counter=0

#rname_map=(/home/thczank/b0psi2sks/gsim/psi2see/b0_psi2s_gsim_psi2see_all.root
#/home/thczank/b0psi2sks/gsim/psi2sjpsiee/b0_psi2s_gsim_psi2sjpsiee_all.root)

rname_map=(/home/thczank/b0psi2sks/gsim/psi2sjpsimumu/b0_psi2s_gsim_psi2sjpsimumu_all.root
/home/thczank/b0psi2sks/gsim/psi2smumu/b0_psi2s_gsim_psi2smumu_all.root
)


for namap in "${rname_map[@]}";do
       export FILENAME=${namap}
       export OUTPUT='b0bp_psi2s_'${counter}'_MC.root'
       basf2 ./B0_psi2s_yusamod_MC.py 
counter=$((counter+1))
done


