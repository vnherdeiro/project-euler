#! /usr/bin/python

infile = "primes193.dat"

with open(infile) as f:
	primes = [int(line.rstrip("\n")) for line in f]

MAX = int(1e7)
primes = filter( lambda x : x < MAX, primes)


def calcMax( p1, p2, val):
	global theMax
	if val <= MAX:
		if val > theMax:
			theMax = val
		calcMax( p1, p2, val*p1)
		calcMax( p1, p2, val*p2)

from itertools import combinations

s = set()
for p1, p2 in combinations( primes, 2):
	if p1 * p2 <= MAX:
		theMax = 0
		calcMax( p1, p2, p1*p2)
		#print ( p1, p2, theMax)
		s.add( theMax)


print(sum(s))
