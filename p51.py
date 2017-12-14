#! /usr/bin/python

infile = "primes87.dat"
primes = [int(x) for x in open(infile)]

#primes = primes[:50000]
primes = primes
setPrimes = set(primes)

dejaVus = set()

for p in primes:
	if p not in dejaVus:
		nDigits = len(str(p))
		for d1 in xrange(0,nDigits-1):
			for d2 in xrange(d1+1,nDigits):
				for d3 in xrange(d2+1,nDigits):
					strP = str(p)
					nPrimes = 0
					lList = []
					for newDigit in (xrange(0,10) if d1 !=0 else xrange(1,10)):
						strP = strP[:d1] + str(newDigit) + strP[d1+1:d2] + str(newDigit) + strP[d2+1:d3] + str(newDigit) + strP[d3+1:] 
						#strP = strP[:d2] + str(newDigit) + strP[d2+1:]
						#print p, strP
						newInt = int(strP) 
						if newInt in setPrimes:
							nPrimes += 1
							lList.append( newInt)
							dejaVus.add( newInt)
						if nPrimes >= 8:
							print lList, d1,d2,d3

