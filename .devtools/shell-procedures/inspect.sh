#!/usr/bin/env bash
echo "### REPO_MANAGEMENT :: inspect :: begins ###"

PROC_PATH=$(dirname "$0")
source $PROC_PATH/helper.sh
source $PROC_PATH/printer_commit.sh



synchronize_it() {
  gh repo sync rattish/$1 -b origin/main
  git pull
}
publish_it() {
  $PROC_PATH/publish.sh $1 $2
}
repo_check() {
  cd "../$1"
  git fetch --all
  git submodule sync
  git submodule update
}



inspect_repo(){
  repo_check $1
  V_DIIFFRENCE=$(awk "BEGIN { local=$(version_local); remote=$(version_remote); print (local-remote) }")
  if [ $V_DIIFFRENCE -lt 0 ]; then ## pull from remote

    synchronize_it $1

  elif [ $V_DIIFFRENCE -gt $(($RANDOM%10+10)) ]; then  ## need to be updated

    publish_it $1 $2

  fi
  #
  if [ $(git status -s | wc -l) -ne 0 ] ; then  ## unstaged need to be done
    git add *
    git add .devtools/*
    git commit -m "$(_PRINT_COMMIT_MESSAGE $1)"
  fi
}

inspect_repo $1 $2


#for (( i=0; i<=$#; i++ )); do
  #echo "$#" "$i" "${!i}"
#  devtools_check inspect "${!i}"
#  project_check inspect

#done


#sync_repo ratman-dataedit
#sync_repo documentation-builder
#sync_repo branching-chainer
#sync_repo rattish

echo "### REPO_MANAGEMENT :: inspect :: ends ###"
