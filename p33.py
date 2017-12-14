#! /usr/bin/python

#project euler problem 33

from fractions import Fraction

for i in range(10,100):
	d11 = i/10
	d12 = i%10
	for j in range(i+1,100):
		d21 = j/10
		d22 = j%10
		if d22 == d12 and d21 != 0 and d12 != 0:
			newFrac = Fraction(d11,d21)
			if newFrac == Fraction(i,j):
				print i,j
		if d22 == d11 and d21 != 0 and d12 != 0:
			newFrac = Fraction(d12,d21)
			if newFrac == Fraction(i,j):
				print i,j
		if d21 == d11 and d22 != 0:
			newFrac = Fraction(d12,d22)
			if newFrac == Fraction(i,j):
				print i,j
		if d21 == d12 and d22 != 0:
			newFrac = Fraction(d11,d22)
			if newFrac == Fraction(i,j):
				print i,j
