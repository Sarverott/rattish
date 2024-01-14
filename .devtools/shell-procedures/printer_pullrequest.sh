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

_PRINT_SECTION_TITLE() {
  printf "\n---\n\n### ${1^^}\n"
}

_PRINT_BODY() {
  echo "# PULL REQUEST LOG - $1"
  echo "from [$(git config user.name)](https://github.com/$GIT_CURRENT_USER) <$(git config user.email)>"
  echo "> date: $(date --rfc-email)"

  _PRINT_SECTION_TITLE "version"

  echo "> \`[ $GIT_CURRENT_USER@$(version_local) === ROOT::$(version_remote)  ]\`"

  _PRINT_SECTION_TITLE "status"

  git diff main origin/main --stat

  _PRINT_SECTION_TITLE "result list"

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

  _PRINT_SECTION_TITLE "patches"

  find . -maxdepth 1 -mindepth 1 -name "*-*.patch" -type f --exec _PRINT_PATCH_RAPORT {} \;

  _PRINT_SECTION_TITLE "submodules"

  git submodule status | grep --label="   - "
  printf "\n\n---\n\n"
  cat LICENSE | head -3 | tail -1
  printf "\n\n---\n\n"
  printf "# END-OF-PULL-REQUEST-LOG"
}
