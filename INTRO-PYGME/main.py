import pygame as pg

#inicializar todos los modulos de pygmae (pantallas,objetos,sonidos,etc)
pg.init()

#crear pantallas o sourceface
pg.display.set_mode( (800,600))#definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame")#agregar titulo en string a mi ventana

game_over = True

while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

#cierre de pantalla
pg.quit()