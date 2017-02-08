#!/usr/bin/python
import sys
prev = [-1, -1]
entries = []
for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    splits = list(map(int, splits))
    if( splits[0] == prev[0] and splits[1] == prev[1] ):
	    entries.append( splits[2] )
    else:
        if( -1 in entries):
	        # Exists case
	        entries.remove(-1)
	        entries.sort()
	        for e in entries:
	            temp = [prev[0], prev[1], e]
	            temp.sort()
	            print("%s\t%s\t%s" %(temp[0], temp[1], temp[2]))

        prev = [ splits[0], splits[1] ]
        entries = [ splits[2] ]