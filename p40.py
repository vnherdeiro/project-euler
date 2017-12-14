#! /usr/bin/python

#solving euler project p40
#WORKS!

import numpy as np

def nDigits(x): #returns the number of digits of a number
	return int(np.ceil(np.log10(x+.001)))

def d(n):
	currentInt = 1
	passedDigits = 0
	while n - passedDigits - nDigits(currentInt) > 0:
		passedDigits += nDigits(currentInt)
		currentInt += 1
	#extracting the right digit now
	return int(str(currentInt)[n-passedDigits-1])

print d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000)
