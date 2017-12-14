#! /usr/bin/python3

from fractions import Fraction


f13 = Fraction(1,3)
f23 = Fraction(2,3)
f1_500 = Fraction(1,500)

sequence = "PPPPNNPPPNPPNPN"


isPrimes = [True] * 500
isPrimes[0] = False #1 is not prime
for val in range(2, 501):
	n = val*2
	while n <= 500:
		isPrimes[n-1] = False
		n += val


for i, isPrime in enumerate( isPrimes):
	print( i+1, isPrime)


#checking for every starting position
probability = Fraction(0,1)
for pos in range

