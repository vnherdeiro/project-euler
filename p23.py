#! /usr/bin/python

def properDivisors(n):
	return [i for i in xrange(1,n/2+1) if n%i == 0]

#calculating the abundant numbers
abundantNumbers = [n for n in xrange(1,28123) if sum(properDivisors(n)) > n]


#calculated the sum
notWrittableList = []
for i in xrange(1,28123):
	pool = set(filter( lambda x : x <= i-abundantNumbers[0], abundantNumbers))
	isWrittable = False
	for n1 in pool:
		if i - n1 in pool:
			isWrittable = True
			break
	if not isWrittable:
		print i
		notWrittableList.append( i)

print notWrittableList
print sum(notWrittableList)
