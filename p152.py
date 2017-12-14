#! /usr/bin/python

import fractions


fracTab = [fractions.Fraction(1,x)**2 for x in xrange(2,46)]
aHalf = fractions.Fraction(1,2)

def sums22(val, index):
	#print index
	count = 0
	addedValue = val + fracTab[index]
	if addedValue > aHalf:
		if index + 1 < len(fracTab):
			count += sums22(val,index+1)
	elif addedValue == aHalf:
		count += 1
		count += sums22(val,index+1) #not adding it
	elif index + 1 < len(fracTab):
		count += sums22(addedValue,index+1) #adding it
		count += sums22(val,index+1) #skipping it
	return count


print sums22(fractions.Fraction(0,1),0)
