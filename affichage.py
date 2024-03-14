import pygame as pg

pg.init()
screen = pg.display.set_mode((1080, 720))
clock = pg.time.Clock()
running = True

screen.fill((222, 222, 222))

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.__dict__["key"] == pg.K_ESCAPE:
            running = False
    
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(20, 20, 1040, 680), 3)

    pg.display.flip()

    clock.tick(60)

pg.quit()