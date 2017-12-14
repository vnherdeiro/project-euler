#! /usr/bin/python

def properDivisors(x):
	return [n for n in xrange(1,x/2+1) if x % n == 0]

class Memoize:
	def __init__(self, f):
		self.f = f
		self.memo = {}
	def __call__(self, *args):
		if not args in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

@Memoize
def iter(x):
	return sum( properDivisors(x))


alreadyParsed = set()

longestChain = 0
minElementinChain = 0

pos = 2

while pos < 1000000:
	i = pos
	currentChain = [i]
	while i != 0 and i != 1 and i <= 1000000:
		i = iter(i)
		if i == currentChain[0]: #isamicable
			if len(currentChain) > longestChain:
				longestChain = len(currentChain)
				minElementinChain = min(currentChain)
				break
		if i in currentChain[1:]: #looping but not coming back to initial value
			break
		currentChain.append( i)
	if pos % 10000 == 0:
		print pos
	pos += 1

print minElementinChain
