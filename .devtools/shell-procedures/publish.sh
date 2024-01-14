#!/usr/bin/env bash

echo "### REPO_MANAGEMENT :: publish :: begins ###"

PROC_PATH=$(dirname "$0")
source $PROC_PATH/helper.sh
source $PROC_PATH/printer_pullrequest.sh


upload() {
  cd ../$1
  if [ $(version_local) -ge $(version_remote) ] ; then
    if [ $2 == "upload" ] ; then
      git push
      gh pr create --title "$(_PRINT_TITLE $1)" --body "$(_PRINT_BODY $1)"
    else

    fi
  fi
}

#update_and_upload_repo rattiish

upload $1 "upload"

#git diff main origin/main --numstat

echo "### REPO_MANAGEMENT :: publish :: ends ###"
