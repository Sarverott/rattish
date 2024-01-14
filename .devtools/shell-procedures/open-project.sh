#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
EDITOR=$1

shift 1

$PROC_PATH/init-dev.sh $@

$PROC_PATH/sync-devtools.sh $@ rattish

$EDITOR --foreground --no-sandbox . $@

$PROC_PATH/update-project.sh $@ rattish
