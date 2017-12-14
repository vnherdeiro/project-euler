#! /usr/bin/python3

MAX_LENGTH = 100
#def countIncreasing( nDigits, lastDigit):
#	if nDigits > MAX_LENGTH:
#		return 0
#	count = 0
#	for i in range(lastDigit,10):
#		count += 1
#		count += countIncreasing( nDigits + 1, i)
#	return count
#
#
#s = 0
#for i in range(10):
#	s += countIncreasing(1,i)
#print( s)


#dynamical programming solution

#increasing
dicInc = { (1,i) : 1 for i in range(1,10)}

for digit in range(2,MAX_LENGTH+1):
	for j in range(1,10):
		s = 0
		for k in range(j,10):
			s += dicInc[ (digit-1,k)]
		dicInc[ (digit,j)] = s

#print( sum( dic.values())*2 - MAX_LENGTH*9)
#print( sum( dic.values()))

#decreasing
dicDec = { (1,i) : 1 for i in range(0,10)}

for digit in range(2,MAX_LENGTH+1):
	for j in range(0,10):
		s = 0
		for k in range(0,j+1):
			s += dicDec[ (digit-1,k)]
		dicDec[ (digit,j)] = s

#removing the overcounting of the constant numbers
print( sum( dicInc.values()) + sum( dicDec.values()) - MAX_LENGTH*10)
