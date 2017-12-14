#! /usr/bin/python3

from itertools import combinations
from functools import reduce
from operator import mul
MAX = 2323218950681478446587180516177954549

with open("primes266.dat","r") as f:
	primes = [int( line.rstrip("\n")) for line in f]

MaxLengthChain = 0
c = 1
while c < MAX:
	c *= primes[MaxLengthChain]
	MaxLengthChain += 1

MinLengthChain = 0
c = 1
while c < MAX:
	c *= primes[-(MinLengthChain+1)]
	MinLengthChain += 1

print (MinLengthChain, MaxLengthChain)
theMax = 0
for length in range(MinLengthChain,MaxLengthChain+1):
	print( length)
	for combi in combinations( primes, length):
		m = reduce(mul, combi)
		if m < MAX and m > theMax:
			theMax = m
			#print("\t", theMax)

print( theMax, theMax % 10**16)
