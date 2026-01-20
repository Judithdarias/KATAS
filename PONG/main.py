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

    for i in range(0,600,30):
        pg.draw.line(pantalla_principal,(255,255,255),(400,i),(400,i+15),width=10)

    
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    pelota.dibujar(pantalla_principal)
    
    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    
    #ogica de choque
    
    pelota.comprobar_choqueV2(raqueta1,raqueta2)
    pelota.mostrar_marcador(pantalla_principal)

    pg.display.flip()



pg.quit()