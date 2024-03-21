from constants import *

S = [[-1 for x in range(C_WIDTH)] for y in range(C_HEIGHT)]

def coups_possibles_chemin(X, Y):
    """
    Fonction qui renvoie une liste des coordonnées des cases auxquelles le cavalier peut se rendre pour un chemin hamiltonien
    """
    result = []

    for x, y in COUPS_CAVALIERS:
        if case_valide_chemin(X+x, Y+y):
            result.append([X+x, Y+y])
    
    return result

def case_valide_chemin(x,  y):
    """
    Fonction qui renvoie `True` si la case est dans l'échiquier. Renvoie `False` sinon
    """
    return (0 <= x < C_WIDTH and 0 <= y < C_HEIGHT and S[x][y] == -1)

def key_sorting(case):
    return A[case[0]][case[1]]

def AVisiter(case):
    return sorted(coups_possibles_chemin(case[0], case[1]),key=key_sorting)

def MAJAcces(case, k, chgmnt):
    res = A[case[0]][case[1]]

    A[case[0]][case[1]] = k
    for x, y in coups_possibles_chemin(case[0], case[1]):
        A[x][y] += chgmnt

    return res

def get_chemin():
    res = [-1 for _ in range(64)]

    for y in range(C_HEIGHT):
        for x in range(C_WIDTH):
            res[S[x][y]-1] = [x, y]
    
    return res

def placerCavalier(case=[0, 0], etape=1):
    if (etape == C_WIDTH*C_HEIGHT):
        Ss.append(get_chemin())
    else:
        V = AVisiter(case)
        for i in range(len(V)):
            k = MAJAcces(case, 0, -1)
            S[case[0]][case[1]] = etape
            placerCavalier(V[i], etape + 1)
            S[case[0]][case[1]] = -1
            MAJAcces(case, k, 1)

A = [[len(coups_possibles_chemin(x, y)) for x in range(C_WIDTH)] for y in range(C_HEIGHT)]
Ss = []

placerCavalier()
print(len(Ss))