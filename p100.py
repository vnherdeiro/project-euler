#! /usr/bin/python

#import numpy as np
import mpmath
from math import sqrt

mpmath.mp.dps = 100 #not much performing loss in 50->100

mptol = mpmath.mpf("1e-15")
def isIntmp(x):
	dep = abs(x - round(x))
	#print dep
	return dep < mptol

tol = 1e-10
def isInt(x):
	return abs(x - round(x)) < tol

k = 1015961000000

hasFound = False
while not hasFound:
	if isInt( .5*(3-2*k) + .5*sqrt(9-16*k + 8*k*k) ):
		if isIntmp( .5*mpmath.mpf(3-2*k) + .5*mpmath.sqrt(9-16*k + 8*k*k) ):
			hasFound = True
	if not hasFound:
		k += 1
	if k % 10000000 == 0:
		print k

print k
