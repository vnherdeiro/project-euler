#!/usr/bin/python

#gen the lists first

from itertools import permutations
triList = []
def tri(n):
	return n*(n+1)/2
n = 1
while tri(n) < 10000:
	if tri(n) >= 1000:
		triList.append( tri(n))
	n += 1

squareList = []
def sq(n):
	return n*n
n = 1
while sq(n) < 10000:
	if sq(n) >= 1000:
		squareList.append( sq(n))
	n += 1

pentaList = []
def penta(n):
	return n*(3*n-1)/2
n = 1
while penta(n) < 10000:
	if penta(n) >= 1000:
		pentaList.append( penta(n))
	n += 1

hexaList = []
def hexa(n):
	return n*(2*n-1)
n = 1
while hexa(n) < 10000:
	if hexa(n) >= 1000:
		hexaList.append( hexa(n))
	n += 1

heptaList = []
def hepta(n):
	return n*(5*n-3)/2
n = 1
while hepta(n) < 10000:
	if hepta(n) >= 1000:
		heptaList.append( hepta(n))
	n += 1

octaList = []
def octa(n):
	return n*(3*n-2)
n = 1
while octa(n) < 10000:
	if octa(n) >= 1000:
		octaList.append( octa(n))
	n += 1

#totalCombi = 1
#for l in (triList, squareList, pentaList, hexaList, heptaList, octaList):
#	totalCombi *= len(l)
#print totalCombi

theLists = [triList, squareList, pentaList, hexaList, heptaList, octaList]

for l in theLists:
	print len(l)

#for x in heptaList:
#	last2 = x%100
#	first2 = x/100
#	inHexa= False
#	for y in hexaList:
#		if y%100 == first2:
#			inHexa = True
#			break
#	inOcta = False
#	if inHexa:
#		for y in octaList:
#			if y/100 == last2:
#				inOcta = True
#				break
#	if inOcta and inHexa:
#		print "\t\t\t",x
#

def g(currentList,preList,postList):
	toKeep = []
	for x in currentList:
		last2 = x%100
		first2 = x/100
		inHexa= False
		for y in preList:
			if y%100 == first2:
				inHexa = True
				break
		inOcta = False
		if inHexa:
			for y in postList:
				if y/100 == last2:
					inOcta = True
					break
		if inOcta and inHexa:
			#print "\t\t\t",x
			toKeep.append(x)
	currentList = toKeep
	return currentList[:]

#octaList = g(octaList,heptaList,triList)
#triList = g(triList,octaList,squareList)
#print octaList,triList

def isDone(theLs):
	global theLists
	return all( len(l) == 1 for l in theLs)

def isEmpty(theLs):
	return all( len(l) == 0 for l in theLs)


#for thePerm in permutations(theLists):
#	thePerm = list(thePerm)
#	i=0
#	while not (isDone(thePerm) or isEmpty(thePerm)):
#		thePerm[i] = g(thePerm[i],thePerm[i-1],thePerm[(i+1)%len(thePerm)])
#		#print map(len,thePerm)
#		i += 1
#		if i >= len(thePerm):
#			i %= len(theLists)
#	if isDone(thePerm):
#		print sum(x[0] for x in thePerm)

#suppressing one redundancy
list1 = [theLists[0]]
for thePerm in permutations(theLists[1:]):
	thePerm = list1[:] + list(thePerm)
	i=0
	while not (isDone(thePerm) or isEmpty(thePerm)):
		thePerm[i] = g(thePerm[i],thePerm[i-1],thePerm[(i+1)%len(thePerm)])
		#print map(len,thePerm)
		i += 1
		if i >= len(thePerm):
			i %= len(theLists)
	if isDone(thePerm):
		print sum(x[0] for x in thePerm)

#print theLists

#return 9 choices
#def filterTheList(theList, otherLists):
#	for element1 in list(theList):
#		notFound = True
#		while notFound:
#			for otherList in otherLists:
#				for element in otherList:
#					if element1 % 100 == element/100:
#						notFount = False
#						break
#		if notFound: #not found in any other list
#			theList.remove( element1)
#
## #filtering all the lists:
## for listIndex in range( len(theLists)):
## 	filterTheList( theLists[listIndex], theLists[:listIndex] + theLists[listIndex+1:])
#
#def isConcatenable(element, theList):
#	for element2 in theList:
#		if element % 100 == element2/100:
#			return True
#	return False
#
##filtering all the lists:
#for listIndex in range( len(theLists)):
#	otherList = []
#	for l in theLists[:listIndex] + theLists[listIndex+1:]:
#		otherList += l
#	theLists[listIndex] = [x for x in theLists[listIndex] if isConcatenable(x,otherList)]
#
#for l in (triList, squareList, pentaList, hexaList, heptaList, octaList):
#	print len(l)o


#solving by recursion
#for l, index in zip(theLists, [4465, 6561, 6112, 1225, 2512, 1281]):
#	print l.index(index)
#
#def f(theLists, theChain=[]):
#	nextList = theLists[0]
#	if not theChain:
#		for x in nextList:
#			f(theLists[1:],[x])
#	else:
#		last = theChain[-1]
#		if len(theLists) == 1:
#			for y in nextList:
#				if y/100 == last % 100:
#					print theChain + [y]
#		else:
#			for y in nextList:
#				if y/100 == last % 100:
#					f(theLists[1:],theChain+[y])
#

#f(theLists, 0)
