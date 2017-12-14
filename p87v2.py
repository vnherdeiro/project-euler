#! /usr/bin/python

infile = "primes87.dat"

primes = [int(x) for x in open(infile)]


primes2 = [x**2 for x in primes]
primes3 = [x**3 for x in primes]
primes4 = [x**4 for x in primes]


primes2 = set(filter(lambda x : x < 50000000, primes2))
primes3 = filter(lambda x : x < 50000000, primes3)
primes4 = filter(lambda x : x < 50000000, primes4)


print map(len, (primes2,primes3,primes4))

del primes


theNumber = 1
theSum = 0

while theNumber < 50000000:
	index1 = 0
	hasFound = False
	while index1 < len(primes4) and primes4[index1] < theNumber and not hasFound:
		index2 = 0
		while index2 < len(primes3) and primes4[index1] + primes3[index2] < theNumber:
			if theNumber - primes4[index1] - primes3[index2] in primes2:
				hasFound = True
				break
			index2 += 1
		index1 +=1
	if hasFound:
		theSum += 1
	if theNumber % 1000000 == 0:
		print theNumber
	theNumber += 1

print theSum
