# coding: utf-8
from Case import *

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
        return self._str_tableau()
    
    def _str_tableau(self):
        # res = "\t-" + ('-' * len(str(self.plateau[0][0])))*len(self.plateau[0]) + "\n" # ligne separation
        # for i in range(len(self.plateau)):
        #     ligne = self.plateau[i]
        #     res += str(i) + "\t"
        #     for case in ligne: # ligne
        #         res += str(case)
        #     res += "|\n\t" + '-' + ('-' * len(str(ligne[0])))*len(ligne) + "\n"
        # return res
        res = self._strIndicesColonne() + self._strLigneSep(0)
        for i in range(len(self.plateau)):
            res += self._strLigneTab(i+1, self.plateau[i])
            res += self._strLigneSep(i+1)
        return res

    def _strIndicesColonne(self) -> str:
        res = "\t" + "".join([f"   {ALPHABET[i+1]} " for i in range((len(self.plateau)))]) + "\n"
        # for i in range(len(self.plateau)):
            # res += "  {indice:2d} ".format(indice = i+1)
        # return res + "\n"
        return res
    
    def _strLigneSep(self, indexLigne: int) -> str:
        extremite = '+' if indexLigne in (0, len(self.plateau)) else '|'

        croisement = '-' if indexLigne in (0, len(self.plateau)) else '+'

        tirets = (('-' * (self._lenAffichageCase() - 1)) + croisement) * len(self.plateau[indexLigne-1]) 

        return f"\t{extremite}{tirets}\b{extremite}\n"
    
    def _lenAffichageCase(self):
        return len(str(self.plateau[0][0]))
    

    def _strLigneTab(self, index : int, ligne: list[int]) -> str:
        res = str(index) + "\t"
        for case in ligne: # ligne
            res += str(case)

        return res + "|\n"

    def initPlateau(self, val:bool=False):
        self.plateau = []
        for x in range(self.tailleX):
            liste = list()
            for y in range(self.tailleY):
                liste.append(Case(x, y, val))
            self.plateau.append(liste)
    
    def getCase(self, x: int, y: int):
        return self.plateau[x][y]

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
