#! /usr/bin/python3

from math import sqrt
from mpmath import mp

mp.dps = 50
shift = mp.mpf(".5")
round = lambda x : int(x+shift)
tol = mp.mpf("1e-15")
isInt = lambda x : abs( x-round(x)) < tol

a = 5
while True:
	
	AreaPlus = (a+1) * mp.sqrt((3*a+1)*(a-1))/4
	if isInt(AreaPlus):
		print( a, mp.sqrt(3*a+1), mp.sqrt(a-1))
	if a**2 % (a-1)**2 == 0:
		AreaMinus = (a-1) * mp.sqrt((3*a-1)*(a+1))/4
		if isInt(AreaMinus):
			print( "\t",a, mp.sqrt(3*a-1),mp.sqrt(a+1))
	a += 1
