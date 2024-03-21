"""
authors : Cyprien ALBERT, Maxime DUHAMEL
date : from 16/02 to 11/03
"""

from constants import *
from random import randint
from math import ceil

WIDTH = C_WIDTH
HEIGHT = C_HEIGHT

def afficher_tableau(chemin):
    """
    Fonction qui affiche le chemin dans un échiquier dans la console (utilisé pour debug)
    """
    tab = [[-1 for y in range(HEIGHT)] for x in range(WIDTH)]

    if chemin:
        for i in range(len(chemin)):
            tab[chemin[i][0]][chemin[i][1]] = i

    for ligne in tab:
        print(ligne)

def backtrackingChemin(x, y, chemin=None, chemins=None):
    """
    Fonction qui utilise un algorithme de backtracking (DFS) pour trouver tous les chemins hamiltoniens selon les déplacements d'un cavalier dans un échiquier rectangulaire donné
    """
    if chemin is None:
        chemin = []
    if chemins is None:
        chemins = []
    
    chemin.append((x, y))

    if (len(chemin) == WIDTH*HEIGHT and chemin not in chemins):
        chemins.append(chemin[:])
    
    coups = coups_possibles_chemin(x, y, chemin)

    for next_coup in coups:
        chemins = backtrackingChemin(next_coup[0], next_coup[1], chemin, chemins)

    chemin.pop()
    return chemins

def backtrackingTour(x, y, chemin=None, chemins=None):
    """
    Fonction qui utilise un algorithme de backtracking (DFS) pour trouver tous les tours hamiltoniens selon les déplacements d'un cavalier dans un échiquier rectangulaire donné
    """
    if chemin is None:
        chemin = []
    if chemins is None:
        chemins = []
    
    chemin.append((x, y))

    if (len(chemin) == (WIDTH*HEIGHT) and chemin not in chemins):
        if (chemin[0] in coups_possibles_tour(x, y, [])):
           print(chemin[:] + [chemin[0]])
           chemins.append(chemin[:] + [chemin[0]])
    
    coups = coups_possibles_tour(x, y, chemin)

    for next_coup in coups:
        chemins = backtrackingTour(next_coup[0], next_coup[1], chemin, chemins)

    chemin.pop()
    return chemins

def coups_possibles_chemin(X, Y, chemin):
    """
    Fonction qui renvoie une liste des coordonnées des cases auxquelles le cavalier peut se rendre pour un chemin hamiltonien
    """
    result = []

    for x, y in COUPS_CAVALIERS:
        if case_valide_chemin(X+x, Y+y, chemin):
            result.append([X+x, Y+y])
    
    return result

def coups_possibles_tour(X, Y, chemin):
    """
    Fonction qui renvoie une liste des coordonnées des cases auxquelles le cavalier peut se rendre pour un tour hamiltonien
    """
    result = []

    for x, y in COUPS_CAVALIERS:
        if case_valide_tour(X+x, Y+y, chemin):
            result.append([X+x, Y+y])
    
    return result

def case_valide_chemin(x,  y, chemin):
    """
    Fonction qui renvoie `True` si la case est dans l'échiquier et hors du chemin. Renvoie `False` sinon
    """
    return (0 <= x < WIDTH and 0 <= y < HEIGHT and (x, y) not in chemin)

def case_valide_tour(x,  y, chemin):
    """
    Fonction qui renvoie `True` si la case est dans l'échiquier et hors du tour sauf pour la dernière case qui doit revenir au point de départ. Renvoie `False` sinon
    """
    res = False
    if (len(chemin) == (WIDTH*HEIGHT)):
        res = (0 <= x < WIDTH and 0 <= y < HEIGHT and (x, y) == chemin[0])
    else:
        res = (0 <= x < WIDTH and 0 <= y < HEIGHT and (x, y) not in chemin)
    return res
        

def symetrie_axiale_point_x(x):
    """
    Fonction qui renvoie la symétrie axiale de la coordonnée `x` dans l'échiquier
    """
    return WIDTH - 1 - x

def symetrie_axiale_point_y(y):
    """
    Fonction qui renvoie la symétrie axiale de la coordonnée `y` dans l'échiquier
    """
    return HEIGHT - 1 - y

def symetrie_axiale_chemin_x(chemin):
    """
    Fonction qui renvoie la symétrie axiale verticale de tous les points du chemins
    """
    res = []
    for point in chemin:
        x,y = point
        res.append((symetrie_axiale_point_x(x), y))
    return res

def symetrie_axiale_chemin_y(chemin):
    """
    Fonction qui renvoie la symétrie axiale horizontale de tous les points du chemins
    """
    res = []
    for point in chemin:
        x,y = point
        res.append((x, symetrie_axiale_point_y(y)))
    return res
    
# def symetrie_axiale_tous_chemins_x(chemins):
#     res = []
#     for chemin in chemins:
#         res.append(symetrie_axiale_chemin_x(chemin))
#     return res

# def symetrie_axiale_tous_chemins_y(chemins):
#     res = []
#     for chemin in chemins:
#         res.append(symetrie_axiale_chemin_y(chemin))
#     return res

