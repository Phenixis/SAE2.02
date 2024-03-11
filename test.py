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
        afficher_tableau(chemin)
        print(f"Chemin {len(chemins)} ajoutés")
    
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
for x in range(WIDTH) :
    for y in range(HEIGHT) :
        tous_chemins[(x, y)] = backtracking(x, y)
        print(res)


# print(f"({x}, {y}) > ({next_coup[0]}, {next_coup[1]}) = {len(chemin)} cases remplies")
# afficher_tableau(chemin)
# print("\n")

