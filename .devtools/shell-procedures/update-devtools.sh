#!/usr/bin/env bash

source $(dirname "$0")/functions.sh


update_and_upload_repo ratman-dataedit
update_and_upload_repo documentation-builder
update_and_upload_repo branching-chainer

cd ../rattish
#update_and_upload_repo rattiish
