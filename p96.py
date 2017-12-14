#! /usr/bin/python

import numpy as np
from random import choice
from copy import deepcopy


class Sudoku():
	"""class handling and, possibly solving, a grid of sudoku"""
	def __init__(self, gridAsLists):
		self.grid = np.array(gridAsLists,dtype=int).reshape( (9,9))
		self.naiveAttributions() #storing the naie attributions once and for all
		self.initial = self.grid.copy()

	def inCase(self,i,j): #looks for the values in the square 3x3 of some grid location
		 return self.grid[ (i/3)*3 : (i/3 + 1)*3, (j/3)*3 : (j/3 + 1)*3].flatten()

	def possibles(self,i,j):
		return [x for x in range(1,10) if x not in np.unique(np.r_[self.inCase(i,j), self.grid[i,:],self.grid[:,j]])]

	def naiveAttributions(self): #checks for and makes obvious attributions when only one possible solution at a location
		hasBeenUpdated = True
		while hasBeenUpdated:
			hasBeenUpdated = False
			for i in xrange(9):
				for j in xrange(9):
					if self.grid[i,j] == 0:
						possibles = self.possibles(i,j)
						if len(possibles) == 1:
							self.grid[i,j] = possibles[0]
							hasBeenUpdated = True

	def checkCoherence(self): #checks that the sudoku grid is not wrong by having duplicated values in a row or col or 3x3-square
		for row in self.grid:
			rowNotZero = row[row>0]
			if np.unique(rowNotZero).size < rowNotZero.size:
				return False
		for col in self.grid.T:
			colNotZero = col[col>0]
			if np.unique(colNotZero).size < colNotZero.size:
				return False
		for i in xrange(0,9,3):
			for j in xrange(0,9,3):
				square = self.inCase(i,j)
				squareNotZero = square[ square>0]
				if np.unique(squareNotZero).size <  squareNotZero.size:
					return False
		return True

	def isSolved(self): #checks if the grid has been solved...
		if 0 not in self.grid.flatten():
			return True
		else:
			return False

	def solve(self):
		solved = False
		while not self.isSolved():
			self.naiveAttributions()
			#print self.grid
			#if not self.checkCoherence():
				#print "clearing everything"
				#self.grid = self.initial.copy()
				#continue
			if not self.isSolved():
				#print "taking guess"
				self.takeGuess()
			#raw_input()

	def takeGuess(self): #here we make a trial on some case
		minPossibles = 999
		minPossibleChoices = []
		for i in xrange(9):
			for j in xrange(9):
				if self.grid[i,j] == 0:
					possibles = self.possibles(i,j)
					if len(possibles) < minPossibles:
						minI = i
						minJ = j
						minPossibleChoices = possibles[:]
						minPossibles = len(possibles)
		if not minPossibleChoices:
			#print "clearing"
			self.grid = self.initial.copy()
			return
		theGuess = choice( minPossibleChoices) #taking guesses at random
		self.grid[ minI, minJ] = theGuess
		#print minI,minJ,theGuess
		#print self.grid


infile = "p096_sudoku.txt"


theSum = 0
with open(infile, "r") as f:
	while f.readline() != "":
		lines = [ f.readline().rstrip("\n") for i in xrange(9)]
		lines = [ int(x) for l in lines for x in l]
		theSudoku = Sudoku(lines)
		#theSudoku.solve()


		if theSudoku.isSolved():
			print "solved"
		else:
			print "not solved"
		#print theSudoku.grid
		theSum += theSudoku.grid[0,0:3].sum()
		print theSum

		#raw_input()
#use threads to send different possibles outcome and only return if valid sudoku
