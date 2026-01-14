import pygame as pg
from figura_class import Figura
import random as ra

#inicializar todos los modulos de pygmae (pantallas,objetos,sonidos,etc)
pg.init()
x_pos=800
y_pos=600
#crear pantallas o sourceface
pantalla = pg.display.set_mode( (x_pos,y_pos))#definicion de tamaño de pantalla
pg.display.set_caption("Intro Pygame")#agregar titulo en string a mi ventana

game_over = True

lista_circulos=[]
lista_rectangulos= []
#por cada vuelta del for voy guardando en lista un objeto figura con datos de entradas diferentes con el random.randint
for i in range(100):
    lista_circulos.append(Figura(ra.randint(0,800),ra.randint(0,600),color=(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),radio=ra.randint(10,100)))
    lista_rectangulos.append(Figura(ra.randint(0,800),ra.randint(0,600),color=(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),w=ra.randint(10,100),h=ra.randint(10,100)))

while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill((74,208,245))#asignar el color de pantalla en rgb
    
    #recorremos la lista de circulos cargada y llamamos a los metodos de mover y dibujar para que muestre en pantalla
    
    """for circulo in lista_circulos:
        circulo.mover(x_pos,y_pos)
        circulo.dibujar_circulo(pantalla)

    for rectangulo in lista_rectangulos:
        rectangulo.mover(x_pos,y_pos)
        rectangulo.dibujar_rectangulo(pantalla)"""

    for i in range(100):
        lista_circulos[i].mover(x_pos,y_pos)
        lista_rectangulos[i].mover(x_pos,y_pos)
        lista_circulos[i].dibujar_circulo(pantalla)
        lista_rectangulos[i].dibujar_rectangulo(pantalla)
        
    


    pg.display.flip()#funcion para recargar toda la configuracion que va 


#cierre de pantalla
pg.quit()