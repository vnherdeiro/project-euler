#! /usr/bin/python3

from string import ascii_lowercase
from itertools import combinations
from math import factorial
from functools import lru_cache

letters = [x for x in ascii_lowercase]

@lru_cache(maxsize=None)
def binomial(x, y):
	return int(factorial(x)/(factorial(y)*factorial(x-y)))

#for length in range(3,26):
#	print( length, len( list( combinations( letters, length))))

#check now if all 1 height words can be generated with neighbour transpotions and rotations on the ordered words

#def is1Height( word):
#	vals = list(map(ord, word))
#	flagged = False
#	for i in range( len( vals)-1):
#		if vals[i+1] < vals[i]:
#			if not flagged:
#				flagged = True
#			else:
#				return False #at least two heights
#	return flagged
#
#
#letters = [x for x in "abcd"]
#from itertools import permutations
#for p in permutations( letters):
#	word = "".join( p)
#	if is1Height( word):
#		print( word)

def p(n):
	p = 0
	for l1 in range(1,n):
		l2 = n - l1
		for w1 in combinations(letters, l1):
			complement = [l for l in letters if l not in w1]
			#second loop could be replaced by some smart counting
			#for w2 in combinations(complement, l2):
			#	if w1[-1] > w2[0]:
			#		p += 1
			for index, l in enumerate(complement):#[:-l2+1]):
				if w1[-1] > l and len(complement) - 1 - index >= l2 - 1:
					p += binomial( len(complement) - 1 - index, l2-1)
	return p

for n in range(15,20):
	print( n, p(n))

#solve by splitting with combinations part1 (length 1) + part2 (length 2) with height between part1 and part2
