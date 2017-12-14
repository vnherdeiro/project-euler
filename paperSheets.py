#! /usr/bin/python


from random import shuffle
from math import sqrt

defaultEnvlp = [8,4,2,1]
splitResult = {8 : [4,2,1], 4 : [2,1], 2 : [1]}

count = 0
countTrue = 0
while True:
	for index in xrange(100000):
		theEnvlp = defaultEnvlp[:]
		for i in xrange(14):
			if len(theEnvlp) == 1:
				countTrue += 1
			count += 1
			shuffle(theEnvlp)
			pick = theEnvlp.pop()
			if pick > 1:
				theEnvlp += splitResult[pick]
	p = float(countTrue)/count
	print p,"\t", sqrt(p*(1-p)/count)
