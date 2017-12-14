#! /usr/bin/python3

from __future__ import print_function
import functools
from mpmath import mp
primesInfile = "primes87.dat"

with open(primesInfile,"r") as f:
	primes = [int(n.rstrip("\n")) for n in f]


kTab = [0] * len(primes)


card = 0
n = 1
while card < 500500:
	index = 0
	lMin = primes[index]
	minIndex = index
	while kTab[index] + kTab[index+1] > 0:
		newVal = primes[index+1]
		if newVal < lMin:
			minIndex = index + 1
			lMin = newVal
		index += 1
	kTab[minIndex] += 1
	print( minIndex, lMin)
	#print( lMin, kTab[:5], primes[:5])
	n *= lMin
	n %= 500500507
	primes[ minIndex] = primes[ minIndex]**2
	#print ( primes[minPrime])
	card += 1
	if card % 1000 == 0:
		print( card)

print( n)

#
#from collections import defaultdict
#
#
#kDic = defaultdict(list)
##kDic[0] = primes #only copying the 10000th first primes
#kDic = [ primes] #only copying the 10000th first primes
#kMax = 0
#
#card = 0
#n = 1
#while card < 500500:
#	index = 0
#	kMinIndex = kMax
#	lMin = kDic[kMax][0]
#	kIndex = kMax -1
#	while kIndex >= 0:
#		newVal = kDic[kIndex][0]
#		if newVal < lMin:
#			kMinIndex = kIndex
#			lMin = newVal
#		kIndex -= 1
#	kDic[kMinIndex].pop(0)
#	if kMax == kMinIndex:
#		kMax += 1
#		kDic.append( [lMin**2])
#	else:
#		kDic[kMinIndex+1].append( lMin**2)
#	n *= lMin
#	n %= 500500507
#	card += 1
#	if card % 1000 == 0:
#		print( card)
#
#print( n)
