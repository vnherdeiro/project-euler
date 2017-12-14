#! /usr/bin/python

#tol = 1e-8
#def isInt(x):
#	return abs(x-int(x)) < tol

def nSol(n):
	x = 2*n
	y = 2*n
	nSolutions = 0
	while y >= n+1:
		nSolutions += n*y % (y-n) == 0
		y -= 1
	return nSolutions

print nSol(65546)
i = 4
while nSol(i) <= 1000:
	i += 1
	if 	i % 1000 == 0:
		print i

print i
