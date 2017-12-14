#!/usr/bin/python

from math import log, pow

infile = "p099_base_exp.txt"

numbers = [ map(int,line.rstrip("\n").split(",")) for line in open(infile)]

numbers = map( lambda (x,y) : y * log(x), numbers) #putting all the numbers in expoential basis and comparing the exponents

print "Max at line ", 1 + numbers.index( max(numbers))
