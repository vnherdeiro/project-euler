#! /usr/bin/python3

from __future__ import print_function
import functools
from math import log10
primesInfile = "primes87.dat"

with open(primesInfile,"r") as f:
	primes = [int(n.rstrip("\n")) for n in f]

primes = primes[:500500]
l = []
primeMax = primes[-1]
k = 1
while primeMax**(1./ 2**k) > 2:
	index = 0
	while primes[index]**(2*k) < primeMax:
		l.append(primes[index]**(2**k))
		index += 1
	k += 1

print( "done building l")

finalList = sorted(primes + l)[:500500]

n = 1
for el in finalList:
	n *= el
	n %= 500500507
print(n)
