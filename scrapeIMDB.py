import 
goToData(f)
while True:
	l = Line(f.readline())
	if (l.endOfData()):
		break
	elif (l.containsActorName()):
		actor, film = l.getActorAndFilm()
		actor.addFilm(film)
	else:
		l.getFilm()
