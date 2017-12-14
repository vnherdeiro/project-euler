#! /usr/bin/python

from __future__ import print_function

#s = set( [1])
#N = 15
#
#totalReturns = []
#def func( theSet, Nop):
#	print( max(theSet))
#	if max(theSet) > N:
#		return
#	elif max(theSet) == N:
#		totalReturns.append( Nop)
#		return
#	else:
#		for val1 in theSet:
#			for val2 in theSet:
#				newSet = theSet.copy()
#				newSet.add( val1 + val2)
#				func( newSet, Nop+1)
#
s = [1]
N = 15

minReturn = 12
def func( theList, Nop):
	#print( theList, Nop)
	global minReturn
	if Nop >= minReturn:
		return
	if theList[-1] == N and Nop < minReturn:
		print( Nop)
		minReturn = Nop
		return
	else:
		for val1 in theList:
			for val2 in theList:
				newVal = val1 + val2
				if newVal <= N and not newVal in theList:
					func( theList + [newVal], Nop+1)
func( s, 0)
print( minReturn)
