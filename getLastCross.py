# function to get the last cross made symbol/indicator
# >>> getLastCross("A/B")
# '/'
# >>> getLastCross("A/B//C")
# '//'
# >>> getLastCross("A//B/2/C/D")
# '/2/'
# >>> getLastCross("A//B/2/C/D/3/E")
# '/3/'
import re

def getLastCross(ped):
	# find all crosses with integers (e.g.  '/3/' but not '/' or '//')
	crosses = re.findall(r'/([0-9])/', ped)
	# get cross number as integers
	crossNo = [ int(x) for x in crosses ]
	# if integers exist, get max integer
	if len(crossNo):
		lastCross = "/" + str(max(crossNo)) + "/"	
	else:
	# else, find last cross character/pattern 
		# look for '//''
		if(re.search(r'//', ped)):
			lastCross = "//"
		# if no '//', look for '/'
		elif(re.search(r'/', ped)):
			lastCross = "/"
		# if no '/', return empty
		else:
			lastCross = ""
	return lastCross
