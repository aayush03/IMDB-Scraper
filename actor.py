class Actor():
	surname = ""
	firstnames = []
	films = []
	disambiguation = 0
	def __init__(self, sname, fnames, disamb=0):
		self.surname = sname
		self.firstnames = fnames
		self.disambiguation = disamb
		self.films = []
		
	def addFilm(self, f):
		self.films.append(f)

	def __str__(self):
		r = ""
		for n in self.firstnames:
			r = r + " " + n
		r = r + self.surname
		return r

