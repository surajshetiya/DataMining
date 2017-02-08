#!/usr/bin/python
import sys
prev = [-1, -1, -1]
count = 0
# T - threshold
T = 1000
for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    splits = list(map(int, splits))
    if(prev[0] == splits[0] and prev[1] == splits[1] and prev[2] == splits[2]):
        count += splits[3]
        if(count == T):
            print("%s\t%s\t%s" %(prev[0],prev[1],prev[2]))

    else:
        prev = splits[0:3]
        count = 0