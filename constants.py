import pygame as pg, math
from random import randint
from time import sleep, time

RAD_DEG_CONVERTER = 57.2958 # 1 radian = 57.2958 degrés
COUPS_CAVALIERS = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)) # déplacements possibles du cavaliers

# Couleurs
GREY = (222, 222, 222)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Dimensions et marges de la fenêtre d'affichage (W pour WINDOW)
W_WIDTH = 1080
W_HEIGHT = 720
W_PADDING = 20

# C pour CHESSBOARD
C_SIDE_MAX = W_HEIGHT-(W_PADDING*2) # Taille maximale de l'échiquier
C_BORDER = 3 # Épaisseur de la bordure

C_WIDTH = 8 # Nombre de cases dans la largeur (les x)
C_HEIGHT = 8 # Nombre de cases dans la hauteur (les y)

C_CASE_LENGTH = C_SIDE_MAX//C_WIDTH if C_SIDE_MAX//C_WIDTH <= C_SIDE_MAX//C_HEIGHT else C_SIDE_MAX//C_HEIGHT # Calcul de la taille d'une case en prenant le minimum parmi les deux tailles possibles

C_SIDE_HEIGHT = C_HEIGHT * C_CASE_LENGTH # Hauteur effective de l'échiquier
C_SIDE_WIDTH = C_WIDTH * C_CASE_LENGTH # Largeur effective de l'échiquier

C_LEFT = (W_WIDTH+400-(C_SIDE_WIDTH))//2-W_PADDING # Coordonnée en x du point supérieur gauche de l'échiquier
C_TOP = (W_HEIGHT-(C_SIDE_HEIGHT))//2 # Coordonnée en y du point supérieur gauche de l'échiquier