#! /usr/bin/python3

from numpy import sqrt

round = lambda x : int(x+.5)
tol = 1e-7
isInt = lambda x : abs(x-round(x)) < tol

setPower2 = set( 2**i for i in range(1,2000))
isPower2 = lambda x : x in setPower2

def solve(n):
	return (1+sqrt(1+4*n))/2


"""
cardAll = 0
cardPerfect = 0
frac = 1
n = 2
while frac > 1./12345:
	solution = solve( n)
	if isInt( solution):
		#print( n,end="")
		cardAll += 1
		if isPower2( solution):
			cardPerfect += 1
			#print( "\t1", end="")
			print(n, "\t", 1)
		#print()
		frac = float( cardPerfect)/cardAll
	n += 1

print(n)
"""


cardAll = 0
cardPerfect = 0
k = 1
while True:
	n = k**2 + k
	#print(n)
	cardAll += 1
	#print( n, end="")
	solution = (1 + sqrt(1+4*n))/2
	if isPower2( solution):
		cardPerfect += 1
		#print("\t", 1, end="")
		print(n, "\t", 1)
	#print()
	if (12345*cardPerfect) < cardAll:
		break
	else:
		k += 1
		#print( n, float(cardPerfect)/cardAll)

print( k**2+k)

	
		

