if $(basename $PWD) == "dev" ; then
  cd ..
fi
git add docs/*
#git add src/*
git add README.md
git commit -m "decumentation regenerated at $(date +%s)s since epoch"
