#!/usr/bin/env bash

pwd

git submodule add https://github.com/rattish/ratman-dataedit.git ./.devtools/data-editor
git submodule add https://github.com/rattish/ratman-docbuilder.git ./.devtools/doc-build
git submodule add https://github.com/rattish/rattlesnake.git ./.devtools/interface
git submodule add https://github.com/rattish/repochainer.git ./.devtools/repochainer

exit 0
