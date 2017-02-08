#!/usr/bin/python
import sys
for line in sys.stdin:
        # Setting some defaults
        line = line.strip()
        splits = line.split("\t")
        splits = list(map(int,splits))
        splits.sort()
        print ('%s\t%s\t%s' %(splits[0], splits[1], splits[2]))