#! /usr/bin/python

from bisect import insort_left

class m:
	def __init__(self, n):
		self.MIN = 999
		self.n = n

	def solve( self):
		#trivial cases
		if self.n == 1:
			return 0
		power2 = [2**i for i in range(8)]
		if self.n in power2:
			from math import log
			return int( log(self.n)/log(2) + .5)
		self.gen( [1], 0)
		return self.MIN

	def gen( self, theList, Nop):
		if Nop >= self.MIN:
			return
		for index1, val1 in enumerate(theList[::-1]):
			for val2 in theList[index1:][::-1]:
				newVal = val1 + val2
				if newVal == self.n:
					if Nop + 1 < self.MIN:
						self.MIN = Nop + 1
					return
				elif  newVal < self.n and newVal not in theList:
					newList = theList[:]
					insort_left( newList, newVal)
					self.gen( newList, Nop+1)


	def improveBound( self): #improve the bound by binary method
		l = [1]
		Nop = 0
		while max(l) < self.n:
			for val in l[::-1]:
				if max(l) + val <= self.n:
					l.append( max(l) + val)
					Nop += 1
					break
		self.MIN = Nop


for i in range(1,30):
	a = m(i)
	a.improveBound()
	#print( "\t\t%d" %a.MIN)
	print( "%d %d" %(i, a.solve()))
			
