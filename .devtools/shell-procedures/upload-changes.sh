#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
source $PROC_PATH/functions.sh



pr_title() {
  echo "PullRequest[ rattish@REMOTE_$(version_remote) >>> $GIT_CURRENT_USER@LOCAL_$(version_local) ]"
}

pr_patch_raport() {
  echo "###### ${1::-6}"
  echo "\`\`\`"
  cat $1 | grep -e "@@" -e "+++" -e "---"
  rm $1
  echo "\`\`\`"
  echo ""
}

pr_echo_status() {
  if [ ! $(git diff main origin/main --name-status | grep "^$2" -c) == "0" ] ; then
    echo " - **$1** :"
    git diff main origin/main --diff-algorithm=histogram --name-status | grep "^$2" --label="   - "
  else
    echo " - ~$1~ :"
  fi
}

pr_body() {
  echo "# PULL REQUEST CONTENT - $1"
  echo "from [$(git config user.name)](https://github.com/$GIT_CURRENT_USER) <$(git config user.email)>"
  echo "> date: $(date --rfc-email)"
  echo "---"
  echo "#### VERSION"
  echo "> \`[ $GIT_CURRENT_USER@$UPDATE_CHECK_LOCAL === ROOT::$UPDATE_CHECK_REMOTE ]\`"
  echo "---"
  echo "### RAPORT"

  git diff main origin/main
  pr_echo_status Added A
  pr_echo_status Copied C
  pr_echo_status Deleted D
  pr_echo_status Modified M
  pr_echo_status Renamed R
  pr_echo_status Type_change T
  pr_echo_status UNMERGED U
  pr_echo_status UNKNOWN X
  pr_echo_status BROKEN B
  echo "### PATCHES"
  echo ""
  find . -maxdepth 1 -mindepth 1 -name "*-*.patch" -type f --exec pr_patch_raport {} \;
  echo "---"
  echo ""
}

upload() {
  cd ../$1
  $PROC_PATH/sync_devtools.sh
  if [ $UPDATE_CHECK_LOCAL -ge $UPDATE_CHECK_REMOTE ]; then
    sync_project $1
    git push
  fi
}


#update_and_upload_repo rattiish



update_and_upload_repo() {
  cd ../$1



  PULL_REQUEST_CONTENT=$(git diff main remotes/origin/main --shortstat)

  git diff main origin/main --numstat
  gh pr create --title "$(get_update_title $1)" --body "$(get_pullrequest_body)"
}
