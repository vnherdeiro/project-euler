#! /usr/bin/python3

from itertools import product
from collections import deque
from functools import reduce, lru_cache


N = 4
l = []
for i in range(2**N):
	l.append([0,1])

print("0")
possibles = product( *l)

def cyclicSlice(theList, index, width):
	if index + width <= len(theList):
		return theList[index:index+width]
	else:
		return theList[index:] + theList[:width - (len(theList) - index)]

#needs optimization here -- exits before doing all compaision
def filterDiffSlices( l):
	return len( set(cyclicSlice(l,i,N) for i in range(len(l)))) == len(l)

def filterDiffSlicesV2( l):
	s = set()
	for i in range( len(l)):
		cyc = cyclicSlice( l, i, N)
		if cyc in s:
			return False
		else:
			s.add( cyc)	
	return True

factors = [2**i for i in range(N)]
@lru_cache(maxsize=None)
def hsh(l):
	return sum( x*y for x,y in zip(factors,l))

def filterDiffSlicesV3( l):
	s = set()
	cyc = deque(l)
	for i in range( len(l)):
		cyc.rotate( -1)
		t = sum(x*y for x,y in zip(cyc,factors))
		if t in s:
			return False
		else:
			s.add( t)	
	return True

def filterDiffSlicesV4( l):
	theL = l + l[:N]
	s = set()
	for i in range( len(l)):
		t = hsh( theL[i:i+N])
		if t in s:
			return False
		else:
			s.add( t)
	return True


print("1")
possibles = list( filter( filterDiffSlicesV2, possibles))

#identify equal by rotation
#rotate to put max consecutive 0 on the left
def rotate( theList):
	maxZero = 0
	maxIndex = 0
	for i in range( len(theList)):
		j = 0
		while theList[ (i+j) % len(theList)] == 0:
			j += 1
		if j > maxZero:
			maxZero = j
			maxIndex = i
	#return theList[maxIndex:] + theList[:maxIndex]
	return cyclicSlice( theList, maxIndex, len(theList))

print("2")
possibles = set( map( rotate, possibles))
print("3")
possibles = ["".join( map(str,p)) for p in possibles]
print( possibles)
print("4")
possibles = [int(p,2) for p in possibles]
print( sum(possibles))

#eof


##WRITE DOWN ALL 5BITS INTS THEN ALL POSSIBLE TRANSITIONS TO GENERATE THE RING
