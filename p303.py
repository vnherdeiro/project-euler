#! /usr/bin/python

class Memoize:
	def __init__(self, f):
		self.f = f
		self.memo = {}
	def __call__(self, *args):
		if not args in self.memo:
			self.memo[args] = self.f(*args)
		return self.memo[args]

# @Memoize
def inc(n):
	numberString = ""
	while n != 0:
		numberString += str( n%3)
		n /= 3
	return int( numberString[::-1])

def f(n):
	i = 1
	while True:
		f = inc(i)
		if f % n == 0:
			break
		else:
			i += 1
	return f

def correctDigits(n):
	while n != 0:
		lastDig = n % 10
		if lastDig != 0 and lastDig != 1 and lastDig !=2:
			return False
		n /= 10
	return True

def f2(n):
	number = n
	while True:
		if correctDigits(number):
			return number
		else:
			number += n


s = 0
for i in xrange(9900,10001):
	s += f2(i)/i
	if i % 100 == 0:
		print i

print s
