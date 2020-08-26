# Given to parent strings and a pedigree string, this will return the shortest match between parents, regardless of location
# reutrns index in string [first, last]

# >>> ped = "AA (X/Y) / BB (V/W) // BB(V/W) / CC (T/U)"
# >>> pedIndex = getShortMatch("BB", "CC", ped)
# >>> ped[pedIndex[0]:pedIndex[1]]
import re

def getShortMatch(p1, p2, ped):
	p1pos = []
	p2pos = []
	for match in re.finditer(p1, ped):
		p1pos.append(match.span())

	p1start = [x[0] for x in p1pos]
	p1end = [x[1] for x in p1pos]
	for match in re.finditer(p2, ped):
		p2pos.append(match.span())

	p2start = [x[0] for x in p2pos]
	p2end = [x[1] for x in p2pos]
	# remove any p1's starting after last p2
	p1start = [ x for x in p1start if x < p2start[len(p2start)-1]]
	i1 = p1start[0]
	i2 = p2end[0]
	diff = abs(p1start[0] - p2end[0])
	for i in p1start:
		for j in p2end:
			diffi = abs(i - j)
			if diff > diffi:
				i1 = i
				i2 = j
				diff = diffi
	return [i1,i2]
