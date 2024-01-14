#!/usr/bin/env bash

source $(dirname "$0")/functions.sh

get_update_title() {
  echo "$GIT_CURRENT_USER@$1::CommitUpdate[ $2 ] = $(date +%s)"
}
commit_if_updated() {
  if [ $(git status -s | wc -l) -ne 0 ] ; then
    UPDATE_CHECK_LOCAL=$(git rev-list --count $(git branch --show-current))
    git add *
    git commit -m "$(get_update_title $1 $UPDATE_CHECK_LOCAL)"
  fi
}



cd ../rattish
#update_and_upload_repo rattiish
