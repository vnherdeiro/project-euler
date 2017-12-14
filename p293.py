#! /usr/bin/python3

with open("primesP50.dat","r") as f:
    primes = [int(line.rstrip("\n")) for lineNo, line in enumerate(f) if lineNo < 3402]
    
MAX = 10**9
adm = []
#need for recursion here
def gen(val, index, isMixed):
	#or we add this value again or the next prime
	if isMixed and val % 2 == 0:
		adm.append( val)
	multBySamePrime = val * primes[index]
	if multBySamePrime < MAX:
		gen( multBySamePrime, index, isMixed)
		if index + 1 < len(primes):
			multByNextPrime = val * primes[index+1]
			if multByNextPrime < MAX:
				gen( multByNextPrime, index+1, True)
			
for index,p in enumerate(primes):
	gen(p, index, False)

pow = 1
while 2**pow < MAX:
	adm.append( 2**pow)
	pow += 1
adm = list(set(adm))
adm = sorted(adm)
print( len( adm))
with open("p293_admissibles.dat","w") as f:
	for val in adm:
		f.write("%d\n" %val)
