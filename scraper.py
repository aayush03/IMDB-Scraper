import re
from roman import fromRoman as roman2int
f = open("actors.list", "r")

class Film:
	name = ""
	year = 0
	disambiguation = 0
	def __init__(self, filmName, filmYear, disamb):
		self.name = filmName
		self.year = filmYear
		self.disambiguation = disamb
	

class Actor:
	surname = ""
	firstnames = []
	films = []
	disambiguation = 0
	def __init__(self, sname, fnames, disamb=0):
		self.surname = sname
		self.firstnames = fnames
		self.disambiguation = disamb
		
	def addFilm(self, f):
		self.films.append(f)

class Line:
	line = ""
	def __init__(self, string):
		self.line = string
	def getActorAndFilm(self):
		l = self._tokenize("\t")
		actor = Line(l[0]).getActor()
		film = Line(l[-1]).getFilm()
		return actor, film
		
	def getActor(self):
		# this functions puts the actor's name into 
		# an array for the first names
		# a stiring for the surname
		# and an integer for the disamiguation
		actorName = self._tokenize(" ")
		# if actorName is only one item long, then it is someone with one name, like Cher
		if (actorName.__len__() == 1):
			surname = actorName[0]
			firstnames = []
			disamb = 0
		else:
			# surname is the 0th item in actorName
			# the surname is followed by a ',' that we need to remove
			# and the we remove the surnams from actorName
			surname = actorName.pop(0).replace(',', '')
			# the last item may be a disambiguation number. Fx. (II)
			# we need to capture it, if it's there, and then remove it from actorName
			lastItem = actorName[-1]	
			if (re.search("\(|\)", lastItem)):
				disamb = lastItem.replace("(", "").replace(")", "")
				try: # I'm not sure if it's always a roman numeral, or if sometimes it's a number
					disamb = int(disamb) # either case, it should work.
				except ValueError:
					disamb = roman2int(disamb)
				except:
					disamb = 0
				actorName.pop() #defaults to the last, so we don't need an index
			else:
				disamb = 0
			# remaining names should be the firstnames
			firstnames = actorName
#		print "VVVVVVVVVVVVV"
#		print self.line
#		print surname, firstnames, disamb
#		print "_____________"
		return Actor(surname, firstnames, disamb)

	def containsActorName(self):
		if (re.search("^\S", self.line) != None): # starts with a non-whitespace character
			return True                      # will fail after the end of the data file
		else:                                # when other non-actor lines start with a character
			return False
	
	def getFilm(self):
		filmName = "" 
		year = 0
		disamb = 0
		filmString = self._tokenize(" ")
		# cleaning up for processing
		# empty items, tabs in the first item, newlines in the last one
		empties = filmString.count("")
		for i in xrange(0, empties):
			filmString.remove("")
		filmString[0] = filmString[0].replace("\t", "")
		filmString[-1] = filmString[-1].replace("\n", "")
		if (re.search("<\d+>", filmString[-1])): # fx. <25>. I _think_ this is disambiguation
			disamb = int(filmString.pop().replace("<", "").replace(">", ""))		
		for item in filmString:
			filmName = filmName + " " + i
			if (re.search("\(\d+\)", item)): #fx (1986)
				year = int(i.replace("(", "").replace(")", ""))
				break
		return Film(filmName.strip(), year, disamb)
	
	
	def _tokenize(self, s):
		return self.line.split(s)
		


def goToData(filename):
	while (True):
		l = filename.readline()
		if (l.startswith("Name")):
			# might have found the begining!
			l2 = f.readline()
			if (l2.startswith("----")):
				# found the begining!
				break


def testLine(line):
	test = Line(line)
	test.getFilm()
testLine('"The Bonnie Hunt Show" (2008) {(2010-03-24)}  [Himself]')
testLine('"Oog in oog" (1991)  [Oudste zoon (1993)]')
testLine('"Au th��tre ce soir" (1966) {La coquine (1981)}  [Le valet de chambre]  <8>')
testLine('')

#while(True): pass

goToData(f)
while True:
	l = Line(f.readline())
	if (l.containsActorName()):
		actor, film = l.getActorAndFilm()
		actor.addFilm(film)
	else:
		l.getFilm()


