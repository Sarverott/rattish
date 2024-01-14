#!/usr/bin/env bash

GIT_CURRENT_USER=$(gh api user -q ".login")

PROC_PATH=$(dirname "$0")

version_local(){
  git rev-list --count $(git branch --show-current)
}
version_remote(){
  git rev-list --count origin/main
}
forkname() {
  #echo "rattish-devtools-$1"
  echo "$1"
}
