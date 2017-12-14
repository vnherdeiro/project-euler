#! /usr/bin/python
from itertools import permutations
import sys
infile = "p079_keylog.txt"

with open(infile) as f:
	dat = [line.rstrip("\n") for line in f]

#finding total atoms

setAtoms = set()

for line in dat:
	setAtoms |= set(line)

atoms = list(setAtoms)

for perm in permutations(atoms):
	isWorking = True
	lineIndex = 0
	while isWorking and lineIndex < len(dat):
		pos1 = perm.index(dat[lineIndex][0])
		pos2 = perm.index(dat[lineIndex][1])
		pos3 = perm.index(dat[lineIndex][2])
		isWorking &= pos1 < pos2 < pos3
		lineIndex += 1
	if isWorking:
		print "".join(perm)
		sys.exit()
