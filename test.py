WIDTH = HEIGHT = 6
COUPS_CAVALIERS = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

def afficher_tableau(chemin):
    tab = [[-1 for y in range(HEIGHT)] for x in range(WIDTH)]

    if chemin:
        for i in range(len(chemin)):
            tab[chemin[i][0]][chemin[i][1]] = i

    for ligne in tab:
        print(ligne)

def backtracking(x, y, chemin=None):
    if chemin == None:
        chemin = []
    
    chemin.append((x, y))

    if (len(chemin) == WIDTH*HEIGHT):
        return chemin
    
    coups = coups_possible(x, y, chemin)

    for next_coup in coups:
        # print(f"({x}, {y}) > ({next_coup[0]}, {next_coup[1]}) = {len(chemin)} cases remplies")
        # afficher_tableau(chemin)
        # print("\n")
        chemin_final = backtracking(next_coup[0], next_coup[1], chemin)
        if chemin_final:
            return chemin_final
    
    chemin.pop()
    return None

def coups_possible(X, Y, chemin):
    result = []

    for x, y in COUPS_CAVALIERS:
        if coup_possible(X+x, Y+y, chemin):
            result.append([X+x, Y+y])
    
    return result

def coup_possible(x,  y, chemin):
    return (0 <= x < WIDTH and 0 <= y < HEIGHT and (x, y) not in chemin)

res = backtracking(5, 1)
print(res)

afficher_tableau(res)
