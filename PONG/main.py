import pygame as pg
from figura_class import Raqueta,Pelota
pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("PONG")

raqueta1 = Raqueta(10,300)
raqueta2 = Raqueta(800,300)
pelota = Pelota(400,300,color =(225,232,70))

game_over = True
while game_over:
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over=False
    pantalla_principal.fill((53,104,45))

    pg.draw.line(pantalla_principal,(255,255,255),(400,0),(400,600),width=10)

    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    pelota.dibujar(pantalla_principal)
    
    pg.display.flip()



pg.quit()