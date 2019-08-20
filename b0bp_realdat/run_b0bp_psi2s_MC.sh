#!/bin/bash

counter=0

rname_map=(
)


for namap in "${rname_map[@]}";do
       export FILENAME=${namap}
       export OUTPUT='b0bp_psi2s_'${counter}'_MC.root'
       basf2 ./B0_psi2s_yusamod_MC.py -p4 -n 10000
counter=$((counter+1))
done


