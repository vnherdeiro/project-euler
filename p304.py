#! /usr/bin/python3

import numpy as np

MOD = 1234567891011

T = np.array( [[1,1],[1,0]], dtype="object")

def calcPower(theMatrix, n):
	if n == 1:
		return T
	else:
		m = calcPower(theMatrix,n//2)
		m = m % MOD
		if n % 2 == 0:
			return np.dot(m,m) % MOD
		else:
			return np.dot(T,np.dot(m,m) % MOD)
	

def calcFib(n):
	m = calcPower(T, n)
	_, fibn = np.dot(m,np.array([1,0],dtype="object"))
	return fibn

infile = "primes304.dat"

with open(infile,"r") as f:
	primes = [int(line.rstrip("\n")) for line in f]

values = map( calcFib, primes)

print( sum(values) % MOD)
	
