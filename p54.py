#! /usr/bin/python

from collections import Counter

infile = "p054_poker.txt"

with open(infile,"r") as f:
	dat = f.readlines()

hands = [ (x.split()[:5], x.split()[5:]) for x in dat]

cardValue = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J": 10, "Q":11, "K":12, "A":13}

def readHandValue(theHand):
	sameSuit = len( set( card[1] for card in theHand)) == 1
	valuesInHand = sorted([cardValue[card[0]] for card in theHand])
	handsCounter = Counter(valuesInHand)
	totalVal = sum( valuesInHand)
	differences = [valuesInHand[i+1] - valuesInHand[i] for i in range(len(valuesInHand)-1)]
	maxVal = valuesInHand[-1]
	if sameSuit:
		if totalVal== 45:
			return (1, cardValue["A"], cardValue["A"]) #royal flush
		#checking if straigh flush -- four cards following
		if differences == [1,1,1,1]:
			return (2, maxVal, maxVal)
	if 4 in handsCounter.values(): #four cards of the same valuesInHand
		return (3, valuesInHand[2], maxVal) #the mid value has to be the most common one
	if 3 in handsCounter.values() and 2 in handsCounter.values():
		for card, frequency in handsCounter.items(): #searching the card kind in the triplet -- middle value should word as well
			if frequency == 3:
				triplet = card
		return (4, triplet, maxVal)
	if sameSuit: #all cards of same suit
		return (5, maxVal, maxVal)
	if differences == [1,1,1,1]:
		return (5, maxVal, maxVal)
	if 3 in handsCounter.values():
		for card, frequency in handsCounter.items(): #searching the card kind in the triplet -- middle value should word as well
			if frequency == 3:
				triplet = card
		return (6, triplet, maxVal)
	if handsCounter.values().count(2) == 2:
		maxPair = 0
		for card, frequency in handsCounter.items(): #retrieve max value of a pair
			if frequency == 2:
				maxPair = max(maxPair, card)
		return (7, maxPair, maxVal)
	if 2 in handsCounter.values():
		for card, frequency in handsCounter.items(): #searching the card kind in the triplet -- middle value should word as well
			if frequency == 2:
				double = card
		return (8, double, maxVal)
	return (9, maxVal, maxVal)

def compareVals( hand1, hand2): #return if hand1 > hand2
	value1 = readHandValue( hand1)
	value2 = readHandValue( hand2)
	if value1[0] < value2[0]: #better combination on player1
		return True
	if value1[0] > value2[0]: #better combination on player1
		return False
	#equal cobination - comparing their cards
	if value1[1] > value2[1]:
		return True
	if value1[1] < value2[1]:
		return False
	return value1[2] > value2[2] #highest cards decide here

theSum = 0
for h1, h2 in hands:
	#print h1, "\t\t", h2, "\t\t", compareVals(h1, h2)
	theSum += 1 if compareVals(h1,h2) else 0
print theSum
