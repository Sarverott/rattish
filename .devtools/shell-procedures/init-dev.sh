#!/usr/bin/env bash

source $(dirname "$0")/functions.sh


cd ..

devtool_fork_and_clone documentation-builder
devtool_fork_and_clone branching-chainer
devtool_fork_and_clone ratman-dataedit

cd rattish
