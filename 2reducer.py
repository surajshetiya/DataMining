#!/usr/bin/python
import sys
arr = []
prev = -1
for line in sys.stdin:
        line = line.strip()
        splits = line.split("\t")
        splits = list(map(int,splits))
        if(splits[0] == prev):
            for item in arr:
                if(item < splits[1]):
                    print ('%s\t%s\t%s' %(prev, item, splits[1]))
                else:
                    print ('%s\t%s\t%s' %(prev, splits[1], item))
            arr.append(splits[1])
            index = len(arr)-1
            while(index>0):
                if(arr[index]<arr[index-1]):
                    t = arr[index]
                    arr[index] = arr[index-1]
                    arr[index-1] = t
                else:
                    break
                index -= 1
        else:
            arr = [splits[1]]
            prev = splits[0]