def get_tous_chemins(func=backtrackingChemin, verbose=False):
    tous_chemins = {(x, y): [] for x in range(WIDTH) for y in range(HEIGHT)}

    for x in range(ceil(WIDTH/2)) :
        for y in range(ceil(HEIGHT/2)) :

            if verbose:
                print("backtracking...")

            res = func(x, y)

            if verbose:
                print("backtracking fini")
            
            tous_chemins[(x, y)] = res[:]

            if verbose:
                print(f"La case ({x}, {y}) a {len(tous_chemins[(x, y)])} chemins hamiltoniens heuristiques")
            if len(tous_chemins[(x, y)]) != 0:
                if verbose:
                    print("Voici un chemin aléatoire parmi tous les chemins possibles : ")
                afficher_tableau(tous_chemins[(x, y)][randint(0, len(tous_chemins[(x, y)]))-1])

            if verbose:
                print("Calcul de la symétrie...")
            for chemin in res:
                if (x != ceil(WIDTH/2)-WIDTH%2): # (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2) # WIDTH%2 car lorsque WIDTH est impair, on ne doit pas prendre la symétrie axiale de la colonne du milieu, ce qui correspond à la valeur de cette formule(`ceil(WIDTH/2)-WIDTH%2`)
                    tous_chemins[(symetrie_axiale_point_x(x), y)].append(symetrie_axiale_chemin_x(chemin))

                if (y != ceil(HEIGHT/2)-HEIGHT%2): # (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1) # HEIGHT%2 car lorsque HEIGHT est impair, on ne doit pas prendre la symétrie axiale de la ligne du milieu, ce qui correspond à la valeur de cette formule(`ceil(HEIGHT/2)-HEIGHT%2`)
                    tous_chemins[(x, symetrie_axiale_point_y(y))].append(symetrie_axiale_chemin_y(chemin))

                if (x != ceil(WIDTH/2)-WIDTH%2 and y != ceil(HEIGHT/2)-HEIGHT%2): # (0, 0), (0, 1), (1, 0), (1, 1)
                    tous_chemins[(symetrie_axiale_point_x(x), symetrie_axiale_point_y(y))].append(symetrie_axiale_chemin_x(symetrie_axiale_chemin_y(chemin)))
            
            if verbose:
                print("Calcul de la symétrie fini")
    
    for key in tous_chemins.keys():
        x, y = key
        print(f"La case ({x}, {y}) a {len(tous_chemins[(x, y)])} chemins hamiltoniens heuristiques")


""" PLUS D'INFORMATIONS :

Sens de remplissage
0 est le backtracking initial
1 est la symétrie axiale en X correspondant au premier `if` dans la boucle while
2 est la symétrie axiale en Y correspondant au deuxième `if` dans la boucle while
3 est la symétrie centrale correspondant au troisième `if` dans la boucle while
|0|0|0|1|1|
|0|0|0|1|1|
|0|0|0|1|1|
|2|2|2|3|3|
|2|2|2|3|3|

"""

""" Traces des anciennes fonctions """

# === Vérification des fonctions de symétrie ===

# # === Symétrie Axiale En X ===
# init = backtrackingChemin(0, 0)
# res_awaited = backtrackingChemin(4, 0)

# res = symetrie_axiale_tous_chemins_x(init)

# # # === Premier Test ===
# result = True
# i = 0
# while(i < len(res) and result):
#     result = res[i] in res_awaited
#     i+=1

# print(result)

# # # === Second Test ===
# res = sorted(res)
# res_awaited = sorted(res_awaited)
# print(res == res_awaited)


# # === Symétrie Axiale En Y ===
# res_awaited = backtrackingChemin(0, 4)

# res = symetrie_axiale_tous_chemins_y(init)

# # # === Premier Test ===
# result = True
# i = 0
# while(i < len(res) and result):
#     result = re fonctions de symétrie ===

# # === Symétrie Axiale En X ===
# init = backtrackingChemin(0, 0)
# res_awaited = backtrackingChemin(4, 0)

# res = symetrie_axiale_tous_chemins_x(init)

# # # === Premier Test ===
# result = True
# i = 0
# while(i < len(res) and result):
#     result = res[i] in res_awaited
#     i+=1

# print(result)

# # # === Second Test ===
# res = sorted(res)
# res_awaited = sorted(res_awaited)
# print(res == res_awaited)


# # === Symétrie Axiale En Y ===
# res_awaited = backtrackingChemin(0, 4)

# res = symetrie_axiale_tous_chemins_y(init)

# # # === Premier Test ===
# result = True
# i = 0
# while(i < len(res) and result):
#     result = res[i] in res_awaited
#     i+=1

# print(result)

# # # === Second Test ===
# res = sorted(res)
# res_awaited = sorted(res_awaited)
# print(res == res_awaited)


# # === Symétrie Centrale (Axiale en X et en Y) ===
# res_awaited = backtrackingChemin(4, 4)

# res = symetrie_axiale_tous_chemins_x(symetrie_axiale_tous_chemins_y(init))

# # # === Premier Test ===
# result = True
# i = 0
# while(i < len(res) and result):
#     result = res[i] in res_awaited
#     i+=1

# print(result)

# # # === Second Test ===
# res = sorted(res)
# res_awaited = sorted(res_awaited)
# print(res == res_awaited)


# # === Symétrie Centrale (Axiale en X et en Y) ===
# res_awaited = backtrackingChemin(4, 4)

# res = symetrie_axiale_tous_chemins_x(symetrie_axiale_tous_chemins_y(init))

# # # === Premier Test ===
# result = True
# i = 0
# while(i < len(res) and result):
#     result = res[i] in res_awaited
#     i+=1

# print(result)

# # # === Second Test ===
# res = sorted(res)
# res_awaited = sorted(res_awaited)
# print(res == res_awaited)