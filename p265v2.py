#! /usr/bin/python3

from collections import defaultdict

transitions = defaultdict( list)
#transitions = {}

N = 5

for n in range(2**N):
	s = bin(n)[2:]
	b = s.zfill(N)
	int1 = int( b[1:] + "0", 2)
	if int1 != n:
		transitions[n].append( int1)
	int2 = int( b[1:] + "1", 2)
	if int2 != n:
		transitions[n].append( int2)

possibles = []
def gen( theList):
	if len( theList) == 2**N - N + 1:
		#if theList[0] in transitions[ theList[-1]]:
	#needs to be removed because the circular calculation is not has simple -- it is not the [1:] for of the last need to match the [:-1] of the first
		possibles.append( theList)
	else:
		for tr in transitions[ theList[-1]]:
			if tr not in theList:
				gen(theList + [tr])
#generate all chains
for n in range(2**N):
	gen([n])

def check( theList):
	theStrings = list(map(lambda x : bin(x)[2:].zfill(N), theList))
	theStrings = theStrings[:] + [theStrings[0]]
	for el1, el2 in zip( theStrings[:-1], theStrings[1:]):
		assert el1[1:] == el2[:-1]

def cyclicSlice(theList, index, width):
	if index + width <= len(theList):
		return theList[index:index+width]
	else:
		return theList[index:] + theList[:width - (len(theList) - index)]

def translate( theList):
	theStrings = list(map(lambda x : bin(x)[2:].zfill(N), theList))
	return "".join( [theStrings[0]] + [s[-1] for s in theStrings[1:]])

#for x,y in zip( possibles, map( translate, possibles)):
#	print( x,y)

def filterDiffSlicesV2( theStr):
	exStr = theStr + theStr[:N]
	s = set()
	for i in range( len(theStr)):
		cyc = exStr[i:i+N]
		if cyc in s:
			return False
		else:
			s.add( cyc)	
	return True

possibles = map( translate, possibles)
possibles = list( filter( filterDiffSlicesV2, possibles))

#identify equal by rotation
#rotate to put max consecutive 0 on the left
def rotate( theStr):
	theList = list(map(int, theStr))
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
	return tuple(cyclicSlice( theList, maxIndex, len(theList)))

print("2")
possibles = set( map( rotate, possibles))
#print( possibles)
print("3")
possibles = ["".join( map(str,p)) for p in possibles]
#print( possibles)
print("4")
possibles = [int(p,2) for p in possibles]
print( sum(possibles))

