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

def symetrie_axiale_point_x(x):
    return WIDTH - 1 - x

def symetrie_axiale_point_y(y):
    return HEIGHT - 1 - y

def symetrie_axiale_chemin_x(chemin):
    res = []
    for point in chemin:
        x,y = point
        res.append((symetrie_axiale_point_x(x), y))
    return res

def symetrie_axiale_chemin_y(chemin):
    res = []
    for point in chemin:
        x,y = point
        res.append((x, symetrie_axiale_point_y(y)))
    return res
    
def symetrie_axiale_tous_chemins_x(chemins):
    res = []
    for chemin in chemins:
        res.append(symetrie_axiale_chemin_x(chemin))
    return res

def symetrie_axiale_tous_chemins_y(chemins):
    res = []
    for chemin in chemins:
        res.append(symetrie_axiale_chemin_y(chemin))
    return res

tous_chemins = {(x, y): [] for x in range(WIDTH) for y in range(HEIGHT)}

for x in range(ceil(WIDTH/2)) :
    for y in range(ceil(HEIGHT/2)) :
        print("backtracking...")
        res = backtracking(x, y)
        print("backtracking fini")
        tous_chemins[(x, y)] = res[:]

        print(f"La case ({x}, {y}) a {len(tous_chemins[(x, y)])} chemins hamiltoniens heuristiques")
        if len(tous_chemins[(x, y)]) != 0:
            print("Voici un chemin aléatoire parmi tous les chemins possibles : ")
            afficher_tableau(tous_chemins[(x, y)][randint(0, len(tous_chemins[(x, y)]))-1])
        print("Calcul de la symétrie...")

        for chemin in res:

            if (x != ceil(WIDTH/2)-1): # (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)

                tous_chemins[(symetrie_axiale_point_x(x), y)].append(symetrie_axiale_chemin_x(chemin))

            if (y != ceil(HEIGHT/2)-1): # (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)

                tous_chemins[(x, symetrie_axiale_point_y(y))].append(symetrie_axiale_chemin_y(chemin))

            if (x != ceil(WIDTH/2)-1 and y != ceil(HEIGHT/2)-1): # (0, 0), (0, 1), (1, 0), (1, 1)

                tous_chemins[(symetrie_axiale_point_x(x), symetrie_axiale_point_y(y))].append(symetrie_axiale_chemin_x(symetrie_axiale_chemin_y(chemin)))
        
        print("Calcul de la symétrie fini")
# Sens de remplissage
# 0 est le backtracking initial
# 1 est la symétrie axiale en X du premier `if` dans la boucle while
# 2 est la symétrie axiale en Y du deuxième `if` dans la boucle while
# 3 est la symétrie centrale du troisième `if` dans la boucle while
#|0|0|0|1|1|
#|0|0|0|1|1|
#|0|0|0|1|1|
#|2|2|2|3|3|
#|2|2|2|3|3|

for key in tous_chemins.keys():
    x, y = key
    print(f"La case ({x}, {y}) a {len(tous_chemins[(x, y)])} chemins hamiltoniens heuristiques")

# === Vérification des fonctions de symétrie ===

# # === Symétrie Axiale En X ===
# init = backtracking(0, 0)
# res_awaited = backtracking(4, 0)

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
# res_awaited = backtracking(0, 4)

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
# res_awaited = backtracking(4, 4)

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