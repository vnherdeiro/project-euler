#! /usr/bin/python

def sumXOR(l1,l2):
	s = 0
	for it1,it2 in zip(l1,l2):
		s += it1 != it2 #XOR operation
	return s

numbersDic = {  0 : (1,1,1,0,1,1,1),
				1 : (0,0,1,0,0,1,0),
				2 : (1,0,1,1,1,0,1),
				3 : (1,0,1,1,0,1,1),
				4 : (0,1,1,1,0,1,0),
				5 : (1,1,0,1,0,1,1),
				6 : (1,1,0,1,1,1,1),
				7 : (1,1,1,0,0,1,0),
				8 : (1,1,1,1,1,1,1),
				9 : (1,1,1,1,0,1,1)}

nBars = {}
for i in xrange(10):
	nBars[i] = sum(numbersDic[i])


#dictionnary storing the number of transitions
transitions = {}
for i in xrange(10):
	for j in xrange(10):
		transitions[ i,j] = sumXOR(numbersDic[i],numbersDic[j])


infile = "primes315.dat"
primes = [int(x) for x in open(infile)]

def iter(n):
	return sum( int(x) for x in str(n))


class SamClock():
	"""digital clock Sam style, clearing all number before drawing another one"""
	def __init__(self):
		self.Ntransitions = 0
		self.digits = []

	def draw(self, number): #draws and clear
		for n in str(number):
			self.Ntransitions += 2 * nBars[ int(n)] #increases twice for drawing and clearing


class MaxClock():
	"""digital clock Max style, updates only necessary bars"""
	def __init__(self):
		self.Ntransitions = 0
		self.digits = []

	def draw(self, newNumber): #draws and clear
		newDigits = [int(x) for x in str(newNumber)]

		if not self.digits: #drawing first number
			for x in newDigits:
				self.Ntransitions += nBars[x]
		else: #updates number
			#clearing extra digits on the clock
			while len(newDigits) < len(self.digits):
				toDel = self.digits.pop(0)
				self.Ntransitions += nBars[ toDel]
					
			#updating left digits
			for i in xrange(len(newDigits)):
				self.Ntransitions += transitions[ self.digits[i], newDigits[i]]
		self.digits = newDigits[:]

	def clear(self): #clears the screen
		for n in self.digits:
			self.Ntransitions += nBars[n]
		self.digits = []


sClock = SamClock()
mClock = MaxClock()

for p in primes:
	n = p
	mClock.draw(n)
	sClock.draw(n)
	while True:
		n = iter(n)
		mClock.draw(n)
		sClock.draw(n)
		if n < 10:
			break
	mClock.clear()


print sClock.Ntransitions
print mClock.Ntransitions
print sClock.Ntransitions - mClock.Ntransitions
	



