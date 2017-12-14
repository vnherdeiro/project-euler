#! /usr/bin/python

#checks for non divisibility in tribonacci sequence

def check(n):  #coulb be infinite if (1,1,1) not part of the cycle
	a,b,c = 1, 1, 3 % n
	while c != 0 and (a,b,c) != (1,1,1):
		a,b,c = b, c, (a+b+c) %n
	if c == 0:
		return False
	if (a,b,c) == (1,1,1):
		return True


i = 3
count = 0
while i < 10000:
	if check(i):
		count += 1
		if count == 124:
			print i
			break
	#print "done ", i
	i += 2
