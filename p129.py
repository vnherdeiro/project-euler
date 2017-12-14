#! /usr/bin/python

def A(n):
	rest = 1
	k = 10
	i = 1
	while rest != 0:
		rest += k
		rest %= n
		k *= 10
		i += 1
	return i

MIN = 1000000
a = 1
i = 3
while a < MIN:
	if i % 2 != 0 and i % 5 != 0:
	 	a = A(i)
		print i, a
	i += 1

print i - 1
