#! /usr/bin/python

def sameDigits(n1, n2):
	return sorted( map(int, str(n1))) == sorted( map(int, str(n2)))

print sameDigits( 125874, 251748)



i = 1
hasFound = False

while not hasFound:
	if sameDigits(i, 2*i) and sameDigits(i, 3*i) and sameDigits(i, 4*i) and sameDigits(i, 5*i) and sameDigits(i, 6*i):
		print i
		hasFound = True
	i += 1
