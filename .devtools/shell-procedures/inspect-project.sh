#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
source $PROC_PATH/functions.sh



repo_check() {
  cd "../$1"
  git fetch --all
  git submodule sync
  git submodule update
}
update_title() {
  echo "$GIT_CURRENT_USER@$1::CommitUpdate[ No. $(version_local) ]"
}
inspect_repo(){
  repo_check $1
  V_DIIFFRENCE=$(awk "BEGIN { local=$(version_local); remote=$(version_remote); print (local-remote) }")
  if [ $V_DIIFFRENCE -lt 0 ]; then ## pull from remote
    gh repo sync rattish/$2 -b origin/main
    git pull
  elif [ $V_DIIFFRENCE -gt $(($RANDOM%10+10)) ]; then  ## need to be updated
    $PROC_PATH/upload-changes.sh $1
  fi
  #
  if [ $(git status -s | wc -l) -ne 0 ] ; then  ## unstaged need to be done
    git add *
    git commit -m "$(update_title $1)"
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
