#! /usr/bin/python

from itertools import permutations

round = lambda x : int(x+.5)

tol = 1e-5
def isCube(x):
	root = x**(1./3)
	return abs(root-round(root)) < tol
#
# print isCube(41063620)
# i = 41063620
#
# while True:
# 	listOfCube = []
# 	nDigits = len(str(i))
# 	for perm in permutations(str(i)):
# 		numberStr= "".join(perm)
# 		number = int(numberStr)
# 		if len(numberStr) == nDigits and isCube(number):
# 			listOfCube.append(number)
# 	listOfCube = set(listOfCube)
# 	if len(listOfCube) == 3:
# 		print listOfCube
# 		break


#new way storing the permutations

from collections import defaultdict

cubesPerPerm = defaultdict(int)

numbersDic = {}

i = 1

nPerm = 5
# while not nPerm in cubesPerPerm.values():
while True:
	cube = i**3
	digits = map(int, str(cube))
	digits = sorted(digits)
	orderedDigits = "".join( map(str, digits))
	cubesPerPerm[ orderedDigits] += 1
	if not orderedDigits in numbersDic:
		numbersDic[orderedDigits] = i
	if cubesPerPerm[ orderedDigits] == nPerm:
		break
	i += 1

for key, values in cubesPerPerm.items():
	if values == nPerm:
		thePerm = key

print numbersDic[ thePerm]**3

# theSet = set()
# for perm in permutations(thePerm):
# 	theNumb = int( "".join(perm))
# 	if isCube( theNumb):
# 		theSet.add(theNumb)
# 		#pass
# print sorted(list(theSet))
