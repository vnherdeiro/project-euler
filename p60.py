#!/usr/bin/python

infile = "primesP50.dat"
primes = [int(x) for x in open(infile)]


def isPrime(x):
	for prime in primes:
		if prime >= x:
			break
		if x % prime == 0:
			return False
	return True

def checkConcat(p1,p2):
	return isPrime( int( str(p1)+str(p2))) and isPrime( int( str(p2) + str(p1)))


#adding to 3, 7, 109, 673

#act = (3,7,109,673)
#for p in primes:
#	if p not in act:
#		print p
#		working = True
#		for p2 in act:
#			working &= checkConcat(p,p2)
#		if working:
#			print "\t\t",p

primesPool = primes[:2000]

lMax = len(primesPool)
for p1 in xrange(1,lMax):
	act = [primesPool[p1]]
	for p2 in xrange(p1+1, lMax):
		if checkConcat(primesPool[p1],primesPool[p2]):
			act.append(primesPool[p2])
			for p3 in xrange(p2+1,lMax):
				if checkConcat( primesPool[p1], primesPool[p3]) and checkConcat( primesPool[p2], primesPool[p3]):
					print p1, p2, p3
					act.append(primesPool[p3])
					for p4 in xrange(p3+1,lMax):
						if checkConcat( primesPool[p1], primesPool[p4]) and checkConcat( primesPool[p2], primesPool[p4]) and checkConcat( primesPool[p3], primesPool[p4]):
							print p1, p2, p3, p4
							act.append(primesPool[p4])
							for p5 in xrange(p4+1, lMax):
								if checkConcat( primesPool[p1], primesPool[p5]) and checkConcat( primesPool[p2], primesPool[p5]) and checkConcat( primesPool[p3], primesPool[p5]) and checkConcat(primesPool[p4], primesPool[p5]):
									print "\t\t",primesPool[p1], primesPool[p2], primesPool[p3], primesPool[p4], primesPool[p5]
				
