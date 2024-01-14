#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
source $PROC_PATH/functions.sh
source $PROC_PATH/printer_pullrequest.sh



upload() {
  cd ../$1
  $PROC_PATH/sync_devtools.sh
  if [ $UPDATE_CHECK_LOCAL -ge $UPDATE_CHECK_REMOTE ]; then
    sync_project $1
    git push
  fi
}


#update_and_upload_repo rattiish



update_and_upload_repo() {
  cd ../$1



  PULL_REQUEST_CONTENT=$(git diff main remotes/origin/main --shortstat)

  git diff main origin/main --numstat
  gh pr create --title "$(get_update_title $1)" --body "$(get_pullrequest_body)"
}
