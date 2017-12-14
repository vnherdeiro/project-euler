#! /usr/bin/python


def isPentagital(n):
	if "0" in n:
		return False
	if len(n) != 9:
		return False
	if len(set( n)) != 9:
		return False
	return True


theMax =  0

for i in xrange(1,100000):
	concat = str(i)
	n = 2
	while len(concat) < 9:
		concat += str(i*n)
		n += 1
	if isPentagital(concat):
		theMax = int(concat)
		print i, theMax
