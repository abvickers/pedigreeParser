
# old function
# def stripNested(x):
# 	noNest = re.sub("[\[].*?[\]]", "", x)
# 	noNest = re.sub("[\(\[].*?[\)\]]", "", noNest)
# 	return noNest

# new function just calls a different one. Can remove eventually, or rename rmParen()
def stripNested(x):
	# return(remove_text_inside_brackets(x))
	return(rmInParen(x))
	# 	return noNest

# this function actually works:
# remove_text_inside_brackets from https://stackoverflow.com/questions/14596884/remove-text-between-and-in-python
# def remove_text_inside_brackets(text, brackets="()[]"):
def rmInParen(text, brackets="()[]"): # needed shorter (but still descriptive) name
    count = [0] * (len(brackets) // 2) # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b: # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close # `+1`: open, `-1`: close
                if count[kind] < 0: # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else: # character is not a [balanced] bracket
            if not any(count): # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)
