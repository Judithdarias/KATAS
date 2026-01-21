import pygame as pg
from pongapp.figura_class import *
from pongapp.utils import *



class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption( "PONG" )
        self.tasa_refresco =pg.time.Clock()
        self.pelota = Pelota(ANCHO//2,ALTO//2,color=COLOR_PELOTA)
        self.raqueta1 = Raqueta(20,ALTO//2)
        self.raqueta2 = Raqueta(ANCHO,ALTO//2)
        #self.marcador_font = pg.font.SysFont("arial",30)
        #self.marcador_tiempo_font = pg.font.SysFont("arial",35)
        self.marcador_font = pg.font.Font("pongapp/fonts/PressStart2P.ttf",15)
        self.marcador_tiempo_font = pg.font.Font("pongapp/fonts/RussoOne.ttf",20)
        self.contadorDerecho=0
        self.contadorIzquierdo=0
        self.quienMarco = ""
        self.temporizador = TIEMPO_JUEGO
        self.game_over = True
        self.colorFondo=PISTA_VERDE
        self.contadorFotograma=0

    def bucle_fotograma(self):
        
        while self.game_over:
            self.valor_tasa = self.tasa_refresco.tick(TS)
            self.temporizador = self.temporizador - self.valor_tasa
      
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    self.game_over = False
            
            self.finalizacion_juego()
            #self.pantalla_principal.fill(  COLOR_FONDO )
            self.pantalla_principal.fill( self.fondo_juego()   )
            
            self.quienMarco = self.pelota.mover(ANCHO,ALTO) 

            

            self.mostrar_linea_central()

            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.pelota.dibujar(self.pantalla_principal)

            self.raqueta1.mover(pg.K_w,pg.K_s)
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)

            self.pelota.comprobar_choqueV2(self.raqueta1,self.raqueta2)  
            self.mostrar_marcador()
            
            pg.display.flip()        

        pg.quit()

    def mostrar_linea_central(self):
        for i in range(0,ALTO,30):
            pg.draw.line(self.pantalla_principal,COLOR_BLANCO,(ANCHO//2,i),(ANCHO//2,i+15),width=10)


    def mostrar_marcador(self):
        if self.quienMarco == "derecho":
            self.contadorIzquierdo+=1
        elif self.quienMarco =="izquierdo":
            self.contadorDerecho +=1
        marcador1 = self.marcador_font.render(str(self.contadorIzquierdo),True,COLOR_BLANCO)
        marcador2 = self.marcador_font.render(str(self.contadorDerecho),True,COLOR_BLANCO)
        jugador1 = self.marcador_font.render("Jugador 1",True,COLOR_AZUL)
        jugador2 = self.marcador_font.render("Jugador 2",True,COLOR_AZUL)
        tiempo_juego = self.marcador_tiempo_font.render(f"{int(self.temporizador/1000)}",True,COLOR_ROSA)
        #mostrar el texto definido y la posicion x, y donde se mostraran
        self.pantalla_principal.blit(marcador1,((ALTO//2)+20,50))
        self.pantalla_principal.blit(marcador2,((ANCHO//2)+50,50))
        self.pantalla_principal.blit(jugador1,((ALTO//2)-50,20))
        self.pantalla_principal.blit(jugador2,((ANCHO//2)+50,20))
        self.pantalla_principal.blit(tiempo_juego,(ANCHO//2,10))

        

    def finalizacion_juego(self):
        #finalizacion de juego por puntaje
        if self.contadorIzquierdo == 7:
            print(f"gana el Jugador1: {self.contadorIzquierdo}")
            self.game_over=False
        if self.contadorDerecho == 7:
            print(f"gana el Jugador2 {self.contadorDerecho}")
            self.game_over=False    

        #finalizacion de juego por tiempo
        if self.temporizador <= 0:
            print("fin del juego")
            self.game_over = False   

    def fondo_juego(self):
        self.contadorFotograma += 1
        #los 10 segundos
        if self.temporizador > 10000:
            self.contadorFotograma= 0
        elif self.temporizador > 5000:
            if self.contadorFotograma == 80:
                if self.colorFondo == PISTA_VERDE:
                    self.colorFondo = PISTA_NARANJA
                else:
                    self.colorFondo = PISTA_VERDE
                self.contadorFotograma = 0        
        #los 5 segundos
        else:

            if self.contadorFotograma == 80:
                if self.colorFondo == PISTA_VERDE or self.colorFondo == PISTA_NARANJA:
                    self.colorFondo = PISTA_ROJA
                else:
                    self.colorFondo = PISTA_VERDE
                self.contadorFotograma = 0

        return self.colorFondo   