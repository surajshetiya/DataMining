#!/usr/bin/python
import sys
# T - threshold
T = 1000
last = [-1, -1 ,0]
for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    splits = list(map(int, splits))
    if(splits[0] == last[0] and splits[1] == last[1]):
	    last[2] += 1
    else:
        if( last[2] >= T):
            print("%s\t%s" % (last[0],last[1]))
        last = splits