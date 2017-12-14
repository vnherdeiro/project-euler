#!/usr/bin/python

#def isPrime(n):
# 	if n == 2:
# 		return True
# 	for i in xrange(2,n/2):
# 		if n % i == 0:
# 			return False
# 	return True
#
# thePrimes = [x for x in range(2,1000000) if isPrime(x)] #lists all the primes samller than one million
#
# print len(thePrimes)


##calculating the primes up to a million
#primes = [2]
#for n in xrange(3, 1000000):
#	isPrime = True
#	for prime in primes:
#		if n % prime == 0:
#			isPrime = False
#			break
#	if isPrime:
#		primes.append( n)
#
#print primes, len(primes)

infile = "primesP50.dat"

thePrimes = [int(x) for x in open(infile)]


theMax = 0
sumLength = 0

for ini in xrange(len(thePrimes)-1):
	val = thePrimes[ini]
	nextIndex = ini + 1
	while val + thePrimes[nextIndex] < 1000000:
		val += thePrimes[nextIndex]
		nextIndex += 1
	if val in thePrimes[::-1] and nextIndex - ini + 1 > sumLength:
		sumLength = nextIndex - ini + 1
		theMax = val
		print theMax

print theMax

