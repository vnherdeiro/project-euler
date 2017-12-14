#! /usr/bin/python3


import functools
from re import findall, compile

#@functools.lru_cache(maxsize=None)
#def fact(n):
#	if n == 0:
#		return 1
#	else:
#		return n * fact(n-1)
#
#
#def countOp( theStr):
#	return fact( len( findall("\+|\-|\*|/", theStr)))

opSerie = lambda x,y : (x * y) / (x + y)
opPara = lambda x,y : x + y
choices = (opSerie, opPara)

nFinal = 11
finalSet = set()
for n in range(1,nFinal+1):
	possibles = []
	cVal = 60
	def gen( theStr, number):
		if number == n:
			possibles.append( theStr + [cVal])
		else:
			for c in choices:
				gen( theStr + [cVal,c], number+1)


	gen( [], 1)

	s = set()

	def parse( elements):
		if len(elements) == 1:
			n = elements[0]
			global s
			s.add( n)
			return
		compose( elements)

	def compose( elements):
		if len(elements) == 3:
			try:
				res = elements[1]( elements[0], elements[2])
				#print( "\t"*5,res)
				global s
				s.add( res)
			except:
				pass
			return
		else:
			for index in range(0, len(elements)-2, 2):
				try:
					res = elements[index+1]( elements[index], elements[index+2])
				except:
					continue
				else:
					compose( elements[:index] + [res] + elements[index+3:])


	for i, p in enumerate(possibles):
		parse( p)

	finalSet |= s
print( finalSet)
print( len(finalSet))

def round( x):
	return 10**-5 * int( x * 10**5 + .5)

print( len( set( map( round, finalSet))))
