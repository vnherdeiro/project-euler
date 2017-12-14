#! /usr/bin/python3

from itertools import permutations, combinations_with_replacement
from functools import reduce
from sys import exit

#checking if pandigital in basis b:
def isPandigital( n, b):
	digits = set()
	while n:
		digits.add( n % b)
		if len(digits) == b:
			break
		n //= b
	return len(digits) == b

listPand = []
MAX_BASIS = 12
compositionLaw = lambda x,y : MAX_BASIS*x + y
def check( somePerm):
	n = reduce( compositionLaw, somePerm)
	if all( isPandigital(n,basis) for basis in range(MAX_BASIS-1, 1, -1)):
		print("\t\t%d" % n)
		listPand.append(n)
		if len(listPand) == 10:
			print( sum( sorted(listPand)[:10]))
			exit()
			#should return the minimum sum at first -- ~stability of the permutation algorithm

#generate 12-pandigital numbers from permutations
addedLength = 0
while True:
	pool = list( range(MAX_BASIS))
	if addedLength > 0:
		addons = combinations_with_replacement( range(MAX_BASIS), addedLength)
		for addon in addons:
			for p in permutations( pool + list(addon)):
				if p[0] != 0:
					check( p)
	else:
		for p in permutations( pool):
			if p[0] != 0:
				check( p)
	addedLength += 1

