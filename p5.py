#!/usr/bin/python

from fractions import gcd


#solving lcm by recursion

def lcm(listOfNumbers):
	if len(listOfNumbers) > 1:
		n1 = listOfNumbers[0]
		n2 = listOfNumbers[1]
		return lcm( [n1*n2/gcd(n1,n2)] + listOfNumbers[2:])
	else:
		return listOfNumbers[0]

print lcm( range(1,21))
