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
        self.plateau = None
        self.tailleX = tailleX
        self.tailleY = tailleY
        self.nbCasesParcourues = 0
        self.occur = 0
        
        self.initPlateau()

    def __next__(self):
        """ Pour itérer sur les sommets du graphe """
        return next(self._iter_obj)

    def __str__(self):
        return self._str_tableau()
    
    def _str_tableau(self):
        res = self._strIndicesColonne() + self._strLigneSep(0)

        for x in range(self.tailleX):
            res += self._strLigneTab(x)
            res += self._strLigneSep(x)
        
        return res

    def _strIndicesColonne(self) -> str:
        res = "\t" + "".join([f"   {ALPHABET[i+1]} " for i in range((self.tailleX))]) + "\n"
        # for i in range(len(self.plateau)):
            # res += "  {indice:2d} ".format(indice = i+1)
        # return res + "\n"
        return res
    
    def _strLigneSep(self, indexLigne: int) -> str:
        extremite = '+' if indexLigne+1 in (0, self.tailleX) else '|'

        croisement = '-' if indexLigne+1 in (0, self.tailleX) else '+'

        tirets = (('-' * (self._lenAffichageCase() - 1)) + croisement) * self.tailleY 

        return f"\t{extremite}{tirets}\b{extremite}\n"
    
    def _lenAffichageCase(self):
        return len(str(self.getCase(0, 0)))
    

    def _strLigneTab(self, index : int) -> str:
        res = str(index+1) + "\t"

        for y in range(self.tailleY): 
            res += str(self.getCase(index, y))

        return res + "|\n"

    def initPlateau(self, val:bool=False):
        self.plateau = [[Case(x, y, val) for y in range(self.tailleY)] for x in range(self.tailleX)]
    
    def getCase(self, x: int, y: int):
        return self.plateau[x][y]

    def isPlein(self):
        res = True

        x = 0
        while(res == True and x < self.tailleX):
            y = 0
            while(res == True and y < self.tailleY):
                res = (self.getCase(x, y).indice != -1)
                y += 1
            x += 1
        
        return res

    def isPlein1(self):
        return self.nbCasesParcourues == (self.tailleX * self.tailleY)

    def remplir(self):
        self.initPlateau(True) 

    def voisinsCavalierNonParcouru(self, case: Case):
        result = []
        # print(case)

        for x, y in [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]:
            if (self.voisinsCavalierValides(case.x+x, case.y+y)):
                result.append([case.x+x, case.y+y])
        
        return result
    
    def voisinsCavalierValides(self, x, y):
        return (0 <= x < self.tailleX and 0 <= y < self.tailleY and self.getCase(x, y).indice == -1)

    def dfs_path(self, start: tuple[int, int], chemin: list = []) -> bool:
        """
        Trouve un chemin dans l'échiquier à partir de start
        """
        self.occur += 1
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
    
    def dfs_path1(self, start: tuple[int, int], indice: int=0) -> bool:
        """
        Trouve un chemin dans l'échiquier à partir de start
        """
        self.occur += 1
        result = False
        x, y = start
        voisinsCavalier = self.voisinsCavalierNonParcouru(self.getCase(x, y))

        if indice == 0:
            self.getCase(x, y).indice = indice
        
        if (voisinsCavalier == [] and self.isPlein()):
            result = True
            
        else:
            indVoisin = 0
            while (indVoisin < len(voisinsCavalier) and result == False):
                voisin = voisinsCavalier[indVoisin]
                
                if (self.getCase(voisin[0], voisin[1]).indice == -1):
                    self.getCase(voisin[0], voisin[1]).indice = indice+1

                    if self.dfs_path1(voisin, indice + 1):
                        result = True
                    else:
                        self.getCase(voisin[0], voisin[1]).indice = -1
                
                indVoisin+=1
        
        if result == False and self.getCase(x, y).indice == 0:
            self.getCase(x, y).indice = -1

        return result

    def dfs_path2(self, start: tuple[int, int], indice: int=0) -> bool:
        """
        Trouve un chemin dans l'échiquier à partir de start
        """
        self.occur += 1
        result = False
        x, y = start

        self.getCase(x, y).indice = indice
        voisinsCavalier = self.voisinsCavalierNonParcouru(self.getCase(x, y))

        # if indice == 0:
        #     self.getCase(x, y).indice = indice
        
        if (voisinsCavalier == [] and self.isPlein()):
            result = True
            
        else:
            indVoisin = 0

            while (indVoisin < len(voisinsCavalier) and result == False):
                voisin = voisinsCavalier[indVoisin]

                result = (self.getCase(voisin[0], voisin[1]).indice == -1) and (self.dfs_path2(voisin, indice + 1))
                
                # if (self.getCase(voisin[0], voisin[1]).indice == -1):
                #     if self.dfs_path2(voisin, indice + 1):
                #         result = True
                    
                indVoisin+=1
                # print(self)

            if result == False:
                self.getCase(x, y).indice = -1

        return result
    
    def dfs_path3(self, start: tuple[int, int]) -> bool:
        """
        Trouve un chemin dans l'échiquier à partir de start
        """
        result = False
        x, y = start

        self.parcourir(x, y)
        voisinsCavalier = self.voisinsCavalierNonParcouru(self.getCase(x, y))
        
        if (self.isPlein1()):
            result = True
            
        else:
            indVoisin = 0

            while (result == False and indVoisin < len(voisinsCavalier)):
                voisin = voisinsCavalier[indVoisin]

                result = (self.getCase(voisin[0], voisin[1]).indice == -1) and (self.dfs_path3(voisin))
                    
                indVoisin+=1

            if result == False:
                self.deparcourir(x, y)

        return result

    def parcourir(self, x, y):
        self.getCase(x, y).indice = self.nbCasesParcourues
        self.nbCasesParcourues+=1
    
    def deparcourir(self, x, y):
        self.getCase(x, y).indice = -1
        self.nbCasesParcourues-=1
        
