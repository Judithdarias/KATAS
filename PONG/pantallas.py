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
        self.marcador_font = pg.font.Font(FUENTE1,15)
        self.marcador_tiempo_font = pg.font.Font(FUENTE2,20)
        self.contadorDerecho=0
        self.contadorIzquierdo=0
        self.quienMarco = ""
        self.temporizador = TIEMPO_JUEGO
        self.game_over = True
        self.colorFondo=PISTA_VERDE
        self.contadorFotograma=0
        self.resultado=""

    def bucle_fotograma(self):
        
        while self.game_over:
            self.valor_tasa = self.tasa_refresco.tick(TS)
            self.temporizador = self.temporizador - self.valor_tasa
      
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    self.game_over = False
            
            self.finalizacion_juego()
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
        #finalizacion de juego por tiempo
        if self.temporizador <= 0:
            self.game_over = False 
            if self.contadorIzquierdo > self.contadorDerecho:
                self.resultado = f"Jugador1 - Resultado: Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"
            elif self.contadorIzquierdo < self.contadorDerecho:
                self.resultado= f"Jugador2 - Resultado: Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"
            else:
                self.resultado = f"Empate entre Jugador1 y Jugador2 - Resultado: Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"
             
            return self.resultado 
       
       #finalizacion de juego por puntaje
        if self.contadorIzquierdo == 7:
            #print(f"gana el Jugador1: {self.contadorIzquierdo}")
            self.game_over=False
            self.resultado = f"Jugador1 - Resultado: Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"
            return self.resultado
        if self.contadorDerecho == 7:
            #print(f"gana el Jugador2 {self.contadorDerecho}")
            self.game_over=False
            self.resultado = f"Jugador2 - Resultado: Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"
            return self.resultado

        
        
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


class Menu:
    pg.init()
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Menu")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(FONDO_MENU)
        self.fuente= pg.font.Font(FUENTE2,30)
        self.sonido = pg.mixer.Sound(SONIDO_MENU)

    def bucle_pantalla(self):
        game_over= True
        while game_over:
            pg.mixer.Sound.play(self.sonido)
            pg.mixer.Sound.set_volume(self.sonido,0.05)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False
        
            teclado = pg.key.get_pressed() 
            if teclado[pg.K_RETURN]==True:
                pg.mixer.Sound.stop(self.sonido)
                game_over = False
                return "partida"
            elif teclado[pg.K_r]==True:
                pg.mixer.Sound.stop(self.sonido)
                return "record"


            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            texto_menu = self.fuente.render("Pulsa ENTER para jugar",True,COLOR_BLANCO)
            self.pantalla_principal.blit(texto_menu,(250,(ALTO//2)-90))
            texto_record = self.fuente.render("Pulsa r para ver records",True,COLOR_BLANCO)
            self.pantalla_principal.blit(texto_record,(250,(ALTO//2)-50))
            pg.display.flip()

        pg.quit()    


class Resultado:
    def __init__(self,resultado):
        pg.init()
        self.pantala_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Resultado")
        self.tasa_refresco = pg.time.Clock()
        self.fuente_resultado = pg.font.Font(FUENTE2,15)
        self.resultado = resultado

    def bucle_pantalla(self):
        game_over=True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False 
            self.pantala_principal.fill(COLOR_BLANCO)
            texto_resultado= self.fuente_resultado.render(f"El ganador es: {self.resultado}",True,COLOR_ROSA)   
            self.pantala_principal.blit(texto_resultado,(150,ALTO//2))
            pg.display.flip()        


        pg.quit()


class Record:
    def __init__(self):
        pg.init()
        self.pantalla_principal= pg.display.set_mode((ANCHO,ALTO ))
        pg.display.set_caption("Mejores Puntajes")
        self.tasa_refresco = pg.time.Clock()
        self.fuente_record = pg.font.Font(FUENTE1)
        

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False

            self.pantalla_principal.fill(COLOR_BLANCO)
            texto= self.fuente_record.render(f"RECORD",True,COLOR_ROSA)   
            self.pantalla_principal.blit(texto,(ANCHO//2,ALTO//2))

            pg.display.flip()

        pg.quit()    
    def __init__(self,resultado):
        pg.init()
        self.pantala_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Resultado")
        self.tasa_refresco = pg.time.Clock()
        self.fuente_resultado = pg.font.Font(FUENTE2,30)
        self.resultado = resultado

    def bucle_pantalla(self):
        game_over=True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False 
            self.pantala_principal.fill(COLOR_BLANCO)
            texto_resultado= self.fuente_resultado.render(f"El ganador es: {self.resultado}",True,COLOR_ROSA)   
            self.pantala_principal.blit(texto_resultado,(200,ALTO//2))
            pg.display.flip()        


        pg.quit()