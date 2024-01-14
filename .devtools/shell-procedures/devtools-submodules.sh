#!/usr/bin/env bash

pwd

git submodule add -b main -f https://github.com/rattish/ratman-dataedit.git ./.devtools/data-edit
git submodule add -b main -f https://github.com/rattish/documentation-builder.git ./.devtools/doc-build
#git submodule add https://github.com/rattish/rattlesnake.git ./.devtools/interface
git submodule add -b main -f https://github.com/rattish/branching-chainer.git ./.devtools/repochainer

exit 0
