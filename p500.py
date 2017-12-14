#! /usr/bin/python3

from __future__ import print_function
import functools
from math import log10
primesInfile = "primes87.dat"

with open(primesInfile,"r") as f:
	primes = [int(n.rstrip("\n")) for n in f]


kTab = [0] * len(primes)
logPrimes = [log10(p) for p in primes]

@functools.lru_cache(maxsize=None)
def primePower( thePrime, thePower):
	return thePrime**thePower

card = 0
while card < 500500:
	index = 0
	#while primes[index]**(2*kTab[index]) > primes[index+1]**(2*kTab[index+1]):
	lMin = primePower(primes[index], 2**kTab[index])
	minPrime = index
	while kTab[index] + kTab[index+1] > 0:
		newVal = primePower( primes[index+1],2**kTab[index+1])
		if newVal < lMin:
			minPrime = index+1
			lMin = newVal
		index += 1
	#while primePower(primes[index],2*kTab[index]) > primePower(primes[index+1],2*kTab[index+1]):
	#while logPrimes[index] * 2**(kTab[index]-kTab[index+1]) > logPrimes[index+1]:
	#	index += 1
	#kTab[index] += 1
	kTab[minPrime] += 1
	card += 1
	if card % 10000 == 0:
		print( card)

del primePower
#check decreasing
assert all( [a >= b for a,b in zip(kTab[:-1],kTab[1:])]), "not decreasing kTab!"
print( "done calculating tab")
n = 1
index = 0
while kTab[index] > 0:
	count = 1
	lastF = primes[index]**2
	N1 = primes[index]
	newFactor = N1
	while count <= kTab[index]-1:
		newFactor *= lastF
		newFactor %= 500500507
		lastF = lastF**2
		lastF %= 500500507
		count += 1
	n *= newFactor
	n %= 500500507
	index += 1

print( n)
