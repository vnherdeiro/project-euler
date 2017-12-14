#!/usr/bin/python

class Memoize:
	def __init__(self, f):
		self.f = f
		self.memo = {}

	def __call__(self, *args):
		if not args in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

theDic = {}
def iter(n):
	return sum( map(lambda x : int(x)**2, str(n)))

def search(n):
	theList = []
	while n != 89 and n != 1:
		theList.append(n)
		n = iter(n)
	for element in theList:
		theDic[ element] = n
	return n

tot = 0
for i in xrange(1,10000000):
	if i in theDic:
		final = theDic[ i]
	else:
		final = search(i)
	if final == 89:
		tot += 1
	if i % 500000 == 0:
		print "\t\t", i

print tot
print len(dic)
