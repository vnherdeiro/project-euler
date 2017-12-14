#! /usr/bin/python3

def nTiles( length):
	return 4*(length-1)

MAX_TILES = 1000000

def count( lastTile, totTile):
	if totTile > MAX_TILES:
		return 0
	#print( totTile)
	totCount = 1
	totCount += count( lastTile+2, totTile+nTiles(lastTile+2))
	return totCount

t = 0
for x in range(3, MAX_TILES//4 + 4):
	t += count(x,nTiles(x))

print( t)
