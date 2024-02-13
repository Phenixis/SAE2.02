# coding: utf-8
from Case import Case

class Echiquier(object):

    def __init__(self, tailleX, tailleY):
        """ 
        initialise un objet graphe.
	    Si aucun dictionnaire n'est
	    créé ou donné, on en utilisera un 
	    vide
        """
        self.plateau = list()
        self.tailleX = tailleX
        self.tailleY = tailleY

        self.initPlateau()

    def __iter__(self):
        self._iter_obj = iter(self._graphe_dict)
        return self._iter_obj

    def __next__(self):
        """ Pour itérer sur les sommets du graphe """
        return next(self._iter_obj)

    def __str__(self):
        res = ""
        for ligne in self.plateau:
            res += str(ligne) + "\n"
            # for y in range(len(self.plateau[x])) :
            #     res += "[" + str(int(self.plateau[x][y].parcouru)) + "]"
            # res += "\n"
        return res

    def initPlateau(self, val:bool=False):
        self.plateau = []
        for x in range(self.tailleX):
            liste = list()
            for y in range(self.tailleY):
                liste.append(Case(x, y, val))
            self.plateau.append(liste)
    
    def getCase(self, x: int, y: int):
        return self.plateau[x][y]
    
    def aretes(self, sommet):
        """ retourne une liste de toutes les aretes d'un sommet"""
        return self._graphe_dict[sommet]

    def all_sommets(self):
        """ retourne tous les sommets du graphe """
        return self._graphe_dict.keys()

    def all_aretes(self):
        """ retourne toutes les aretes du graphe """
        return self.__list_aretes()

    def add_sommet(self, sommet):
        """
        Si le "sommet" n'set pas déjà présent
        dans le graphe, on rajoute au dictionnaire 
        une clé "sommet" avec une liste vide pour valeur. 
        Sinon on ne fait rien.
        """
        if sommet not in self.all_sommets():
            self._graphe_dict[sommet] = []

    def add_arete(self, arete):
        """
        l'arete est de  type set, tuple ou list;
        Entre deux sommets il peut y avoir plus
	    d'une arete (multi-graphe)
        """
        dep, arr = arete

        if dep in self.all_sommets():
            if arr not in self.aretes(dep):
                self._graphe_dict[dep].append(arr)
                self.add_arete([arr, dep])

    def __list_aretes(self):
        """
        Methode privée pour récupérer les aretes. 
	    Une arete est un ensemble (set)
        avec un (boucle) ou deux sommets.
        """
        # res = []
        # for sommet in self.all_sommets():
        #     for arete in self.aretes(sommet):
        #         res.append([sommet, arete])
        # return res
        return [[[sommet, arete] for arete in self.aretes(sommet)] for sommet in self.all_sommets()]

    def trouve_chaine(self, sommet_dep, sommet_arr, chain=None):
        chain = [sommet_dep] if chain is None else chain
        res = chain

        # print(chain)

        voisins = self.aretes(sommet_dep)
        i = 0
        while (i < len(voisins) and res[-1] != sommet_arr):
            voisin = voisins[i]
            if voisin not in chain:
                # print(voisin)
                res = self.trouve_chaine(voisin, sommet_arr, chain + [voisin])
            i+=1
        
        return res


    def trouve_toutes_chaines(self, sommet_dep, sommet_arr, sommets=[]):
        res = []

        if (sommet_dep == sommet_arr):
            return [[sommet_dep]]
        else:
            for voisin in self.aretes(sommet_dep):
                if voisin not in sommets:
                    chemins = self.trouve_toutes_chaines(voisin, sommet_arr, sommets + [sommet_dep])
                    for chemin in chemins:
                        res.append([sommet_dep] + chemin)

        return res

    def isPlein(self):
        res = True
        x = 0

        while(res == True and x < len(self.plateau)):
            y = 0
            while(res == True and y < len(self.plateau[x])):
                res = (self.plateau[x][y].indice != -1)
                y += 1
            x += 1
        
        return res
        # return sum([sum(ligne) for ligne in self.plateau]) == self.tailleX*self.tailleY

    def remplir(self):
        self.initPlateau(True) 

    def voisinsCavalierNonParcouru(self, case: Case):
        result = []
        # print(case)

        for x, y in [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]:
            if (self.voisinsCavalierValides(case.x+x, case.y+y)):
                result.append([case.x+x, case.y+y])

        # for deux in [-2, 2]:
        #     for un in [-1, 1]:

        #         if (self.voisinsCavalierValides(case.x+deux, case.y+un)):
        #             result.append([case.x+deux, case.y+un])

        #         if (self.voisinsCavalierValides(case.x+un, case.y+deux)):
        #             result.append([case.x+un, case.y+deux])
        
        return result
    
    def voisinsCavalierValides(self, x, y):
        return (0 <= x < self.tailleX and 0 <= y < self.tailleY and self.getCase(x, y).indice == -1)

    def dfs_path(self, start: tuple[int, int], chemin: list = []) -> bool:
        """
        Trouve un chemin dans l'échiquier à partir de start
        """
        result = False
        x, y = start
        voisinsCavalier = self.voisinsCavalierNonParcouru(self.getCase(x, y))

        if chemin == []:
            self.getCase(x, y).indice = 0
        
        if (voisinsCavalier == [] and self.isPlein()):
            result = True
            chemin.append(self.getCase(x, y))
        else:
            indVoisin = 0
            while (indVoisin < len(voisinsCavalier) and result == False):
                voisin = voisinsCavalier[indVoisin]
                
                if (self.getCase(voisin[0], voisin[1]) not in chemin):
                    self.getCase(voisin[0], voisin[1]).indice = len(chemin)+1

                    if self.dfs_path(voisin, chemin + [self.getCase(x, y)]):
                        result = True
                    else:
                        self.getCase(voisin[0], voisin[1]).indice = -1
                
                indVoisin+=1
        
        if result == False and self.getCase(x, y).indice == 0:
            self.getCase(x, y).indice = -1

        return result
