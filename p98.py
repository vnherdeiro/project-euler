#!/usr/bin/python

from collections import defaultdict
import re
theDict = defaultdict(list)


squareTab = [x**2 for x in xrange(1,10000)]

infile = "p098_words.txt"
dat = open(infile).read()
words = re.findall("\w+",dat)
words = [w.lower() for w in words]

for w in words:
	theDict[ tuple(sorted([x for x in w]))].append(w)

theMax = 0
for key, w in theDict.items():
	if len(w) == 2:
		word1, word2 = w
		lSquareTab = filter(lambda x : len( str(x)) == len( word1), squareTab)
		for square in lSquareTab:
			square = str(square)
			dic = {}
			for index, letter in enumerate( word1):
				dic[letter] = square[index]
			if len( set(dic.values())) != len(dic.keys()):
				pass
			else:
				number = "".join([dic[letter] for letter in word2])
				number = int(number)
				if number in lSquareTab:
					#print square, number, word1, word2, dic
					theMax = max(theMax, number, int(square))
print "\t\t\t", theMax
