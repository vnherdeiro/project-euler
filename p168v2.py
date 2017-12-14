#! /usr/bin/python3

from collections import defaultdict

def rightRotate( n):
	s = str(n)
	return int( s[-1] + s[:-1])

MAX_LENGTH = 100
possibles = []
def rec( number, index, q):
	n = q * number % 10**index
	newDigit = n // 10**(index-1)
	#print( newDigit)
	number += newDigit * 10**index
	if len(str(number)) > MAX_LENGTH:
		return
	if rightRotate(number) == q*number:
		possibles.append( number)
		#return number
	#else:
	#what if different numbers have same root
	rec(number,index+1,q)


	
s = []
d = defaultdict( list)
for firstDigit in range(1,10):
	for q in range(1,10):
		n = rec( firstDigit, 1, q)
		#if n:
			#print( n, q)
		#	s.append(n)
		#	d.append(n)

#print( sorted(possibles)[:10])
print ( sum(possibles) % 10**5)

