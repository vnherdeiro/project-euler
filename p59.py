#!/usr/bin/python

from itertools import izip, cycle
import string

infile = "p059_cipher.txt"

inDat = open(infile).read()
characters = map(int,inDat.split(","))

def decypher(theText,thePassphrase): #theText already in ascii form
	thePassphrase = [ord(x) for x in thePassphrase] #converting the passphrase to ascii code
	theOutput = []
	for character, passElement in izip(theText, cycle(thePassphrase)):
		#print character,"\t", passElement, "\t", character ^ passElement
		theOutput.append( chr(character ^ passElement))
	return theOutput

letterSpace = string.ascii_lowercase #lists all the lower case characters

for x in letterSpace:
	for y in letterSpace:
		for z in letterSpace:
			decrypted = "".join( decypher(characters,x+y+z))
			if "gospel" in decrypted.lower():
				print x+y+z, "\t", decrypted
				print sum ( ord(x) for x in decrypted)
