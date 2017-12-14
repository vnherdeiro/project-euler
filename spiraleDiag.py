#!/usr/bin/python

#compose array of values increasing in a clockwise oriented spiral way
#then sum both diagonals


from sys import argv
import numpy as np

SIZE = int(argv[1])

mat = np.zeros( (SIZE,SIZE), dtype=int)

def writeCrown(theMat, val):
	h = theMat.shape[0] #always square
	#writing right
	for i in range(1,h):
		theMat[i,-1] = val
		val += 1
	#writing bottom
	for i in range(0,h-1)[::-1]:
		theMat[-1,i] = val
		val += 1
	#writing left
	for i in range(0,h-1)[::-1]:
		theMat[i,0] = val
		val += 1
	#writing top
	for i in range(1,h):
		theMat[0,i] = val
		val += 1
	return theMat, val

def growLayer(theMat):
	h = theMat.shape[0]
	newMat = np.zeros( (h+2,h+2), dtype=int)
	newMat[1:-1,1:-1] = theMat
	return newMat

theMatrix = np.ones( (1,1), dtype=int)
value = 2

while theMatrix.shape[0] < SIZE:
	theMatrix = growLayer(theMatrix)
	theMatrix, value = writeCrown( theMatrix, value)

print theMatrix

flippedMatrix = np.zeros( theMatrix.shape, dtype= theMatrix.dtype)

for i in xrange(len(theMatrix)):
	flippedMatrix[i] = theMatrix[i][::-1]

print np.diagonal(theMatrix).sum() + np.diagonal(flippedMatrix).sum() - 1
