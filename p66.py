#! /usr/bin/python

from math import sqrt

round = lambda x : int(x+.5)
tol = 1e-10
def isSquare(x):
	x = sqrt(x)
	return abs(x - round(x)) < tol


def minX(D):
	#x^2 = 1+Dy^2
	y = 1
	while not isSquare(1+D*y*y):
		y += 1
	return round(sqrt(1+D*y*y))


#maxX = 0
#theD = 0
#for D in range(1,1001):
#	if not isSquare(D):
#		lmin = minX(D)
#		if lmin > maxX:
#			maxX = lmin
#			theD = D
#	if D % 50 ==0:
#		print D
#
#print theD, maxX

Ds = [x for x in xrange(1,1001) if not isSquare(x)]

print sorted(Ds,key=minX)[-10:]
