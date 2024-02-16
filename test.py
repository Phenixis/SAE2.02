WIDTH = HEIGHT = 8

def backtracking(x, y, chemin=None):
    if chemin == None:
        chemin = []
    
    chemin.append((x, y))

    if (len(chemin) == WIDTH*HEIGHT):
        return chemin

    coups = coups_possible(x, y, chemin)

    for coup in coups:
        chemin_final = backtracking(coup[0], coup[1], chemin)
        if chemin_final:
            return chemin_final
    
    chemin.pop
    return None

def coups_possible(X, Y, chemin):
    result = []

    for x, y in [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]:
        if (0 <= (X+x) < WIDTH and 0 <= (Y+y) < HEIGHT and (X+x, Y+y) not in chemin):
            result.append([X+x, Y+y])
    
    return result

res = backtracking(0,0)
tab = [[-1 for y in range(HEIGHT)] for x in range(WIDTH)]

for i in range(len(res)):
    tab[res[i][0]][res[i][1]] = i

for ligne in tab:
    print(ligne)