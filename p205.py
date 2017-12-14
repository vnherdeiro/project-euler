#! /usr/bin/python

import numpy as np


s = 0
card = 0

batch = 10000000
while True:
	peter = np.random.randint(1,5,size=(batch,9)).sum(axis=1)
	colin = np.random.randint(1,7,size=(batch,6)).sum(axis=1)
	s += (peter > colin).sum()
	card += batch
	print "%.8f" % (float(s)/card)
	
