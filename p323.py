#! /usr/bin/python

import numpy as np

s = 0
card = 0
while True:
	x = 0
	MAX = 2**32
	count = 0
	while x != MAX-1:
		x = x | np.random.randint(0,MAX)
		count += 1

	s += count
	card += 1
	if card % 1000000 == 0:
		print float(s)/card
