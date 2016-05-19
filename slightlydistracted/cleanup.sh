#!/bin/sh
files="*.txt"
for i in $files
do
  sed '/^$/d' $i > $i.out
  sed -e 's/^[ \t]*//' $i.out > $i.more
  sed -e 's/nnn */ /g' $i.more > $i.fix
  mv  $i.fix $i
  rm $i.more && rm $i.out
done
