#!/usr/bin/python
import sys
from sys import argv


with open(sys.argv[1], 'r') as f:
    for l in f:
        print l, len(l)
