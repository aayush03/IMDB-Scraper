class Film:
	name = ""
	year = 0
	def __init__(self, filmName, filmYear):
		self.name = filmName
		self.year = filmYear
	def __str__(self):
		return "%s %s" % (self.name, self.year)

