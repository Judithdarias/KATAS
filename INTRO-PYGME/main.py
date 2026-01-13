import pygame as pg

#inicializar todos los modulos de pygmae (pantallas,objetos,sonidos,etc)
pg.init()

#crear pantallas o sourceface
pantalla = pg.display.set_mode( (800,600))#definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame")#agregar titulo en string a mi ventana

game_over = True
x = 0
vx = 1
while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False


    pantalla.fill((81,189,245))#asignar el color de pantalla en rgb

    x = x + vx
    if x==0 or x == 800:
        vx = vx*-1 
        
    #agregamos objeto a la pantalla
    #draw.rect(sourface,color en (rgb),posiciones (posicionX,posicionY,tamañoX, tamañoY)
    pg.draw.rect(pantalla, (158,36,156),(x,300-15,30,30))

    pg.display.flip()#funcion para recargar toda la configuracion que va 

#cierre de pantalla
pg.quit()