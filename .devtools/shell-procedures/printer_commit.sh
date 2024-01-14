#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
source $PROC_PATH/helper.sh


_PRINT_COMMIT_MESSAGE() {
  echo "$GIT_CURRENT_USER@$1::CommitUpdate[ No. $(version_local) ]"
}
