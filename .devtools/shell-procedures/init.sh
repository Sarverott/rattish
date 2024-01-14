#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
source $PROC_PATH/helper.sh

submods_fork_and_clone() {
  gh repo fork "rattish/$1" --clone=true --remote-name "$(forkname $1)"
  #git clone "https://github.com/$GIT_CURRENT_USER/rattish-devtools-$1.git"
}
api_call_for_status(){
  curl "https://api.github.com/repos/$GIT_CURRENT_USER/$(forkname $1)" -I | grep "^HTTP\/"
}
fork_if_not_exist() {
  IFS=' '
  API_CALL_STATUS=$(api_call_for_status $1)
  read -a RESULT_HTTP_CODE <<< "$API_CALL_STATUS"
  if [ "${RESULT_HTTP_CODE[1]}" == "404" ] ; then
    devtool_fork_and_clone $1 $2
  elif [ ! -e "../$(forkname $1)" -a  "${RESULT_HTTP_CODE[1]}" == "200"  ]; then
    gh repo clone $GIT_CURRENT_USER/$(forkname $1).git
  else
    echo "ERROR! exits on <fork_if_not_exist()> ..."
    exit 500
  fi
}

echo "### REPO_MANAGEMENT :: init :: begins ###"

cd ..

for (( i=0; i<=$#; i++ )); do
  #echo "$#" "$i" "${!i}"
  fork_if_not_exist "${!i}"

done

#devtool_fork_and_clone documentation-builder
#devtool_fork_and_clone branching-chainer
#devtool_fork_and_clone ratman-dataedit

cd rattish

echo "### REPO_MANAGEMENT :: init :: ends ###"
