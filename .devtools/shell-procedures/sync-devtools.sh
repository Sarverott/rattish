#!/usr/bin/env bash

source $(dirname "$0")/functions.sh

for (( i=0; i<=$#; i++ )); do
  #echo "$#" "$i" "${!i}"
  confront_states "${!i}"
  
done


#sync_repo ratman-dataedit
#sync_repo documentation-builder
#sync_repo branching-chainer
#sync_repo rattish
