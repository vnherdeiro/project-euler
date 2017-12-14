#! /usr/bin/python

infile = "primes87.dat"

primes = [int(x) for x in open(infile)]


primes2 = [x**2 for x in primes]
primes3 = [x**3 for x in primes]
primes4 = [x**4 for x in primes]


primes2 = set(filter(lambda x : x < 50000000, primes2))
primes3 = filter(lambda x : x < 50000000, primes3)
primes4 = filter(lambda x : x < 50000000, primes4)

del primes

print map(len, (primes2,primes3,primes4))


val = [p1+p2+p3 for p1 in primes2 for p2 in primes3 for p3 in primes4 if p1+p2+p3 < 50000000]

val = set(val)

print len(val)


