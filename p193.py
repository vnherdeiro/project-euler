#! /usr/bin/python

from collections import Counter

infile = "primes193.dat"
primes = [int(x)**2 for x in open(infile)]
#missing primes

MAX = 2**50
#MAX = 100001

i = 1
s = primes[0]
while s * primes[i] < MAX:
	s *= primes[i]
	i+=1
print i

#import numpy as np
#
#MAX = 2**10
#primes = np.array([2],dtype=np.int64)
#
#for i in xrange(3,MAX):
#	notPrime = False
#	for j in xrange( primes.size):
#		if i % primes[j] == 0:
#			notPrime = True
#			break
#	if not notPrime:
#		primes = np.append(primes, i)


theList = []

count = 0
print "doing overestimation..."
for p in primes:
	n = p
	while n < MAX:
		theList.append(n)
		count += 1
		n += p
	#count += int( (MAX-1)/n)

print MAX - 1 - len(set(theList))
theCounter = Counter(theList)
doubleCount = 0
for val,c in theCounter.items():
	if val == 33000:
		pass
		#print "\t\t",val, c 
	#if c >= 2:
	#	doubleCount += 1
print "\t"*3,theCounter[4356]

print MAX - 1 - count 
print "removing overcounting..."

#removing overcounting
#primes = primes[::-1]

listSub = []
for p1 in xrange(len(primes)):
	for p2 in xrange(p1+1,len(primes)):
		number = primes[p1] * primes[p2]
		if number > MAX - 1:
			break
		while number < MAX:
			listSub.append( number)
			count -= 1
			number += primes[p1] * primes[p2]
		#count -= int( (MAX-1)/number)

c2 = Counter(listSub)
print "\t"*3,c2[4356]
for val,c in c2.items():
	if theCounter[val] -c != 1:
		print "\t\t",val, theCounter[val] - c

print count
print MAX - 1 - count


