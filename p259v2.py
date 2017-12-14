#! /usr/bin/python3


import functools
from re import findall, compile

@functools.lru_cache(maxsize=None)
def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)


def countOp( theStr):
	return fact( len( findall("\+|\-|\*|/", theStr)))

#choices = ["", "(" , ")", "+", "-", "/", "*"]
opC = lambda x,y : 10*x + y #composition in basis=10
op1 = lambda x,y : x + y
op2 = lambda x,y : x - y
op3 = lambda x,y : x / y
op4 = lambda x,y : x * y
choices = (opC, op1, op2, op3, op4)
possibles = []
def gen( theStr, number):
	if number == 9:
		possibles.append( theStr + [9])
	else:
		for c in choices:
			gen( theStr + [number,c], number+1)


gen( [], 1)
def applyOPC( p):
	index = 0
	while index < len(p) - 2:
		if p[index+1] == opC:
			p = p[:index] + [opC(p[index],p[index+2])] + p[index+3:]
		else:
			index += 2
	return p
possibles = [ applyOPC(p) for p in possibles]
s = set()
def isInt(x):
	return abs(x - int(x+.5)) < 1e-8


def parse( elements):
	if len(elements) == 1:
		n = elements[0]
		if n > 0 and isInt(n):
			global s
			s.add( int(n))
		return
	compose( elements)

def compose( elements):
	if len(elements) == 3:
		try:
			res = elements[1]( elements[0], elements[2])
			#print( "\t"*5,res)
			if res > 0 and isInt(res):
				global s
				s.add( int(res))
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


for i,p in enumerate(possibles):
	#if not p[-1].isdigit():
	#	print( p)
	parse( p)
	if i % 10000 == 0:
		print(i)
print(sum(s))
