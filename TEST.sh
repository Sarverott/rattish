#for dir in /_old_*/     # list directories in the form "/tmp/dirname/"
#do
    #echo $dir
    #dir=${dir%*/}      # remove the trailing "/"
    #echo $dir
    #echo "${dir##*/}"    # print everything after the final "/"
#done
