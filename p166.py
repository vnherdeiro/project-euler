#! /usr/bin/python3

from collections import defaultdict


d = defaultdict( int)

for x in range(10):
	for y in range(10):
		for z in range(10):
			for t in range(10):
				d[ x+y+z+t] += 1

for x,y in d.items():
	print (x, y)

d2 = defaultdict( list)
for x in range(10):
	for y in range(10):
		for z in range(10):
			for t in range(10):
				d2[ x+y+z+t].append( (x,y,z,t))

#print (d2)
