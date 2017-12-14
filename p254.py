#! /usr/bin/python3

from math import factorial
from itertools import combinations_with_replacement


cwr = combinations_with_replacement

factTab = [factorial(n) for n in range(10)]

def f(x):
	digits = map(int, str(x))
	return sum( factTab[x] for x in digits)

def sf(x):
	return sum( int(d) for d in str(f(x)))

def sumDigits(x):
	return sum( int(d) for d in str(x))


#theDic = {}
#x = 1
#MAX = 20
#while len(theDic) < MAX:
#	g = sf(x)
#	if 1 <= g <= MAX and not g in theDic:
#		theDic[g] = x
#		print( x, g)
#	x += 1
#
#
#print( theDic)
#print( sum( map( sumDigits, theDic.values())))
#

def minimal( c):
	c = list( c)
	nZeroes = 0
	while 0 in c:
		c.pop(0)
		nZeroes += 1
	c = sorted(c)
	for i in range(nZeroes):
		c.insert( 1, 0)
	return int( "".join( map(str,c)))

theDic = {}
MAX = 150
length = 1
while len(theDic) < MAX:
	print( length, len(theDic))
	for combi in cwr( range(0,10), length):
		sf = sumDigits(sum( factTab[i] for i in combi))
		if 1 <= sf <= MAX:
			m = minimal( combi)
			if m != 0 and (sf not in theDic or theDic[sf] > m):
				theDic[sf] = m
	length += 1
	
print( theDic)
print( sum( map( sumDigits, theDic.values())))
