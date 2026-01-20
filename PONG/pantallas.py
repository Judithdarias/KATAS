import pygame as pg
from figura_class import *

ANCHO=800
ALTO=600
COLOR_PELOTA=(225, 232, 70)
COLOR_FONDO=(53,104,45)

class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption( "PONG" )
        self.tasa_refresco =pg.time.Clock()
        self.pelota = Pelota(ANCHO//2,ALTO//2,color=COLOR_PELOTA)
        self.raqueta1 = Raqueta(20,ANCHO//2)
        self.raqueta2 = Raqueta(ANCHO,ALTO//2)

    def bucle_fotograma(self):
        game_over = True
        while game_over:
            self.valor_tasa = self.tasa_refresco.tick(300)
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    game_over = False
        
            self.pelota.mover(ANCHO,ALTO)    
            self.pantalla_principal.fill(  COLOR_FONDO )

            for i in range(0,600,30):
                pg.draw.line(self.pantalla_principal,(255,255,255),(400,i),(400,i+15),width=10)

            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.pelota.dibujar(self.pantalla_principal)

            self.raqueta1.mover(pg.K_w,pg.K_s)
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)

            self.pelota.comprobar_choqueV2(self.raqueta1,self.raqueta2)  
            self.pelota.mostrar_marcador(self.pantalla_principal)

            
            
            pg.display.flip()        


juego = Partida()
juego.bucle_fotograma()