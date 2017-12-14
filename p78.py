#! /usr/bin/python


class Memoize:
	def __init__(self, f):
		self.f = f
		self.memo = {}

	def __call__(self, *args):
		if not args in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

@Memoize
def countPartitions(n):
	Npartitions = 0
	for x in xrange(n-1,0,-1):
		if n-x > 1:
			Npartitions += countPartitions(n-x)
		if n-x == 1:
			Npartitions += 1
	return Npartitions

print countPartitions(4)
