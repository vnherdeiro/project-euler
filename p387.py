#! /usr/bin/python3

from math import sqrt
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


def sumDigits(x):
	s = 0
	while x:
		s += x % 10
		x //= 10
	return s

def isHarshad(x):
	return x % sumDigits(x) == 0

def isStrongHarshad(x):
	if not isPrime( x/sumDigits(x)):
		return False
	return True
	#x //= 10
	#while x:
	#	if not isHarshad(x):
	#		return False
	#	x //= 10
	#return True


MAX = 10000

iteratorsList = list( range(1,10))
finalList = []

while iteratorsList:
	element = iteratorsList.pop()
	if element < MAX:
		if isPrime( element):
			finalList.append( element)
		if isHarshad( element):
			element *= 10
			for newIt in range(0,10):
				iteratorsList.append( element + newIt)

finalList = filter( isStrongHarshad, finalList)
finalList = sorted(list(finalList))
print( finalList)
print( sum(finalList))


