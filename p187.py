#!/usr/bin/python
import numpy as np


infile = "thePrimes.dat"
primes = np.loadtxt(infile, dtype=int)

theSum = 0
threshold = 10**8

for p1 in xrange(len(primes)):
	p2 = p1
	while p2 < len(primes) and primes[p1]*primes[p2] < threshold:
		theSum += 1
		p2 += 1

print theSum
