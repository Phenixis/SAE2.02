from constants import *
from test import *

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

def affiche_arrow(screen, dep, arr):
    """
    Fonction dessinant à l'écran(screen) une flèche entre le point dep et le point arr
    """
    pg.draw.line(screen, RED, dep, arr, C_BORDER)
    angle = get_angle(dep, arr)

    """
    Je vous avoue que je ne sais pas pourquoi il faut faire cela mais, dans le cas où le déplacement en x est supérieur à 0, la flèche est inversée. On ajoute donc 180 pour l'inverser à nouveau.
    """
    if ((arr[0] - dep[0]) > 0):
        angle = angle + 180
    
    pg.draw.line(screen, RED, get_point(arr, angle-25), arr, C_BORDER)
    pg.draw.line(screen, RED, get_point(arr, angle+25), arr, C_BORDER)

def get_angle(dep, arr):
    bc = (arr[1]-dep[1])
    ab = (arr[0]-dep[0])
    return math.atan(bc/ab)*RAD_DEG_CONVERTER

def get_point(arr, angle):
    return (int(arr[0] + 20*math.cos(angle/RAD_DEG_CONVERTER)), int(arr[1] + 20*math.sin(angle/RAD_DEG_CONVERTER)))

def titre(screen, text=f"Échiquier {C_WIDTH}x{C_HEIGHT}", dest=(5, 25)):
    screen.blit(pg.font.Font("./open-sans/OpenSans-Bold.ttf", 50).render(text, False, BLACK), dest)

def log(screen, text, nb_ops):
    if nb_ops == 0:
        pg.draw.rect(screen, GREY, pg.Rect(5, 125, 300, 550))
        pg.draw.rect(screen, BLACK, pg.Rect(5, 125, 300, 550), C_BORDER)
    screen.blit(pg.font.Font("./open-sans/OpenSans-Regular.ttf", 30).render(text, False, BLACK), (10, 125+nb_ops*50))

pg.init()

screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pg.time.Clock()
running = True
nb_ops = 0

screen.fill(GREY)
chessboard = pg.Rect(C_LEFT-C_BORDER, C_TOP-C_BORDER, C_SIDE_WIDTH+(2*C_BORDER), C_SIDE_HEIGHT+(2*C_BORDER))
pg.draw.rect(screen, BLACK, chessboard, C_BORDER)
titre(screen)

chessboard_cases = draw_chessboard(screen)

tous_chemins = {(x, y): None for x in range(WIDTH) for y in range(HEIGHT)}
borders = {(x, y): False for x in range(WIDTH) for y in range(HEIGHT)}               

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.__dict__["key"] == pg.K_ESCAPE:
            running = False
    
    for y in range(C_HEIGHT):
        for x in range(C_WIDTH):
            border = pg.Rect(chessboard_cases[(x, y)].x, chessboard_cases[(x, y)].y, C_CASE_LENGTH, C_CASE_LENGTH)
            if chessboard_cases[(x, y)].collidepoint(pg.mouse.get_pos()):
                if (not borders[(x, y)]):
                    pg.draw.rect(screen, RED, border, C_BORDER)
                    borders[(x, y)] = True

                if (pg.mouse.get_pressed()[0]):
                    chessboard_cases = draw_chessboard(screen)
                    pg.display.flip()
                    if (tous_chemins[(x, y)] is None):
                        tous_chemins[(x, y)] = backtracking(x, y)

                    log(screen, f"({x}, {y}) : {len(tous_chemins[(x, y)])} chemins", nb_ops)
                    nb_ops += 1
                    if (nb_ops == 11):
                        nb_ops = 0
                    if (len(tous_chemins[(x, y)])):
                        affiche_chemin(tous_chemins[(x, y)][randint(0, len(tous_chemins[(x, y)]))], chessboard_cases, screen)
            else:
                if (borders[(x, y)]):
                    borders[(x, y)] = False
                    if ((x+y)%2 == 1):
                        pg.draw.rect(screen, (0, 0, 0), border, C_BORDER)
                    else:
                        pg.draw.rect(screen, GREY, border, C_BORDER)
    
    pg.display.flip()
    clock.tick(60)

pg.quit()