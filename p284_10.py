#! /usr/bin/python3

def theFilter( n):
	s = str(n)
	s2 = str(n*n)
	return s == s2[-len(s):]


#for i in filter( theFilter, range(1,1000000000)):
#	if i % 10 == 5:
#		print( i, i**2)


theSeeds = list( filter( theFilter, range(2,11)))


MAX_LENGTH = 10000
steadys = [1] #trivial solution included

def iterate( n):
	l = len( str(n))
	if l > MAX_LENGTH:
		return
	for i in range(1,10):
		newNumber = i * 10**l + n
		if theFilter( newNumber):
			steadys.append( newNumber)
			print( newNumber)
		iterate( newNumber)

def iterateV2( n):
	if len( str(n)) > MAX_LENGTH:
		return
	n2 = n*n
	n2String = str(n2)
	index = 0
	while index < len(n2String):
		newNumber = int( n2String[index:])
		if theFilter( newNumber) and newNumber not in steadys: 
			steadys.append( newNumber)
			iterateV2( newNumber)
			#break
		index += 1
		

for s in theSeeds:
	iterateV2(s)

assert all( theFilter(x) for x in steadys), "wrong solutions collected"
print( sorted(steadys))
	
