#!/usr/bin/env bash

source $(dirname "$0")/functions.sh

get_update_body() {
  echo "uploaded version: $(git rev-list --count $(git branch --show-current))"
  echo "remote version: $(git rev-list --count origin/main)"
}

update_and_upload_repo branching-chainer

cd ../rattish
#update_and_upload_repo rattiish



update_and_upload_repo() {

  cd ../$1

  UPDATE_CHECK_LOCAL=$(git rev-list --count $(git branch --show-current))
  UPDATE_CHECK_REMOTE=$(git rev-list --count origin/main)

  if [ $UPDATE_CHECK_LOCAL -ge $UPDATE_CHECK_REMOTE ]; then
    sync_project $1
    git push

  fi

  PULL_REQUEST_CONTENT=$(git diff main remotes/origin/main --shortstat)

  git diff main remotes/origin/main --numstat
  gh pr create --title "$(get_update_title $1 $UPDATE_CHECK_LOCAL)" --body ""
}
