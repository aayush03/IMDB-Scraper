from scraper import goToData, Line, Film, Actor

f = open("actors.list", "r")
lineNo = 0

goToData(f)
while True:
	l = Line(f.readline())
        print l.line
	if (l.endOfData()):
		break
	elif (l.containsActorName()):
		actor, film = l.getActorAndFilm()
		actor.addFilm(film)
	else:
		l.getFilm()
