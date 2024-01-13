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

update_and_upload_repo() {
  cd ../$1
  git add *
  read COMMIT_INFO
  git commit -m "$GIT_CURRENT_USER@$1 : autoupdating-devtools = $(date +%s)"
  git push
  gh pr create --title "$GIT_CURRENT_USER@$1 : autoupdating-devtools = $(date +%s)" --body "$GIT_CURRENT_USER@$1 : autoupdating-devtools = $(date +%s)"
}
