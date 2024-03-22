from constants import *
from backtracking import *

def draw_chessboard(screen):
    """
    Fonction dessinant l'échiquier et renvoyant un dictionnaire où les coordonnées x et y d'une case renvoie le rectangle associé à la case.
    """
    chessboard_cases = {}

    for y in range(C_HEIGHT):
        for x in range(C_WIDTH):
            actual_case = pg.Rect(C_LEFT+(x*C_CASE_LENGTH), C_TOP+(y*C_CASE_LENGTH), C_CASE_LENGTH, C_CASE_LENGTH)
            chessboard_cases[(x, y)] = actual_case
            if ((x+y)%2 == 1):
                pg.draw.rect(screen, BLACK, actual_case, 0)
            else:
                pg.draw.rect(screen, GREY, actual_case, 0)
    
    return chessboard_cases

def affiche_chemin(chemin, chessboard_cases, screen):
    """
    Fonction dessinant à l'écran(screen) le chemin donné en paramètre grâce au dictionnaire de cases.
    """
    for i in range(len(chemin)-1):
        affiche_arrow(screen, chessboard_cases[chemin[i]].center, chessboard_cases[chemin[i+1]].center)
        pg.display.flip()
        sleep(0.25)

def affiche_arrow(screen, dep:tuple[int,int], arr:tuple[int,int]):
    """
    Fonction dessinant à l'écran(screen) une flèche partant d'un point de départ vers le point d'arrivée
    """
    pg.draw.line(screen, RED, dep, arr, C_BORDER)
    angle = get_angle(dep, arr)

    """
    Je vous avoue que je ne sais pas pourquoi il faut faire cela mais, dans le cas où le déplacement en x est supérieur à 0, la flèche est inversée. On ajoute donc 180 pour l'inverser à nouveau.
    """
    if ((arr[0] - dep[0]) > 0):
        angle = angle + 180
    
    pg.draw.line(screen, RED, get_coor_point(arr, angle-25), arr, C_BORDER)
    pg.draw.line(screen, RED, get_coor_point(arr, angle+25), arr, C_BORDER)

def get_angle(dep:tuple[int,int], arr:tuple[int,int]):
    """
    Fonction qui renvoie l'angle de direction de la flèche se situant entre le point de départ et d'arrivée
    """
    bc = (arr[1]-dep[1])
    ab = (arr[0]-dep[0])
    return math.atan(bc/ab)*RAD_DEG_CONVERTER

def get_coor_point(arr, angle, dist=20):
    """
    Fonction qui renvoie les coordonnées du point d'angle de direction `angle` allant jusqu'à `arr` et ayant une longueur de `dist` 
    """
    return (int(arr[0] + dist*math.cos(angle/RAD_DEG_CONVERTER)), int(arr[1] + dist*math.sin(angle/RAD_DEG_CONVERTER)))

def titre(screen, text=f"Échiquier {C_WIDTH}x{C_HEIGHT}", dest=(5, 25)):
    """
    Fonction qui affiche un titre en haut à gauche de la fenêtre
    """
    screen.blit(pg.font.Font("./open-sans/OpenSans-Bold.ttf", 50).render(text, False, BLACK), dest)

def log(screen, text, nb_log):
    """
    Fonction qui affiche un texte à gauche de la fenêtre en dessous du titre
    """
    if nb_log == 0:
        pg.draw.rect(screen, GREY, pg.Rect(5, 125, 350, 550))
        pg.draw.rect(screen, BLACK, pg.Rect(5, 125, 350, 550), C_BORDER)
    screen.blit(pg.font.Font("./open-sans/OpenSans-Regular.ttf", 30).render(text, False, BLACK), (10, 125+nb_log*50))


pg.init() # Initialisation de pygame
screen = pg.display.set_mode((W_WIDTH, W_HEIGHT)) # Création de l'écran
clock = pg.time.Clock() # Création d'une horloge pour limiter les FPS

running = True 
nb_log = 0 

