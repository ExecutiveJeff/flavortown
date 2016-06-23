tr  '.' '\n' < $1 > dummy.txt
sed '/^$/d' dummy.txt > dumb.txt
sed 's/$/./' dumb.txt > clean.txt
rm dummy.txt && rm dumb.txt
