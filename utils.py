def goToData(filename):
	while (True):
		l = filename.readline().decode("ISO-8859-2")
		if (l.startswith("Name")):
			# might have found the begining!
			l2 = filename.readline()
			if (l2.startswith("----")):
				# found the begining!
				break

def string2list(list_of_strings):
	returnString = ""
	for i in list_of_strings:
		returnString = returnString + " " + i
	return returnString.strip()
