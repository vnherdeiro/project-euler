#! /usr/bin/python3

from collections import defaultdict
from copy import deepcopy
from itertools import islice

theDic = {1:0}
for x in range(2,201):
	theDic[x] = 999

combiDic = { x : () for x in range(1,201)}


hasChanged = True
while hasChanged:
	#print( "loop")
	hasChanged = False
	newDic = deepcopy( theDic)
	for index1, val1 in enumerate(theDic.keys()):
		for val2 in theDic.keys():
			#print( "\t\t",val1, val2)
			newVal = val1 + val2
			#print( val1, val2, newVal)
			if newVal <= 200:
				newCombi = combiDic[val1] + combiDic[val2]
				newCombi = set( newCombi)
				newCombi.add( (val1,val2))
				nOp = len(newCombi)
				if theDic[ newVal] > nOp:
					#print( newVal, nOp)
					newDic[ newVal] = nOp
					combiDic[ newVal] = tuple(newCombi)
					hasChanged = True
	theDic = newDic

#print (theDic)
#print( combiDic[15])
#print( sum( theDic.values()))
for entry, val in theDic.items():
	print( entry, val)



			
	
#need to store more information...

