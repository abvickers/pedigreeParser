# format Backcross pedigree symbols. 
# Examples:

# >>> formatBC("AAA/3*BB")
# 'AAA/BB//BB/3/BB' # correct!

# >>> formatBC("AAA*3/BB")
# 'AAA//AAA/3/AAA/BB' # correct!

# >>> formatBC("AA*2//BB/CC")
# 'AA/3/AA//BB/CC' # correct!

# >>> formatBC("A/*2B/C")
# 'A/*2B/C' # INCORRECT! must be a typo in the right pedigree part

# >>> formatBC("D/A*3/3/B//C")
# 'D/A/4/D/A/5/D/A/3/B//C' # INCORRECT!
# should return:
# 'D/A/4/A/5/A/3/B//C'
# or
# 'D/A/5/A/4/A/3/B//C'
# probably need to split left side by cross symbol (need independent function to do this?)
# see ** for location
import re
import getLastCross

def formatBC(ped):
	crossOrder = ["/", "//", ] + ["/" + str(i) + "/" for i in range(3, 10)]
	lc = getLastCross.getLastCross(ped)
	nBCleft = [int(x) for x in re.findall(r'\*([0-9])/', ped) ]
	nBCright = [int(x) for x in re.findall(r'/([0-9])\*', ped) ]
	if len(nBCleft):
		lped = [ped]
	# for i in nBCleft[::-1]: # does this really need to be reversed?
		for i in nBCleft:
			if len(lped) == 1:
				lped = lped[0].split(r"*" + str(i))
			else:
				lped = [ lped.split(i) for x in lped ]
			# ** need to split lped[0] by "/" and take last element? see above
			repPar = [ bc for bc in [lped[0]] for j in range(i) ]
			nextCross = [j+1 for j, x in enumerate(crossOrder) if lc == x][0] # NOte: [0] doesnt allow more than 1 backcross!
			cross = crossOrder[nextCross:nextCross+nBCleft[0]-1]
			cross.append("")
		lped[0] = ''.join([j + k for j , k in zip(repPar, cross)])
		ped = ''.join(lped)
	if len(nBCright):
		rped = [ped]
	# for i in nBCleft[::-1]: # does this really need to be reversed?
		for i in nBCright:
			if len(rped) == 1:
				rped = rped[0].split(str(i) + "*")
			else:
				rped = [ rped.split(i) for x in rped ]
			rpedi = len(rped) -1
			repPar = [ bc for bc in [rped[rpedi]] for j in range(i) ]
			nextCross = [j+1 for j, x in enumerate(crossOrder) if lc == x][0] # NOte: [0] doesnt allow more than 1 backcross!
			cross = crossOrder[nextCross:nextCross+nBCright[0]-1]
			cross.append("")
		rped[rpedi] = ''.join([j + k for j , k in zip(repPar, cross)])
		ped = ''.join(rped)
	return(ped)
