#! /usr/bin/python3

MAX = 2323218950681478446587180516177954549

with open("primes266.dat","r") as f:
	primes = [int( line.rstrip("\n")) for line in f]

theMax = 0
def calcProds( val, index):
	if val > MAX:
		return
	newVal = val * primes[index]
	if newVal <= MAX:
		global theMax
		if newVal > theMax:
			theMax = newVal
			print( theMax, "\t",theMax % 10**16)
		if index + 1 < len(primes):
			calcProds(newVal, index+1)	
	if index + 1 < len(primes):
		calcProds(val, index+1)


calcProds(1,0)
