#! /usr/bin/python

import numpy as N
from itertools import count

listSquares = set(N.arange(1,10**6)**2)

def f(x):
	return sum( int(y)**2 for y in str(x) )
theSum = 0
for i in count(1,10**20):
	if f(i) in listSquares:
		theSum += i

print theSum % 10**9

