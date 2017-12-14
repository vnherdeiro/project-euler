#! /usr/bin/python3

import numpy as np
import functools


@functools.lru_cache(maxsize=None)
def s(k):
	if k <= 55:
		return (100003 - 200003*k + 300007*k*k*k) % 1000000 - 500000
	else:
		return (s(k-24) + s(k-55) + 1000000) % 1000000 - 500000


tab = [s(k) for k in range(1,2000**2 +1)]
tab = np.array(tab, dtype=np.int32)
tab = np.resize(tab, (2000,2000))

MAX = 0
#checking max by rows
print( "doing rows")
for row in tab:
	for i in range(0,2000):
		c = max(np.cumsum( row[i:]))
		MAX = max( c, MAX)

print( "doing cols")
tab2 = tab.T.copy()
#checking cols
for row in tab2:
	for i in range(2000):
		c = max(np.cumsum( row[i:]))
		MAX = max( c, MAX)

#checking diagonals
print( "doing diag")
for ind in range(-1999,2000):
	d = np.diagonal(tab, ind)
	for i in range( len(d)):
		c = max( np.cumsum( d[i:]))
		MAX = max(c, MAX) 

print( "doing adiag")
#checking antidiagonals
tab2 = np.flipud(tab).copy()
for ind in range(-1999,2000):
	d = np.diagonal(tab2, ind)
	for i in range( len(d)):
		c = max( np.cumsum( d[i:]))
		MAX = max(c, MAX) 
print( MAX)
