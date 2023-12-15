if $(basename $PWD) == "build" ; then
  cd ..
fi
git add command-list/*
git add examples/*
git add README.md
git commit -m "decumentation regenerated at $(date +%s)s since epoch"
