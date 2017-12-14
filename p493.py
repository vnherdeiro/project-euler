#! /usr/bin/python
from __future__ import print_function
from random import shuffle
from math import factorial

#l = range(7)*10
#shuffle( l)
#
#sumColors = 0
#card = 0
#
#
#while True:
#	shuffle( l)
#	sumColors += len( set(l[:20]))
#	card += 1
#	if card % 100000 == 0:
#		print( "%.9f" % (float(sumColors)/card))


Nperms = factorial(70) / factorial(10)**7


def theProd( someList):
	return reduce( lambda x, y : x*y, map(factorial, someList))

def rec( theList, n):
	if n == 1:
		lastVar = 20 - sum(theList)
		if lastVar >= 1 and lastVar <= 10:
			return factorial(20) / theProd( theList + [lastVar])
		else:
			return 0
	else:
		theSum = 0
		for x in range(1,11):
			theSum += rec( theList + [x], n-1)
		return theSum
		
			
def p(n):
	return rec( [], n)

def colorPerm(n):
	return factorial(7) / (factorial(n) * factorial(7-n))

finalSum = 0
card = 0
for i in range(1,8):
	pi = p(i) * colorPerm(i)
	finalSum += i * pi
	card += pi

print( p(7))
print( card)
#finalCard = factorial(70)/ (factorial(50)*factorial(20))
print ( "%.10f" % (float(finalSum)/card))
