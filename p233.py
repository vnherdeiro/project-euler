#! /usr/bin/python3

from sys import argv

tot = 0
for N in range(1,10000):
	N2 = N*N
	x = N
	y = 0
	Nsol = 0
	while x > 0:
		x -= 1
		while x*x + (y+1)*(y+1) <= N2:
			y += 1
			if x*x + y*y == N2:
				Nsol += 1

	if Nsol == 105:
		tot += 1
print( tot)
