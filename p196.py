#! /usr/bin/python3

from sys import argv
from re import findall

infile = argv[1]
with open(infile,"r") as f:
	content = f.read()
dic = {}
for point in findall("(\d+)\, (\d+)\, (\d+)",content):
	i,j,p = map(int, point)
	dic[ i,j] = p
mean = lambda x : sum(x)//len(x)
midRow = mean( set(map( lambda x : x[0],dic.keys())))
print( midRow)
#looking for triplets
setPrimes = set()
def neighbours(i,j):
	neigh = []
	for delta_i in (-1,0,1):
		for delta_j in (-1,0,1):
				if (i+delta_i,j+delta_j) in dic:
					neigh.append( (i+delta_i,j+delta_j))
	return neigh


for i,j in dic.keys():
	neigh = neighbours(i,j)
	if len(neigh) >= 3:
		for I,J in neigh:
			if I == midRow:
				setPrimes.add( dic[I,J])

print(sum(setPrimes))
