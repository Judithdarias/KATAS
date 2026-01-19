import pygame as pg
from figura_class import Raqueta,Pelota
pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("PONG")

raqueta1 = Raqueta(10,300)
raqueta2 = Raqueta(800,300)
pelota = Pelota(400,300,color =(225,232,70))

#definir tiempo de tasa de refresco dentro del bucle que fotogramas fps=fotograma por segundo
tasa_refresco= pg.time.Clock()


#agregar texto marcadores,funte y tamaño de letra
marcador1_font=pg.font.SysFont("verdana",30)
marcador2_font=pg.font.SysFont("verdana",30)

#asignacion de color y texto
marcador1 = marcador1_font.render("10",True,(255,255,255))
marcador2 = marcador2_font.render("10",True,(255,255,255))

game_over = True
while game_over:
       #obtenemos la tasa de refresco en milisegundos
    valor_tasa = tasa_refresco.tick(300)#variable para controlar la velocidad entre fotogramas
    #print(valor_tasa)
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = False
  
    pelota.mover(800,600)    
    
    pantalla_principal.fill((53,104,45))

    """
    pg.draw.line(pantalla_principal,(255,255,255),(400,0),(400,600),width=10)
    """
    
    x = 400
    raya = 15   
    espacio = 10   
    y = 0

    while y < 600:
        pg.draw.line(pantalla_principal,(255, 255, 255),(x, y),(x, y + raya),width=10)
        y += raya + espacio

    
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    pelota.dibujar(pantalla_principal)
    
    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    print("raqueta1:",pelota.contadorDerecho)
    print("raqueta2:",pelota.contadorIzquierdo)
    pelota.mostrar_marcador(pantalla_principal)

    pg.display.flip()



pg.quit()