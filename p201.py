#! /usr/bin/python3

from itertools import combinations
from sys import argv

theList = [x**2 for x in range(1,101)]


def genPair():
	for index_a, a in enumerate(theList):
		for b in theList[index_a+1:]:
			yield a,b

SIZE_A, SIZE_B = map(int, argv[1:3])
SIZE_TOT = SIZE_A + SIZE_B


genA = combinations( theList, SIZE_A)
for combiA in genA:
	genB = combinations( theList, SIZE_B)
	for combiB in genB:
		#print(combiA, combiB)
		if len(set( combiA + combiB)) == SIZE_TOT and sum(combiA) == sum(combiB):
		#if not [x for x in combiA if x not in combiB] and sum(combiA) == sum(combiB):
			print(combiA, combiB)
 
