#!/usr/bin/env bash

GIT_CURRENT_USER=$(gh api user -q ".login")

devtool_fork_and_clone() {
  gh repo fork "rattish/$1" --clone=true
  #git clone "https://github.com/$GIT_CURRENT_USER/rattish-devtools-$1.git"
}

sync_repo() {
  cd ../$1
  git fetch --all
  git pull
  git submodule sync
  git submodule update
}

get_update_body() {
  echo "current version: $(git rev-list --count $(git branch --show-current))"
  echo "remote version: $(git rev-list --count origin/main)"
}

get_update_title() {
  echo "$GIT_CURRENT_USER@$1->PULL_REQUEST : version $2 = $(date +%s)"
}

update_and_upload_repo() {

  UPDATE_CHECK_LOCAL=$(git rev-list --count $(git branch --show-current))
  UPDATE_CHECK_REMOTE=$(git rev-list --count origin/main)

  if [[ ! $UPDATE_CHECK_LOCAL == $UPDATE_CHECK_REMOTE ]]; then
    sync_repo $1

  fi

  cd ../$1
  git add *
  git commit -m
  git push

  PULL_REQUEST_CONTENT=$(git diff main remotes/origin/main --shortstat)

  git diff main remotes/origin/main --numstat
  gh pr create --title "$GIT_CURRENT_USER@$1 : autoupdating $1 = $(date +%s)" --body " \n "
}