# Dessin des premiers traits
screen.fill(GREY) # Remplissage de l'écran
chessboard = pg.Rect(C_LEFT-C_BORDER, C_TOP-C_BORDER, C_SIDE_WIDTH+(2*C_BORDER), C_SIDE_HEIGHT+(2*C_BORDER)) # Rectangle représentant l'échiquier
pg.draw.rect(screen, BLACK, chessboard, C_BORDER) # Dessin de la bordure de l'échiquier
titre(screen) # Ajout du titre

chessboard_cases = draw_chessboard(screen) # Dessin des cases de l'échiquier et récupération des cases

tous_chemins = {(x, y): None for x in range(WIDTH) for y in range(HEIGHT)} # Utile pour enregistrer les chemins déjà calculés
borders = {(x, y): False for x in range(WIDTH) for y in range(HEIGHT)} # Utile pour l'affichage de la bordure rouge          

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.__dict__["key"] == pg.K_ESCAPE: # Quitter si `echap` pressé
            running = False
    
    for y in range(C_HEIGHT):
        for x in range(C_WIDTH): # Pour chaque case
            
            if chessboard_cases[(x, y)].collidepoint(pg.mouse.get_pos()): # Si la souris est sur la case
                if (not borders[(x, y)]): # Si la case n'est pas enregistré comme étant déjà survolée
                    pg.draw.rect(screen, RED, chessboard_cases[(x, y)], C_BORDER)
                    borders[(x, y)] = True

                if (pg.mouse.get_pressed()[0]):
                    chessboard_cases = draw_chessboard(screen)
                    pg.display.flip()
                    if (tous_chemins[(x, y)] is None):
                        debut = time()
                        chemins = backtrackingChemin(x, y)
                        duree = time() - debut

                        tous_chemins[(x, y)] = chemins[:]

                        log(screen, "Tps d'exécution : {:.2f}s".format(duree), nb_log)
                        nb_log += 1
                        
                        for chemin in chemins:
                            if (x != ceil(WIDTH/2)-WIDTH%2): # (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2) # WIDTH%2 car lorsque WIDTH est impair, on ne doit pas prendre la symétrie axiale de la colonne du milieu, ce qui correspond à la valeur de cette formule(`ceil(WIDTH/2)-WIDTH%2`)
                                tous_chemins[(symetrie_axiale_point_x(x), y)] = symetrie_axiale_chemin_x(chemin)

                            if (y != ceil(HEIGHT/2)-HEIGHT%2): # (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1) # HEIGHT%2 car lorsque HEIGHT est impair, on ne doit pas prendre la symétrie axiale de la ligne du milieu, ce qui correspond à la valeur de cette formule(`ceil(HEIGHT/2)-HEIGHT%2`)
                                tous_chemins[(x, symetrie_axiale_point_y(y))] = symetrie_axiale_chemin_y(chemin)

                            if (x != ceil(WIDTH/2)-WIDTH%2 and y != ceil(HEIGHT/2)-HEIGHT%2): # (0, 0), (0, 1), (1, 0), (1, 1)
                                tous_chemins[(symetrie_axiale_point_x(x), symetrie_axiale_point_y(y))] = symetrie_axiale_chemin_x(symetrie_axiale_chemin_y(chemin))


                    log(screen, f"({x}, {y}) : {len(tous_chemins[(x, y)])} chemins", nb_log)
                    nb_log += 1
                    if (nb_log == 11):
                        nb_log = 0
                    if (len(tous_chemins[(x, y)])):
                        affiche_chemin(tous_chemins[(x, y)][randint(0, len(tous_chemins[(x, y)]))], chessboard_cases, screen)
            else:
                if (borders[(x, y)]):
                    borders[(x, y)] = False
                    if ((x+y)%2 == 1):
                        pg.draw.rect(screen, (0, 0, 0), chessboard_cases[(x, y)], C_BORDER)
                    else:
                        pg.draw.rect(screen, GREY, chessboard_cases[(x, y)], C_BORDER)
    
    pg.display.flip()
    clock.tick(60)

pg.quit()