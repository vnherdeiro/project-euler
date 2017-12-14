#! /usr/bin/python

infile = "p089_roman.txt"



def reduceRoman(theNumber):
	#reducing the "IIIII"
	theNumber = theNumber.replace("IIIII","V")
	theNumber = theNumber.replace("IIII","IV")
	theNumber = theNumber.replace("VV","X")
	theNumber = theNumber.replace("VIV","IX")
	theNumber = theNumber.replace("XXXXX","L")
	theNumber = theNumber.replace("XXXX","XL")
	theNumber = theNumber.replace("LL","C")
	theNumber = theNumber.replace("LXL","XC")
	theNumber = theNumber.replace("CCCCC","D")
	theNumber = theNumber.replace("CCCC","CD")
	theNumber = theNumber.replace("DD","M")
	theNumber = theNumber.replace("DCD","CM")
	return theNumber

saveSpace = 0
with open(infile) as f:
	for line in f:
		number = line.rstrip("\n")
		reduced = reduceRoman(number)
		print number,reduced
		saveSpace += len(number) - len(reduced)

print saveSpace
