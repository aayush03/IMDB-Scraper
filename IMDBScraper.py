import re
from roman import fromRoman as roman2int
from actor import Actor
from film import Film
from file import File

class IMDBScraper:
	def __init__(self, file_name):
		self.open_file = File(file_name)
		self.open_file.skipToData()
		
	def next(self):
		actor = Actor("init", "actor")
		for line in self.open_file.next():
			if (line.containsActorName()):
				yield actor
				actor, film = line.getActorAndFilm()
				actor.addFilm(film)
			else:
				film = line.getFilm()
				if not film is None:
					actor.addFilm(film)
			

