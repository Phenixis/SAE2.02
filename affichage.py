import pygame as pg
from random import randint
from time import sleep
from constants import *
from test import *

def draw_chessboard(screen):
    chessboard_cases = {}

    for y in range(C_SIDE_CASES):
        for x in range(C_SIDE_CASES):
            actual_case = pg.Rect(C_LEFT+(x*C_CASE_LENGTH), C_TOP+(y*C_CASE_LENGTH), C_CASE_LENGTH, C_CASE_LENGTH)
            chessboard_cases[(x, y)] = actual_case
            if ((x+y)%2 == 1):
                pg.draw.rect(screen, (0, 0, 0), actual_case, 0)
            else:
                pg.draw.rect(screen, GREY, actual_case, 0)
    
    return chessboard_cases

def affiche_chemin(chemin, chessboard_cases, screen):
    chessboard_cases = draw_chessboard(screen)
    for i in range(len(chemin)-1):
        pg.draw.line(screen, RED, chessboard_cases[chemin[i]].center, chessboard_cases[chemin[i+1]].center, C_BORDER)
        pg.display.flip()
        sleep(0.25)

def titre(screen, text=f"Échiquier {C_SIDE_CASES}x{C_SIDE_CASES}", dest=(5, 25)):
    screen.blit(pg.font.Font("./open-sans/OpenSans-Bold.ttf", 50).render(text, False, BLACK), dest)

def log(screen, text, nb_ops):
    screen.blit(pg.font.Font("./open-sans/OpenSans-Regular.ttf", 30).render(text, False, BLACK, GREY), (5, 125+nb_ops*50))
pg.init()

screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pg.time.Clock()
running = True
nb_ops = 0

screen.fill(GREY)
chessboard = pg.Rect(C_LEFT-C_BORDER, C_TOP-C_BORDER, C_SIDE+(2*C_BORDER), C_SIDE+(2*C_BORDER))
pg.draw.rect(screen, BLACK, chessboard, C_BORDER)
titre(screen)

chessboard_cases = draw_chessboard(screen)

tous_chemins = {(x, y): None for x in range(WIDTH) for y in range(HEIGHT)}
borders = {(x, y): False for x in range(WIDTH) for y in range(HEIGHT)}               

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.__dict__["key"] == pg.K_ESCAPE:
            running = False
    
    for y in range(C_SIDE_CASES):
        for x in range(C_SIDE_CASES):
            border = pg.Rect(chessboard_cases[(x, y)].x, chessboard_cases[(x, y)].y, C_CASE_LENGTH, C_CASE_LENGTH)
            if chessboard_cases[(x, y)].collidepoint(pg.mouse.get_pos()):
                if (not borders[(x, y)]):
                    pg.draw.rect(screen, RED, border, C_BORDER)
                    borders[(x, y)] = True

                if (pg.mouse.get_pressed()[0]):
                    if (tous_chemins[(x, y)] is None):
                        tous_chemins[(x, y)] = backtracking(x, y)

                    log(screen, f"({x}, {y}) : {format('3d', len(tous_chemins[(x, y)]))} chemins", nb_ops)
                    nb_ops += 1
                    if (nb_ops == 12):
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