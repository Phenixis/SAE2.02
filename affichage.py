import pygame as pg

W_WIDTH = 1080
W_HEIGHT = 720
W_PADDING = 20

C_SIDE = W_HEIGHT-(W_PADDING*2)
C_LEFT = W_WIDTH-(C_SIDE+W_PADDING)
C_TOP = W_PADDING

C_SIDE_CASES = 5

pg.init()
screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pg.time.Clock()
running = True

screen.fill((222, 222, 222))

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.__dict__["key"] == pg.K_ESCAPE:
            running = False
    
    chessboard = pg.Rect(C_LEFT, C_TOP, C_SIDE, C_SIDE)
    pg.draw.rect(screen, (0, 0, 0), chessboard, 3)

    for x in range(C_SIDE_CASES):
        for y in range(C_SIDE_CASES):
    

    pg.display.flip()

    clock.tick(60)

pg.quit()