#!/usr/bin/python


tot = 0
for i in xrange(1,100):
	nNumbers = 0
	j = 1
	while len(str(pow(j,i))) <= i:
		nNumbers += 1 if len(str(pow(j,i))) == i else 0
		j += 1
	print i, nNumbers
	tot += nNumbers
	i += 1

print "\t\t", tot
