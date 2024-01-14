#!/usr/bin/env bash

pwd

git submodule add -b main -f "$1" "$2"

exit 0
