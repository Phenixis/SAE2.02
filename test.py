from random import randint
from math import ceil

WIDTH = HEIGHT = 5
COUPS_CAVALIERS = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

def afficher_tableau(chemin):
    tab = [[-1 for y in range(HEIGHT)] for x in range(WIDTH)]

    if chemin:
        for i in range(len(chemin)):
            tab[chemin[i][0]][chemin[i][1]] = i

    for ligne in tab:
        print(ligne)

def backtracking(x, y, chemin=None, chemins=None):
    if chemin is None:
        chemin = []
    if chemins is None:
        chemins = []
    
    chemin.append((x, y))

    if (len(chemin) == WIDTH*HEIGHT and chemin not in chemins):
        chemins.append(chemin[:])
        # afficher_tableau(chemin)
        # print(f"Chemin {len(chemins)} ajoutés")
    
    coups = coups_possible(x, y, chemin)

    for next_coup in coups:
        chemins = backtracking(next_coup[0], next_coup[1], chemin, chemins)

    chemin.pop()
    return chemins

def coups_possible(X, Y, chemin):
    result = []

    for x, y in COUPS_CAVALIERS:
        if coup_possible(X+x, Y+y, chemin):
            result.append([X+x, Y+y])
    
    return result

def coup_possible(x,  y, chemin):
    return (0 <= x < WIDTH and 0 <= y < HEIGHT and (x, y) not in chemin)

tous_chemins = {}
for x in range(ceil(WIDTH/2)) :
    for y in range(ceil(HEIGHT/2)) :
        res = backtracking(x, y)
        tous_chemins[(x, y)] = res
        print(f"La case ({x}, {y}) a {len(tous_chemins[(x, y)])} chemins hamiltoniens heuristiques")
        if len(tous_chemins[(x, y)]) != 0:
            print("Voici un chemin aléatoire parmi tous les chemins possibles : ")
            afficher_tableau(tous_chemins[(x, y)][randint(0, len(tous_chemins[(x, y)]))-1])
        print("Calcul de la symétrie")
        tous_chemins[(symetrie_axiale_point_x(x), y)] = symetrie_axiale_chemins_x(res)
        tous_chemins[(X, symetrie_axiale_chemin_y(y))] = symetrie_axiale_chemins_y(res)
        
        


# print(f"({x}, {y}) > ({next_coup[0]}, {next_coup[1]}) = {len(chemin)} cases remplies")
# afficher_tableau(chemin)
# print("\n")

def symetrie_axiale_point_x(x):
    ...

def symetrie_axiale_point_y(y):
    ...

def symetrie_axiale_chemin_x(chemin):
    ...

def symetrie_axiale_chemin_y(chemin):
    ...

def symetrie_axiale_chemins_x(chemins):
    ...

def symetrie_axiale_chemins_y(chemins):
    ...