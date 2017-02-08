#!/usr/bin/python
import sys
filename = "op3"
individual = dict()
items = []
with open(filename) as f:
    for line in f:
        line = line.strip()
        splits = line.split("\t")
        splits = list(map(int, splits))
        splits.sort()
        items.append(splits)
        for s in splits:
            individual[s] = 1

curEntries = []
for line in sys.stdin:
    line = line.strip()
    splits = line.split(" ")
    splits = list(map(int, splits))
    for entry in splits:
	    if( entry in individual ):
	        curEntries.append(entry)

    for index1 in range(len(curEntries)):
        for index2 in range(index1+1,len(curEntries)):
            for index3 in range(index2+1,len(curEntries)):
                item = [curEntries[index1], curEntries[index2], curEntries[index3]]
                item.sort()
                if( item in items ):
                    print("%s\t%s\t%s\t1" % (item[0],item[1],item[2]))
    curEntries = []
