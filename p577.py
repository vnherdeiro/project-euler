#! /usr/bin/python3

def h(n):
	s = 0
	for i in range(n+2):
		for j in range( i+1):
			s += (0<i<n+1) and (0<j<i+1)
	return s


print( list( map( h, (3,6,20))))