#	def getFilm(self):
#		filmName = "" 
#		year = 0
#		disamb = 0
#		role = ""
#		filmString = self._tokenize(" ")
#		# if it contains one of these, it's not a film. (VG) == video game
#		if (filmString.__len__() == 1):
#			if (filmString[0] != '\n'):
#				print "non-empty?", filmString
#			return None
#		if (filmString.count("(VG)") > 0):
#			return None
#		# cleaning up for processing
#		# empty items, tabs in the first item, newlines in the last one
#		empties = filmString.count("")
#		for i in xrange(0, empties):
#			filmString.remove("")
#		filmString[0] = filmString[0].replace("\t", "")
#		filmString[-1] = filmString[-1].replace("\n", "")
#	
#		# These if-statements check for optional items in the list
#		# and if they are there, they remove the from the array, and 
#		# convert them into an integer or string.
#		print "VVVVVVVVVVVVV"
#		print self.line
#		print filmString
#		print filmName, year
#		if (re.search("<\d+>", filmString[-1])): # fx. <25>. I _think_ this is disambiguation
#			disamb = int(filmString.pop().replace("<", "").replace(">", ""))
#			print disamb, "disamb"
#			print filmString
#		# Remove multi-item []s fx. "Oog in oog" (1991)  [Oudste zoon (1993)]
#		# first search if the last item has ] but not [
#		# then continue until one has [ but not ]
#		# then remove from the [ to ]
#		# it will remove the item in ['s  position, until it reaches the end #a
#		if (re.search("\]", filmString[-1]) and not re.search("\[", filmString[-1])):
#			begining = 0
#			for i in xrange(2, filmString.__len__()):
#				if (re.search("\[", filmString[-i]) and not re.search("\]", filmString[-i])):
#					begining = i
#					break
#			index = - begining 
#			while (True): #a
#				filmString.pop(index)
#				index += 1
#				if (index >= 0):
#					break
#		if (re.search("\[.+\]", filmString[-1])): # fx. [Himself].
#			role = filmString.pop().replace("[", "").replace("]", "")
#			print role, "role"
#			print filmString
#		if (re.search("\(w+\)", filmString[-1])): # fx. (v)
#			filmType = filmString.pop().replace("(", "").replace(")", "")
#			print filmType, "filmType"
#			print filmString
#		if (re.search("{.+}", filmString[-1])): # fx. {(#10.1)},  used for TV shows.
#			filmString.pop()
#			print filmString.pop(), "episode"
#		if (re.search("\(\d+\)", filmString[-1])): #fx (1986)
#			try:
#				year = int(filmString.pop().replace("(", "").replace(")", ""))	
#			except:
#				print self.line
#				print filmString
#				print year
#			print year, "year"
#			print filmString
#		# strigify the rest of the array ( should be the film name )
#		for i in filmString:
#			filmName = filmName + i + " "
#		filmName = filmName.strip()
#		print
#		print
#		print "_____________"
#
#
#		return Film(filmName, year, disamb)


#def detectNewActor(line):
#	if (re.search("^\S", line) != None): # starts with a non-whitespace character
#		return True
#	else:
#		return False

#def getActor(line):
#	l = line.split("\t")
#	actor = parseActor(l[0])
#	film = parseFilm(l[-1])
#	actor.addFilm(film)

#def parseActor(actorString):
	# this functions puts the actor's name into 
	# an array for the first names
	# a stiring for the surname
	# and an integer for the disamiguation #TODO
#	actorName = actorString.split(" ")
	# surname is the 0th item in actorName
	# the surname is followed by a ',' that we need to remove
	# and the we remove the surnams from actorName
#	surname = actorName.pop(0).replace(',', '')
	# the last item may be a disambiguation number. Fx. (II)
	# we need to capture it, if it's there, and then remove it from actorName
#	lastItem = actorName[-1]	
#	if (re.search("\(|\)", lastItem)):
#		disamb = last
#		actprName.pop() #defaults to the last, so we don't need an index
#	else:
#		disamb = 0
	# remaining names should be the firstnames
#	firstnames = actorName
#	return Actor(surname, firstnames, disamb)

#def parseFilm(line):
#	filmString = line.split(" ")
#	print filmString
#	empties = filmString.count("")
#	print empties
#	for i in xrange(0, empties):
#		print "clearing"
#		filmString.remove("")
#	print filmString
#	if (re.search("<|>", filmString[-1])):
#		disamb = filmString.pop()
#	if (re.search("\[|\]", filmString[-1])):
#		role = filmString.pop()
#	if (re.search("\(|\)", filmString[-1])):
#		year = filmString.pop()
#	filmName = filmString
#	print filmName
#	print filmName.tostring()
#	return "film"
