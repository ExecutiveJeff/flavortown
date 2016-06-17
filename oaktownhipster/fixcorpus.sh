#!/bin/bash

grep -E -v '^-' $1 > prep.txt
cat prep.txt | sed 's/^/BEGIN NOW /' > prep2.txt
cat prep2.txt | sed 's/$/ END/' > finish.txt
rm prep.txt && rm prep2.txt
