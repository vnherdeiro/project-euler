#!/usr/bin/python

from math import sqrt


def isPrime(n):
	if n == 2:
		return True
	for i in xrange(2, int(sqrt(n)+1)):
		if n % i == 0:
			return False
	return True

def addCrown(theSize, lastVal):
	theSize += 2
	newPrimes = 0
	for i in range(3): #adding 3 values each time
		lastVal += theSize-1
		newPrimes += isPrime(lastVal)
	return newPrimes, theSize, lastVal + theSize -1

lastVal = 1
tab = [False] # starts with 1 -- not prime
nPrimes = 0
size = 1

densityHigher = True
threshold = .1
while densityHigher:
	newPrimes, size, lastVal = addCrown( size, lastVal)
	nPrimes += newPrimes
	density = float(nPrimes)/ (2*size - 1)
	#print density
	densityHigher = density > threshold

print size

#works really well!
