import pygame as pg
from figura_class import Rectangulo,Circulo

#inicializar todos los modulos de pygmae (pantallas,objetos,sonidos,etc)
pg.init()
x_pos=800
y_pos=600
#crear pantallas o sourceface
pantalla = pg.display.set_mode( (x_pos,y_pos))#definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame")#agregar titulo en string a mi ventana

game_over = True
rectangulo1 = Rectangulo(0,300,(201,92,56))
rectangulo2 = Rectangulo(20,500)
rectangulo3 = Rectangulo(0,400,(222,22,55))
circulo1 = Circulo(200,500,(131,214,71),20)

while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False


    pantalla.fill((74,208,245))#asignar el color de pantalla en rgb
    
    rectangulo1.mover(x_pos,y_pos)
    rectangulo2.mover(x_pos,y_pos)
    circulo1.mover(x_pos,y_pos)
        
    #agregamos objeto a la pantalla
    #draw.rect(sourface,color en (rgb),posiciones (posicionX,posicionY,tamañoX, tamañoY)
    rectangulo1.dibujar(pantalla)
    rectangulo2.dibujar(pantalla)
    rectangulo3.dibujar(pantalla)
    circulo1.dibujar(pantalla)



    pg.display.flip()#funcion para recargar toda la configuracion que va 


#cierre de pantalla
pg.quit()