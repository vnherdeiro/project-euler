#! /usr/bin/python3


def checkCyclic(original, test):
	for i in range(len(original)):
		if test[i:] + test[:i] == original:
			return True
	return False


beg = "00000000137"
end = "56789"

i = 0
while True:
	number = beg + str(i) + end
	length = len(number)
	if all ( checkCyclic( number, str(int(number) * multFactor).zfill(length)) for multFactor in range(1,length+1)):
		print ( number, sum(map(int,number)))
		break
	i += 1
