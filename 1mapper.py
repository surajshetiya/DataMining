#!/usr/bin/python
import sys
for line in sys.stdin:
	line = line.strip()
	splits = line.split(" ")
	splits = list(map(int, splits))
	splits.sort()
	for index in range(len(splits)):
		for index1 in range(index+1, len(splits)):
			print ("%s\t%s\t1" % (splits[index],splits[index1]))