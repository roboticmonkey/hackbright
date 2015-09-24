# function to check for a string

def check_for_string (input):
	if (type(input) == str):
		print input, "is a string!"
	else: print input, "is not a string."


check_for_string("words")
check_for_string(56)
