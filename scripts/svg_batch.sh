#! /bin/bash

book_root=./Intro_to_CS

for f in `find ${book_root} -name \*.svg -print`; do
  stem=`basename $f .svg`
  dir=`dirname $f`
  png="${dir}/${stem}.png"
  echo "$f => $dir $stem  =>  $png"
  rsvg-convert -o $png -f png $f
done;