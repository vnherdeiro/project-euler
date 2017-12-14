#!/usr/bin/python



import numpy as np
from sys import argv

#SIZE = int(argv[1])

def isPrime(n):
	if n == 2:
		return True
	for i in xrange(2,n/2):
		if n % i == 0:
			return False
	return True

isPrime = np.vectorize( isPrime)

def writeCrown(theMat, val):
	h = theMat.shape[0] #always square
	#writing right
	for i in xrange(-2,-h,-1):
		theMat[i,-1] = val
		val += 1
	#writing top
	for i in xrange(h-1,-1,-1):
		theMat[0,i] = val
		val += 1
	#writing left
	for i in xrange(1,h):
		theMat[i,0] = val
		val += 1
	#writing bottom
	for i in xrange(1,h):
		theMat[-1,i] = val
		val += 1
	return theMat, val

def growLayer(theMat):
	h = theMat.shape[0]
	newMat = np.zeros( (h+2,h+2), dtype=int)
	newMat[1:-1,1:-1] = theMat
	return newMat

theMatrix = np.ones( (1,1), dtype=int)
value = 2

# print theMatrix
#theMatrix = growLayer(theMatrix)
#print writeCrown(theMatrix, value)
densityHigher = True
threshold = .1
while densityHigher:
	theMatrix = growLayer(theMatrix)
	theMatrix, value = writeCrown( theMatrix, value)
	mainDiag = np.diag(theMatrix)
	oppositeDiag = np.diag(np.flipud(theMatrix))
	totalDiag = np.r_[ mainDiag, oppositeDiag[:len(oppositeDiag)/2], oppositeDiag[len(oppositeDiag)/2 + 1:]]
	#print theMatrix.shape, mainDiag, oppositeDiag, totalDiag, isPrime(totalDiag)
	density = np.mean( isPrime(totalDiag))
	print density
	densityHigher = density > threshold

print theMatrix.shape

##VERY VERY INEFFICIENT!! -- only keep the corners and more efficent checking if prime
