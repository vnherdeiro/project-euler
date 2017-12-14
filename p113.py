#! /usr/bin/python

def countIncreasing(nDigits):
	theSum = 0
	for dig in xrange(1,nDigits+1):
		theSum += countIncreasingDigit(1,dig)
	return theSum

def countIncreasingDigit(theMin, nDigit):
	if nDigit == 1:
		return 9-theMin + 1
	else:
		combi = 0
		for runningMin in xrange(theMin,10):
			combi += countIncreasingDigit(runningMin,nDigit-1)
		return combi

def countDecreasingDigit(theMax, nDigit):
	if nDigit == 1:
		return theMax + 1 #counting the zero
	else:
		combi = 0
		for runningMax in xrange(theMax,-1,-1):
			combi += countDecreasingDigit(runningMax, nDigit-1)
		return combi

def countDecreasing(nDigits):
	theSum = 0
	for dig in xrange(1,nDigits+1):
		theSum += countDecreasingDigit(9,dig)
	return theSum


Ndigits = 10
#print countIncreasing(Ndigits) + countDecreasing(Ndigits) - 9*(Ndigits)
print countIncreasing(Ndigits)
