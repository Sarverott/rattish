#!/usr/bin/env bash

echo "### REPO_MANAGEMENT :: open :: begins ###"

PROC_PATH=$(dirname "$0")
source $PROC_PATH/helper.sh


EDITOR=$1

shift 1

$PROC_PATH/init.sh documentation-builder ratman-dataedit branching-chainer

$PROC_PATH/submodule-reload.sh https://github.com/rattish/ratman-dataedit.git ./.devtools/data-edit
$PROC_PATH/submodule-reload.sh https://github.com/rattish/documentation-builder.git ./.doc-build/data-edit
$PROC_PATH/submodule-reload.sh https://github.com/rattish/branching-chainer.git ./.devtools/repochainer

$PROC_PATH/inspect.sh documentation-builder upload
$PROC_PATH/inspect.sh ratman-dataedit upload
$PROC_PATH/inspect.sh branching-chainer upload
$PROC_PATH/inspect.sh rattish release

$EDITOR --foreground --no-sandbox . ../documentation-builder ../ratman-dataedit ../branching-chainer


$PROC_PATH/publish.sh documentation-builder upload
$PROC_PATH/publish.sh ratman-dataedit upload
$PROC_PATH/publish.sh branching-chainer upload
$PROC_PATH/publish.sh rattish release

echo "### REPO_MANAGEMENT :: open :: ends ###"
