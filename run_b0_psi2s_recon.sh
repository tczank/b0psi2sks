#!/bin/bash

number_map=(0 1 2 3 4 5 6 7 8 9)

name_map=(psimumu psiee psijpsimumu psijpsiee)

for namap in "${name_map[@]}";do
    for numap in "${number_map[@]}";do
        basf2 ./shou_b0_psi2s_gsim_recon.py -p16 <<EOF
        /home/thczank/b0psi2sks/evtgen/${namap}/b0_psi2s_evtgen_${namap}_${numap}.root
        b0_psi2s_gsim_${namap}_${numap}.root
EOF
    done
done


