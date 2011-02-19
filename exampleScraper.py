#Example scraper. Doesn't acctually save anything.
import sys
from utils import goToData
from line import Line

f = open(sys.argv[1], "r")
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
		actor.addFilm(l.getFilm())
