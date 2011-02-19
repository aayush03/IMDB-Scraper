def goToData(filename):
	while (True):
		l = filename.readline()
		if (l.startswith("Name")):
			# might have found the begining!
			l2 = filename.readline()
			if (l2.startswith("----")):
				# found the begining!
				break

