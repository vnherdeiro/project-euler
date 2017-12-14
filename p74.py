#! /usr/bin/python

from math import factorial


#solving with memoization

def iter(n):
	return sum( map(factorial, map(int, str(n))))
#could be sped up by storing factorial values
theDic = {}

def measIter(n):
	global theDic
	if n in theDic:
		return theDic[n]
	x = iter(n)
	theList = [n]
	while x not in theList:
		theList.append(x)
		x = iter(x)
	posIni = theList.index(x)
	for index, element in enumerate(theList[:posIni]):
		theDic[element] = len(theList) - index
	for element in theList[posIni:]:
		theDic[element] = len(theList[posIni:])
	return len(theList)

print sum( measIter(n) == 60 for n in xrange(1,1000000))
