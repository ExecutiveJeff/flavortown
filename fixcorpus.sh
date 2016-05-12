#!/bin/bash

grep -E -v '^-' flavortown.txt > flavorprep.txt
cat flavorprep.txt | sed 's/^/BEGIN NOW /' > flavorprep2.txt
cat flavorprep2.txt | sed 's/$/ END/' > flavordone.txt
