#!/usr/bin/env bash

echo "### REPO_MANAGEMENT :: publish :: begins ###"

PROC_PATH=$(dirname "$0")
source $PROC_PATH/helper.sh
source $PROC_PATH/printer_pullrequest.sh


upload() {
  cd ../$1
  if [ $(version_local) -ge $(version_remote) ] ; then
    if [ $2 == "upload" ] ; then
      gh repo sync rattish/$1 -b origin/main
      git pull
      git push
      gh pr create --title "$(_PRINT_TITLE $1)" --body "$(_PRINT_BODY $1)"
    elif [ $2 == "release" ] ; then
      gh repo sync rattish/$1 -b origin/main
      git pull
      git push
      gh release create v1.2.3 --generate-notes
    fi
  fi
}

#update_and_upload_repo rattiish

upload $1 $2

#git diff main origin/main --numstat

echo "### REPO_MANAGEMENT :: publish :: ends ###"
