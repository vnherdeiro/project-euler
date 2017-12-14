#! /usr/bin/python

from fractions import gcd
from operator import mul

infile = "primesP50.dat"

primes = [int(x) for x in open(infile)]

MAX = 120000

primes = filter(lambda x : x <= MAX, primes)

primesSet = set(primes)
# def gcd(a,b):
# 	if a == 0:
# 		return b
# 	a, b = b%a, a
# 	return gcd(a,b)

class Memoize:
	def __init__(self, f):
		self.f = f
		self.memo = {}
	def __call__(self, *args):
		if not args in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

@Memoize
def rad(n):
	if n == 1:
		return 1
	if n in primesSet:
		return n
	return reduce( mul, [p for p in primes if p <= n and n % p == 0])


theList = []
for c in xrange(3,MAX):
	radC = rad(c)
	if radC < c:
		for b in xrange(2,c):
			if c-b < b and gcd(b,c) == 1 and rad(b)*rad(c-b)*radC < c:
				theList.append(c)
				print c

print len(theList), sum(theList)
#theList = set(theList)
#print len(theList),sum(theList)
