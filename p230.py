#! /usr/bin/python


cycle = "abbababb"
#
# dic = {"a" : "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679", "b": "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"}
#
# def d(n):
# 	if n < 200:
# 		theCycle = "ab"[n/100]
# 	else:
# 		n -= 200
# 		cycleNumber = (n / 100) % 8
# 		theCycle = cycle[ cycleNumber]
# 	return dic[theCycle][n % 100]
#
#
# for n in xrange(0,18):
# 	print d( (127 + 19*n) * (7**n))
#
# print "".join( [d( (127 + 19*n) * (7**n)) for n in xrange(0,18)][::-1])
#
# print (dic["a"] + dic["b"])[127]

a = "a"
b = "b"
concat = "ab"

for i in xrange(30):
	a,b = b, a+b
	concat += b

print len(concat)
print concat[:2]
concat = concat[2:]
for i in xrange(10):
	print concat[i*8:(i+1)*8]

#print concat.replace(cycle,"m").replace("ababb","x").replace("mm","2").replace("m","1")

for j in xrange(100):
	c2 = concat[j:]
	for i in xrange(1,100):
		if c2[:i] == c2[i:2*i] and c2[:i] == c2[2*i:3*i] and c2[:i] == c2[3*i:4*i]:
			print j,i,c2[:i]

import re

REPEATER = re.compile(r"(.+?)\1+$")

def repeated(s):
	match = REPEATER.match(s)
	return match.group(1) if match else None

print repeated(concat)
