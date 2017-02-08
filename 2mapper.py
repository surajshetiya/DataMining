#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    splits = list(map(int,splits))
    splits.sort()
    print('%s\t%s' % (splits[0],splits[1]))