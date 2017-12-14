#! /usr/bin/python3

import numpy as np
from re import sub
#from functools import lru_cache

def pprintTab( someTab):
	print( "-" * 150)
	print( sub("[\[\]]"," ",np.array_str(someTab)))
	print( "-" * 150)

np.set_printoptions( linewidth=220)

SIZE = 1000

tab = np.arange( 0, SIZE**2, dtype=int).reshape((SIZE,SIZE))
tab += 1
isSquare = np.zeros( tab.shape, dtype=bool)

for val in range(1, SIZE+1):
	sq = val**2
	sq -= 1
	isSquare[sq//SIZE][sq%SIZE] = True

#print( tab)
#print( isSquare)


#returns the number of neighbours of a case
#@lru_cache(maxsize=None)
def Nnei( i, j):
	N = 0
	if j >= 1:
		N += 1
	if j <= SIZE - 2:
		N += 1
	if i >= 1:
		N += 1
	if i <= SIZE - 2:
		N += 1
	return N

nNeiTab = np.zeros( (SIZE,SIZE), dtype=int)
for i, row in enumerate(nNeiTab):
	for j, _ in enumerate(row):
		nNeiTab[i,j] = Nnei(i,j)
#print nNeiTab

#fluxTab = np.zeros( (SIZE,SIZE))
#for i, row in enumerate(fluxTab):
#	for j, _ in enumerate(row):
#		fluxTab[i][j] = 1./Nnei(i,j)
#fluxTab /= fluxTab.sum()
#print (fluxTab*isSquare).sum()


probTab = np.ones( (SIZE,SIZE))
probTab /= probTab.sum()

#solving by iterating
#using strategy 2
Niter = 10000
#checkboard updates
offset = 0
SIZE_2 = SIZE*SIZE

def letsQuit( theTab): #exits when the four corners have very close values
	theVals = (theTab[0,-1], theTab[0,0], theTab[-1,-1], theTab[-1,0])
	maxDist = max( theVals) - min( theVals)
	print( maxDist)
	return 0. < maxDist < 1e-13


#for t in range( Niter):
#while True:
##while not letsQuit( probTab):
#	#picking points at random here
#	lOffset = offset
#	for i in range(SIZE):
#		for j in range(lOffset, SIZE, 2):
#			den = .5
#			num = 0
#			#summing over neighbours
#			if i > 0:
#				num += probTab[i-1,j]/(2*nNeiTab[i-1,j])
#			if i < SIZE-1:
#				num += probTab[i+1,j]/(2*nNeiTab[i+1,j])
#			if j > 0:
#				num += probTab[i,j-1]/(2*nNeiTab[i,j-1])
#			if j < SIZE-1:
#				num += probTab[i,j+1]/(2*nNeiTab[i,j+1])
#			probTab[i,j] = num/den
#		lOffset += 1
#		lOffset %= 2
#	probTab /= probTab.sum()
#	offset += 1
#	offset %= 2
#	#adding averaging of the three types: corners, borders and inside
#	avgInside = probTab[1:-1,1:-1].mean()
#	probTab[1:-1,1:-1] = avgInside
#	avgBorder = np.r_[ probTab[1:-1,0], probTab[1:-1,-1], probTab[0,1:-1], probTab[-1,1:-1]].mean()
#	probTab[1:-1,0] = avgBorder
#	probTab[1:-1,-1] = avgBorder
#	probTab[0,1:-1] = avgBorder
#	probTab[-1,1:-1] = avgBorder
#	avgCorners = np.mean( (probTab[0,0], probTab[0,-1], probTab[-1,0], probTab[-1,-1]))
#	probTab[0,0] = avgCorners
#	probTab[0,-1] = avgCorners
#	probTab[-1,0] = avgCorners
#	probTab[-1,-1] = avgCorners
#	print((probTab*isSquare).sum())

#pprintTab(probTab)


sol = (probTab*isSquare).sum()

probTab = np.ones( (SIZE,SIZE))
probTab /= probTab.sum()
#using strategy 1
resTab = np.asfortranarray(1./(1+nNeiTab)) #should be faster in fortran ordering
#for t in range( Niter):
while True:
#while not letsQuit( probTab):
	#picking points at random here
	lOffset = offset
	tempTab = probTab * resTab
	for i in range(SIZE):
		for j in range(lOffset,SIZE,2):
			Nneigh = nNeiTab[i,j]
			den = Nneigh*(1./(1+Nneigh))
			num = 0
			#summing over neighbours
			if i > 0:
				num += tempTab[i-1,j]
			if i < SIZE-1:
				num += tempTab[i+1,j]
			if j > 0:
				num += tempTab[i,j-1] 
			if j < SIZE-1:
				num += tempTab[i,j+1]
			probTab[i,j] = num/den
		lOffset += 1
		lOffset %= 2
	probTab /= probTab.sum()
	offset += 1
	offset %= 2
	#adding averaging of the three types: corners, borders and inside
	avgInside = probTab[1:-1,1:-1].mean()
	probTab[1:-1,1:-1] = avgInside
	avgBorder = np.r_[ probTab[1:-1,0], probTab[1:-1,-1], probTab[0,1:-1], probTab[-1,1:-1]].mean()
	probTab[1:-1,0] = avgBorder
	probTab[1:-1,-1] = avgBorder
	probTab[0,1:-1] = avgBorder
	probTab[-1,1:-1] = avgBorder
	avgCorners = np.mean( (probTab[0,0], probTab[0,-1], probTab[-1,0], probTab[-1,-1]))
	probTab[0,0] = avgCorners
	probTab[0,-1] = avgCorners
	probTab[-1,0] = avgCorners
	probTab[-1,-1] = avgCorners
	print((probTab*isSquare).sum())

#pprintTab(probTab)
#print (probTab*isSquare).sum()
sol += (probTab*isSquare).sum()
print("%.12f" %(sol/2))
#print (probTab*isSquare).sum()
#implement the checkboard method

