#! /usr/bin/python3

def rightRotate( n):
	s = str(n)
	return int( s[-1] + s[:-1])

if __name__ == "__main__":
	i = 11
	while True:
		r = rightRotate(i)
		if r % i == 0 and r != i:
			print( i, r//i)
			s = str(i)
			while len(s) <= 100:
				s = s + str(i)
				n = int(s)
				if rightRotate(n) % n != 0:
					print( i, "\tnot motif")
		i += 1
