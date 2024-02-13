from Chemin import *
from Echiquier import *

def dfs_path(g: Echiquier, start: tuple[int, int], chemin: list = []) -> bool:
    """
    Trouve un chemin dans g de start à end (sans refaire un chemin appartenant à all_chemin)
    """
    result = False
    x, y = start
    voisinsCavalier = g.voisinsCavalierNonParcouru(g.getCase(x, y))
    # print(voisinsCavalier)

    if chemin == []:
        g.getCase(x, y).indice = 0

    if (voisinsCavalier == [] and g.isPlein()):
        result = True
    else:
        indVoisin = 0
        while (indVoisin < len(voisinsCavalier) and result == False): # transformer en while pour opti
            voisin = voisinsCavalier[indVoisin]
            
            if (g.getCase(voisin[0], voisin[1]) not in chemin):
                g.getCase(voisin[0], voisin[1]).indice = len(chemin)
                if dfs_path(g, voisin, chemin + [g.getCase(x, y)]):
                    result = True
                else:
                    g.getCase(voisin[0], voisin[1]).indice = -1
            
            indVoisin+=1
    # print(tab)

    return result

tab = Echiquier(8, 8)
print(dfs_path(tab, [3, 4]))
print(tab)