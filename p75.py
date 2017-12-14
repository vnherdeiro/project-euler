#! /usr/bin/python


def solCounter(n):
	a = n/3
	b = n/3
	nSol = 0
	while nSol <= 2 and a > 0 and b < n/2:
		print b, a
		if 2*a*b + n*n == 2*(a+b)*n:
			nSol += 1
		a -= 1
		b += 1
	return nSol == 1


print solCounter(24)
