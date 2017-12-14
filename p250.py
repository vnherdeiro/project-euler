#! /usr/bin/python3

from collections import Counter
from functools import reduce
from operator import mul

def expo(n):
	n %= 250
	beg = n
	i = 1
	while i < beg:
		n *= beg
		n %= 250
		i += 1
	return n


theList = [expo(n) for n in range(1,251)]
c = Counter( theList)
setList = list( set( theList))
print( setList)


possibles = []

THE_MOD = 10**16
count = 0
def calcPossibles(theList, lastIndex):
	if lastIndex == len(setList):
		if sum( theList) % 250 == 0 and theList:
			global count
			count += reduce( mul, (c[val] for val in theList))
			count %= THE_MOD
			#possibles.append( theList)
			#print ( theList)
		return
	else:
		calcPossibles( theList, lastIndex+1)
		calcPossibles( theList + [setList[lastIndex]], lastIndex+1)

calcPossibles( [], 0)

#print( possibles)
#
#count = 0
#for p in possibles:
#	count += reduce( mul, [ c[val] for val in p])
#	count %= THE_MOD

print( count)
