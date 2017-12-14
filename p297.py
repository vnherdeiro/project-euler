#! /usr/bin/python

MAX = 10**17

fib = [1, 2]
while True:
	nextValue = sum( fib[-2:])
	if nextValue >= MAX:
		break
	fib.append( nextValue)

print len(fib)
#print fib

def z(sumValue,zValue,theList):
	count = zValue
	if theList:
		for index in xrange(len(theList)):
			if sumValue + theList[index] < MAX:
				count += z(sumValue+ theList[index], zValue+1, theList[index+2:])
			else:
				break
	return count

print z(0, 0, fib)
