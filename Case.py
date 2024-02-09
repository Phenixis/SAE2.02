ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Case(object):
    def __init__(self, x=0, y=0, parcouru=False):
        self.x = x
        self.y = y
        self.parcouru = parcouru
    
    def __str__(self):
        return self.getCoordonnéesEchec() + ": " + str(self.parcouru)
    
    def __repr__(self):
        return f"[{'x' if self.parcouru else ' '}]"

    def getCoordonnéesEchec(self) :
        return ALPHABET[self.x-1] + str(self.y)


















