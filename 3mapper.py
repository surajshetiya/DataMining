#!/usr/bin/python
import sys
for line in sys.stdin:
	line = line.strip()
	splits = line.split("\t")
	splits = list(map(int, splits))
	splits.sort(reverse=True)
	if( len(splits) == 2):
	    print("%s\t%s\t%s" % (splits[0],splits[1],-1))
	else:
	    print("%s\t%s\t%s"% (splits[0],splits[1],splits[2]))