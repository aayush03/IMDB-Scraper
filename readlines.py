import sys
filename = sys.argv[1]
lower = int(sys.argv[2])
upper = int(sys.argv[3])

lines = upper - lower

prints = 0
i = 0
f = open(filename)

while(True):
    l = f.readline()
    if (i > lower and i <= upper):
        print l
        prints += 1
        if(prints == lines):
            print "done."
            sys.exit()
    i += 1
