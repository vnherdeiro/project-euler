#! /usr/bin/python

class Memoize:
	def __init__(self, f):
		self.f = f
		self.memo = {}
	def __call__(self, *args):
		if not args in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

def summingWays(n,nmax): #calculates the total number of ways of summing up to n with numbers <= nmax
	totalWays = 0
	for number in xrange(nmax,0,-1):
		if n - number >= 1:
			totalWays += summingWays(n-number,number)
		if n - number == 0:
			totalWays += 1
	return totalWays

summingWays = Memoize(summingWays)

def summingWaysIni(n): #total ways of summing up to n
	return summingWays(n,n-1)

print summingWaysIni(100)
