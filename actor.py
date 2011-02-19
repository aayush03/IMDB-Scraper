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
