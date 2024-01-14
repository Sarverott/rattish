#!/usr/bin/env bash

echo "### REPO_MANAGEMENT :: open :: begins ###"

PROC_PATH=$(dirname "$0")
source $PROC_PATH/helper.sh


EDITOR=$1

shift 1

$PROC_PATH/init.sh documentation-builder ratman-dataedit branching-chainer

$PROC_PATH/inspect.sh documentation-builder
$PROC_PATH/inspect.sh ratman-dataedit
$PROC_PATH/inspect.sh branching-chainer
$PROC_PATH/inspect.sh rattish

$EDITOR --foreground --no-sandbox . ../documentation-builder ../ratman-dataedit ../branching-chainer


$PROC_PATH/publish.sh documentation-builder
$PROC_PATH/publish.sh ratman-dataedit
$PROC_PATH/publish.sh branching-chainer
$PROC_PATH/publish.sh rattish

echo "### REPO_MANAGEMENT :: open :: ends ###"
