#! /usr/bin/python

from fractions import gcd

infile = "primes87.dat"

primes = [ int(x) for x in open(infile)]
primes = filter( lambda x : x <= 1000003, primes)
primes = primes[2:]

s = 0
for p1, p2 in zip(primes[-2:-1],primes[-1:]):
	nDig = len(str(p1))
	i = 1
	while True:
		number = i*10**nDig + p1
		if number % p2 == 0:
			s += number
			break
		i += 1
print s
