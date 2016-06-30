sed -e :1 -e 's/\([.?!]\)[[:blank:]]\{1,\}\([^[:blank:]]\)/\1\
\2/;t1' $1 > dummy.txt
sed '/^$/d' dummy.txt > clean.txt
grep -E -v '^-' clean.txt > prep.txt
cat prep.txt | sed 's/^/BEGIN NOW /' > prep2.txt
cat prep2.txt | sed 's/$/ END/' > finish.txt
rm prep.txt && rm prep2.txt && rm dummy.txt && rm clean.txt
python pickletown
