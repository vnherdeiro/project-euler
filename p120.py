#! /usr/bin/python



#simplified the expression by hand, =2 for n even, = 2na for n odd
def rmax(a):
	return max([2] + [2*n*a% a**2 for n in xrange(1,a)])


print sum( rmax(a) for a in xrange(3, 1001))
