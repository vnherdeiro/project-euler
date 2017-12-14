#! /usr/bin/python3

from mpmath import mp
pow = mp.power
binom = mp.binomial
from scipy.optimize import minimize

thresh = 10**9
def g(f):
	mp.dps = 400
	if f <= 0 or f >= 1: #forcing minimization in (0,1)
		return 0
	f = mp.mpf( f[-1])
	#print( f)
	s = mp.mpf()
	for k in range(1001):
		gain = pow(1+2*f, k) * pow(1-f, 1000 - k)
		if gain > thresh:
			s += binom(1000, k)
			#print(binom(1000, k))
	#print( s)
	s /= pow(2,1000)
	return -s

output = minimize( g, .05, method="Powell", tol=1e-14,)
print( output)

#print( "%.15f" % g(0.05))
