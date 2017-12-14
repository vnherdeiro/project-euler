#! /usr/bin/python

from collections import defaultdict

dicPeter = defaultdict(int)
dicColin = defaultdict(int)

#peter choices
for p1 in xrange(1,5):
	for p2 in xrange(1,5):
		for p3 in xrange(1,5):
			for p4 in xrange(1,5):
				for p5 in xrange(1,5):
					for p6 in xrange(1,5):
						for p7 in xrange(1,5):
							for p8 in xrange(1,5):
								for p9 in xrange(1,5):
									s = p1 + p2 + p3 + p4 + p5 + p6 +p7+ p8+p9
									dicPeter[s] += 1

for c1 in xrange(1,7):
	for c2 in xrange(1,7):
		for c3 in xrange(1,7):
			for c4 in xrange(1,7):
				for c5 in xrange(1,7):
					for c6 in xrange(1,7):
						s = c1 + c2 + c3 + c4 + c5 +c6
						dicColin[s] += 1

card = 4**9 * 6**6
#card = sum(dicPeter.values()) * sum(dicColin.values())

prob = 0.
for valPeter, pPeter in dicPeter.items():
	for valColin, pColin in dicColin.items():
		if valPeter>valColin:
			prob += float(pPeter)*pColin/card

print "%.7f" %prob
