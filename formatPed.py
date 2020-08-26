# function to clean up white space surrounding cross slashes
# "  / " -> "/"
import re
def formatPed(ped):
	return re.sub("\s*/\s*", "/", ped)

	# would be nice if we could add uniform spaces back in for human eyes, but this funcitonality is low priority