import pygame as pg

pg.init()

pantalla = pg.display.set_mode((800,600))
pg.display.set_caption("PONG")


game_over = True
while game_over:
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over=False
    pantalla.fill((123,179,105))

    pg.display.flip()


pg.quit()