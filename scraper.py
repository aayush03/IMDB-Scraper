import re
from roman import fromRoman as roman2int

class Film:
	name = ""
	year = 0
	def __init__(self, filmName, filmYear):
		self.name = filmName
		self.year = filmYear


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
					disamb = roman2int(disamb) # either case, it should work.:
				except:
					disamb = 0
					print actorName
					print self.line
					print lineNo
				actorName.pop() #defaults to the last, so we don't need an index
			else:
				disamb = 0
			# remaining names should be the firstnames
			firstnames = actorName
		return Actor(surname, firstnames, disamb)

	def containsActorName(self):
		if (re.search("^\S", self.line) != None): # starts with a non-whitespace character
			return True                      # will fail after the end of the data file
		else:                                # when other non-actor lines start with a character
			return False
	
	def getFilm(self):
		filmName = "" 
		year = 0
		filmString = self._tokenize(" ")
		# cleaning up for processing
		# empty items, tabs in the first item, newlines in the last one
		empties = filmString.count("")
		for i in xrange(0, empties):
			filmString.remove("")
		if (filmString.__len__() <= 1): # all films have a title and a year
			return None
		filmString[0] = filmString[0].replace("\t", "")
		filmString[-1] = filmString[-1].replace("\n", "")
		for item in filmString:
			filmName = filmName + " " + item
			if (re.search("\(\d{4}.*\)", item)): #fx (1986) or (2010/I)
				try:
					# find 4 numbers followed zero or more any-character,
					# all of which is surrounded by ()s,
					# then capture the 4 numbers.
					# re.findall returns a list, we want the first item, hence the [0]
					year = re.findall("\((\d{4}).*\)", item)[0]
					break
				except:
					print filmString, item
		return Film(filmName.strip(), year)

	def endOfData(self):
		if (self.line.startswith("-----------------------------------------------")):
			return True
		else:
			return False


	
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



