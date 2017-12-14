#!/usr/bin/python

import numpy as np

mat = np.loadtxt("p11_matrix.txt",dtype=int)

def calc4prod(theInput): #calculates the product of 4 numbers in list
	assert len(theInput)==4
	return reduce( lambda x,y : x*y, theInput)

theMax = 0
#slicing along digonals
for i in xrange(-19,20):
	theDiag = mat.diagonal(i)
	if len(theDiag) >= 4:
		for index in range(0,len(theDiag)-3):
			theMax = max(theMax, calc4prod(theDiag[index:index+4]))

mat2 = mat.copy()
for i in range(20):
	mat2[i] = mat[i][::-1]

for i in xrange(-19,20):
	theDiag = mat2.diagonal(i)
	if len(theDiag) >= 4:
		for index in range(0,len(theDiag)-3):
			theMax = max(theMax, calc4prod(theDiag[index:index+4]))

#along rows
for row in mat:
	for index in range(0, len(row)-3):
		theMax = max(theMax, calc4prod(row[index:index+4]))


#along cols
for col in mat.T:
	for index in range(0, len(col)-3):
		theMax = max(theMax, calc4prod(col[index:index+4]))

print theMax
