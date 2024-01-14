#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
source $PROC_PATH/functions.sh
source $PROC_PATH/printer_pullrequest.sh



upload() {
  cd ../$1
  $PROC_PATH/sync_devtools.sh
  if [ $(version_local) -ge $(version_remote) ]; then
    git push
    gh pr create --title "$(_PRINT_TITLE $1)" --body "$(_PRINT_BODY $1)"
  fi
}


#update_and_upload_repo rattiish

upload $1

#git diff main origin/main --numstat
