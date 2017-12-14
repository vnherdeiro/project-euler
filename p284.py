#! /usr/bin/python3

from functools import reduce


def toBasis14(n):
	theDigits = []
	while n:
		dig = n % 14
		if dig < 10:
			theDigits.append( str(dig))
		elif dig == 10:
			theDigits.append( "a")
		elif dig == 11:
			theDigits.append( "b")
		elif dig == 12:
			theDigits.append( "c")
		elif dig == 13:
			theDigits.append( "d")
		n //= 14
	return "".join(theDigits[::-1])

def toBasis10( n):
	n = [int(dicReverse[i]) for i in n]
	return reduce( lambda x,y : 14*x + y, n)

#
#def inBasis14( n):
#	digits = toBasis14( n)
#	return "".join( digits)

#def theFilter(n):
#	basis14_n = toBasis14(n)
#	basis14_n2 = toBasis14(n*n)
#	return basis14_n == basis14_n2[-len(basis14_n):]

def theFilter( n_basis14):
	n_basis10 = toBasis10( n_basis14)
	n2 = n_basis10 * n_basis10
	n2_basis14 = toBasis14( n2)
	return n2_basis14[-len(n_basis14):] == n_basis14

dic = {10:"a", 11:"b", 12:"c", 13:"d"}
for i in range(10):
	dic[i] = str(i)

dicReverse = {val : entry for entry, val in dic.items()}


#by trial here, we find to different seeds
#but they also seem to require two different kinds of iterations to find all the solutions
seeds = ["7", "8"]
steadys = ["1"]
possibleIterates = list(map(str, range(10)))
possibleIterates = possibleIterates + ["a", "b", "c", "d"]
MAX_LENGTH = 9

def iterateFor8( n): #should work on the seed 8
	string_n = str(n)
	if len(string_n) > MAX_LENGTH:
		return
	for p in possibleIterates:
		newNumber = p + string_n
		if theFilter( newNumber) and newNumber not in steadys:
			steadys.append( newNumber)
			iterateFor8( newNumber)

def iterateFor7( n):
	if len( str(n)) > MAX_LENGTH:
		return
	n10 = toBasis10(n)
	n2 = toBasis14( n10*n10)
	n2String = n2
	index = 0
	while index < len(n2String):
		newNumber = int( n2String[index:])
		if theFilter( newNumber) and newNumber not in steadys: 
			steadys.append( newNumber)
			iterateFor7( newNumber)
			#break
		index += 1

#print( "".join(toBasis14(fromBasis14("c37")**2)))
#s = 0
#for n in filter( theFilter, range(1, 1000000000)):#fromBasis14("dddddddddddddd"))):
#	if inBasis14(n)[-1] == "8":
#		print( inBasis14(n), inBasis14(n*n))
#	if inBasis14(n)[-1] == "7":
#		print( "\t\t\t",inBasis14(n), inBasis14(n*n))
#	#for d in digits:
#	#	s += dicReverse[ d]
#print( s)
#print( "".join(toBasis14(s)))

iterateFor7( "7")
iterateFor8( "8")

#assert all( theFilter(x) for x in steadys), "wrong solutions collected"
print( sorted(steadys))


#eof
