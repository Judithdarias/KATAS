import pygame as pg 
import random as ra
from clases import Rectangulo

pg.init()
pantalla=pg.display.set_mode((800,600))
pg.display.set_caption("LLUVIA")

game_over = True

lista_rectangulos=[]
for i in range(250):
    rect = Rectangulo(ra.randint(0, 800),ra.randint(-600, 0),5,10,ra.randint(2, 6))
    lista_rectangulos.append(rect)

clock = pg.time.Clock()    
while game_over:
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((0,0,0))

    for rect in lista_rectangulos:
        rect.mover()
        rect.dibujar(pantalla)
    
    clock.tick(60)
    pg.display.flip()

pg.quit()
