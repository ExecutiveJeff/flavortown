#!/bin/bash

grep -E -v '^-' output.txt > flavorprep.txt
cat flavorprep.txt | sed 's/^/BEGIN NOW /' > flavorprep2.txt
cat flavorprep2.txt | sed 's/$/ END/' > outdone.txt
rm flavorprep.txt && rm flavorprep2.txt
