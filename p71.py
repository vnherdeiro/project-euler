#!/usr/bin/python


import fractions

closest = fractions.Fraction(0,1)
upperBound = fractions.Fraction(3,7)

for d in xrange(2,1000000):
	for n in xrange(int( d * closest),int(d*3./7+1)):
		theFrac = fractions.Fraction(n,d)
		if theFrac < upperBound:
			if fractions.gcd(n,d) ==1 and theFrac > closest:
				closest = theFrac
		else:
			break

print closest
