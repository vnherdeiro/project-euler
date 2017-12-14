#! /usr/bin/python3

from heapq import heappop, heappush

infile = "primes87.dat"
with open(infile) as f:
	primes = [int(l.rstrip("\n")) for l in f]

def has200( n):
	return "200" in str(n)


#unique members priority queue
class HeapSet:

	def __init__(self):
		self.theSet = set()
		self.theList = []

	def add(self, n, i, j):
		if n not in self.theSet:
			heappush( self.theList, (n, i, j))
			self.theSet.add( n)

	def pop(self):
		return heappop( self.theList)

myHeap = HeapSet()
val = primes[0]**3 * primes[1]**2
myHeap.add( val, 0, 1)
val = primes[1]**3 * primes[0]**2
myHeap.add( val, 1, 0)

while True:
	n, i, j = myHeap.pop()
	if i > j:
		val = primes[i+1]**3 * primes[j]**2
		myHeap.add( val, i+1, j)
		val = primes[i+1]**3 * primes[j+1]**2
		myHeap.add( val, i+1, j+1)
	else:
		val = primes[i]**3 * primes[j+1]**2
		myHeap.add( val, i, j+1)
		val = primes[i+1]**3 * primes[j+1]**2
		myHeap.add( val, i+1, j+1)
	if has200(n):
		print( n)

