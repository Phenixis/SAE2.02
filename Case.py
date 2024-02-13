ALPHABET = " abcdefghijklmnopqrstuvwxyz"

class Case(object):
    def __init__(self, x=0, y=0, parcouru=False):
        self.x = x
        self.y = y
        self.indice = -1
    
    def __str__(self):
        return self.getCoordonnéesEchec() + ": " + str(self.indice)
    
    def __repr__(self):
        return "{indice:2d}".format(indice = self.indice)

    def getCoordonnéesEchec(self) :
        return ALPHABET[self.x+1] + str(self.y+1)

















