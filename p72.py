#!/usr/bin/python

from sys import argv
from fractions import gcd

maxD = int(argv[1])

theSum = 0
for d in xrange(2,maxD+1):
	for n in xrange(1,d):
		if gcd(n,d) == 1:
			theSum += 1

print theSum

#too slow -- done summing the Euler totem function
