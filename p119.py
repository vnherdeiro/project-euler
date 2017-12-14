#! /usr/bin/python

from sys import exit

def sumDigits( n):
	return sum( map(int, str(n)))

#ini = 11
#index = 1
#
#while True:
#	baseN = sumDigits(ini)
#	if baseN != 1:
#		n = baseN
#		while n < ini:
#			n *= baseN
#		if n == ini:
#			print index, ini
#			index += 1
#	ini += 1
#

theList = []
POWER_MAX = 30
for i in range(2,400):
	p = 1
	n = i
	while p <= POWER_MAX:
		if n > 10 and sumDigits(n) == i:
			theList.append( n)
		p += 1
		n *= i
	
	
print( sorted(theList))
print( sorted(theList)[29])

#eof
