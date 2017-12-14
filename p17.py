#! /usr/bin/python

from sys import argv


theDic= {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",
12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",
30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}


def spellNumber(n):
	if n == 1000:
		return "onethousand"
	str = ""
	if n >= 100:
		str += theDic[n/100] + "hundred"
		n  %= 100
		if n !=0:
			str += "and"
	if n > 20:
		str += theDic[n - n%10]
		if n%10 != 0:
			str += theDic[n%10]
	elif n != 0  or str == "":
		str += theDic[n]
	return str

txt = spellNumber(int(argv[1]))
print txt, len(txt)

print sum(len(spellNumber(n)) for n in xrange(1,1001))

for i in xrange(1,1001):
	text = spellNumber(i)
	#print i, text, len(text)
