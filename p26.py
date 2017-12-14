#! /usr/bin/python

import re
from decimal import *

def repetitions(s):
   r = re.compile(r"(.+?)\1+")
   for match in r.finditer(s):
       yield (match.group(1), len(match.group(0))/len(match.group(1)))


getcontext().prec= 3000

values = []
for i in xrange(2,1000):
	theString = (Decimal(1)/Decimal(i)).to_eng_string()
	repetitionList = list( repetitions(theString))
	if repetitionList:
		#print repetitionList[0]
		longestString = max(repetitionList, key = lambda x : len(x[0]))
		#print i, longestString
		values.append( [i, len(longestString[0])])

print sorted(values, key = lambda x : x[1])[-10:]

