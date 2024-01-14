#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
source $PROC_PATH/functions.sh


_PRINT_TITLE() {
  echo "PullRequest[ rattish@REMOTE_$(version_remote) <<< $GIT_CURRENT_USER@LOCAL_$(version_local) ]"
}

_PRINT_PATCH_RAPORT() {
  echo "###### ${1::-6}"
  echo "\`\`\`"
  cat $1 | grep -e "@@" -e "+++" -e "---"
  rm $1
  echo "\`\`\`"
  echo ""
}

_PRINT_LOG_STATUS() {
  if [ ! $(git diff main origin/main --name-status | grep "^$2" -c) == "0" ] ; then
    echo " - **$1** :"
    git diff main origin/main --diff-algorithm=histogram --name-status | grep "^$2" --label="   - "
  else
    echo " - ~$1~ :"
  fi
}

_PRINT_PULLREQUEST_BODY() {
  echo "# PULL REQUEST CONTENT - $1"
  echo "from [$(git config user.name)](https://github.com/$GIT_CURRENT_USER) <$(git config user.email)>"
  echo "> date: $(date --rfc-email)"
  echo "---"
  echo "#### VERSION"
  echo "> \`[ $GIT_CURRENT_USER@$(version_local) === ROOT::$(version_remote)  ]\`"
  echo "---"
  echo "### RAPORT"

  git diff main origin/main
  _PRINT_LOG_STATUS Added A
  _PRINT_LOG_STATUS Copied C
  _PRINT_LOG_STATUS Deleted D
  _PRINT_LOG_STATUS Modified M
  _PRINT_LOG_STATUS Renamed R
  _PRINT_LOG_STATUS Type_change T
  _PRINT_LOG_STATUS UNMERGED U
  _PRINT_LOG_STATUS UNKNOWN X
  _PRINT_LOG_STATUS BROKEN B
  echo "### PATCHES"
  echo ""
  find . -maxdepth 1 -mindepth 1 -name "*-*.patch" -type f --exec _PRINT_PATCH_RAPORT {} \;
  echo "---"
  echo ""
  cat LICENSE | head -3 | tail -1
}
