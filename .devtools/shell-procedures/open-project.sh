#!/usr/bin/env bash

PROC_PATH=$(dirname "$0")
source $PROC_PATH/functions.sh


EDITOR=$1

shift 1

$PROC_PATH/init-dev.sh documentation-builder ratman-dataedit branching-chainer

$PROC_PATH/inspect-project.sh documentation-builder
$PROC_PATH/inspect-project.sh ratman-dataedit
$PROC_PATH/inspect-project.sh branching-chainer
$PROC_PATH/inspect-project.sh rattish

$EDITOR --foreground --no-sandbox . ../documentation-builder ../ratman-dataedit ../branching-chainer

$PROC_PATH/upload-changes.sh documentation-builder ratman-dataedit branching-chainer rattish
