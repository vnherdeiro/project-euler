#! /usr/bin/python

def isPalindrome(n): #check if number is palindrome
	return str(n) == str(n)[::-1]

def reverseNumber(n):
	return int( str(n)[::-1])

Niterations = 50
def isLychrel(n):
	itIndex = 1
	n += reverseNumber(n)
	while(not isPalindrome(n) and itIndex < Niterations):
		n += reverseNumber(n)
		itIndex += 1
	return isPalindrome(n)

upperBound = 10000


print sum( not isLychrel(i) for i in xrange(1,upperBound))
