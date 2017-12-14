#! /usr/bin/python3

from fractions import gcd

with open( "P233_NULL.dat") as f:
	NULLSET = [int(x.rstrip("\n")) for x in f]
with open( "P233_GROW1.dat") as f:
	GROW1 = [int(x.rstrip("\n")) for x in f]
with open( "P233_GROW2.dat") as f:
	GROW2 = [int(x.rstrip("\n")) for x in f]
GROW2 = map( lambda x : x*x, GROW2)
with open( "P233_GROW3.dat") as f:
	GROW3 = [int(x.rstrip("\n")) for x in f]
GROW3 = map( lambda x : x*x*x, GROW3)

#print("done reading...")

MAX = 10**11

s = 0

for el_grow1 in GROW1:
	for el_grow2 in GROW2:
		if el_grow1 * el_grow2 > MAX:
			break
		if gcd(el_grow1, el_grow2) == 1:
			for el_grow3 in GROW3:
				if el_grow1 * el_grow2 * el_grow3 > MAX:
					break
				if gcd(el_grow3,el_grow2) == 1 and gcd( el_grow1, el_grow3) == 1:
					for el_null in NULLSET:
						if el_grow1 * el_grow2 * el_grow3 * el_null> MAX:
							break
						#print(el_grow1 , el_grow2 , el_grow3 , el_null ,el_grow1 * el_grow2 * el_grow3 * el_null)
						print(el_grow1 * el_grow2 * el_grow3 * el_null)
						s += el_grow1 * el_grow2 * el_grow3 * el_null
						
						
#print( s)
			
