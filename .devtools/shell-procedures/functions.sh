#!/usr/bin/env bash

GIT_CURRENT_USER=$(gh api user -q ".login")

forkname() {
  echo "rattish-devtools-$1"
}

devtools_check(){
  cd "../$(forkname $1)h"
  git fetch --all
  git submodule sync
  git submodule update
  if [ $1 == "sync" ] ; then
    git pull
    gh repo sync rattish/$1 -b origin/main
    git pull
  fi
}

project_check() {
  cd "../rattish"
  git fetch --all
  git submodule sync
  git submodule update
  if [ $1 == "sync" ] ; then
    git pull
    gh repo sync rattish/rattish -b origin/main
    git pull
  fi
}

update_and_upload_repo() {

  cd ../$1

  UPDATE_CHECK_LOCAL=$(git rev-list --count $(git branch --show-current))
  UPDATE_CHECK_REMOTE=$(git rev-list --count origin/main)

  if [ $UPDATE_CHECK_LOCAL -ge $UPDATE_CHECK_REMOTE ]; then
    sync_repo $1


  fi

  PULL_REQUEST_CONTENT=$(git diff main remotes/origin/main --shortstat)

  git diff main remotes/origin/main --numstat
  gh pr create --title "$(get_update_title $1 $UPDATE_CHECK_LOCAL)" --body ""
}
