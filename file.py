from line import Line

class File:
    def __init__(self, file_name):
        self.open_file = open(file_name)

    def next(self):
        for line in self.open_file:
            yield Line(line.decode("ISO-8859-2"))

    def skipToData(self):
        while (True):
            l = self.open_file.readline().decode("ISO-8859-2")
            if (l.startswith("Name")):
                # might have found the begining!
                l2 = self.open_file.readline().decode("ISO-8859-2")
                # filename.readline()
                if (l2.startswith("----")):
                    # found the begining!
                    break
