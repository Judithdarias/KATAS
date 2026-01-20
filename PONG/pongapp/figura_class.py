import pygame as pg
from utils import *
class Raqueta:
    def __init__(self,posx,posy,color=(COLOR_BLANCO),w=10,h=50):
        self.pos_x = posx
        self.pos_y = posy
        self.color = color
        self.w = w
        self.h = h
    
    def dibujar(self,screen):
        pg.draw.rect(screen,self.color,(self.pos_x-(self.w),(self.pos_y-self.h//2),self.w,self.h))

    def mover(self,teclado_arriba,teclado_abajo):
        teclado = pg.key.get_pressed()
    
        if teclado[teclado_arriba] ==True and self.pos_y >=0+(self.h//2):
            self.pos_y = self.pos_y -1
        if teclado[teclado_abajo]==True and self.pos_y <=600-(self.h//2):
            self.pos_y = self.pos_y +1
    @property
    def p_derecho(self):
        return self.pos_x + (self.w//2)
    @property
    def p_izquierdo(self):
        return self.pos_x - (self.w//2)
    @property
    def p_arriba(self):
        return self.pos_y - (self.h//2)
    @property
    def p_abajo(self):
        return self.pos_y + (self.h//2)
class Pelota:
    def __init__(self,posx,posy,color=(COLOR_BLANCO),radio=20):
        self.pos_x = posx
        self.pos_y = posy
        self.color = color
        self.radio = radio    
        self.vx = 1
        self.vy = 1
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0


    def dibujar(self,screen):
        pg.draw.circle(screen,self.color,(self.pos_x,self.pos_y),self.radio)

    def mover(self,xmax,ymax):
        self.pos_x = self.pos_x + self.vx
        self.pos_y = self.pos_y - self.vy
        
        #limite derecho
        if self.pos_x >= xmax+(8*self.radio):         
            self.contadorIzquierdo +=1
            self.pos_x = 400
            self.pos_y = 300 
            self.vx = self.vx*-1   
        #limite izquierdo
        if self.pos_x <=0-(8*self.radio):
            self.contadorDerecho +=1
            self.pos_x = 400
            self.pos_y = 300 
            self.vx = self.vx*-1   
            
        

        if self.pos_y >= ymax-(self.radio) or self.pos_y <=0+(self.radio):
            self.vy = self.vy*-1   
    
    def mostrar_marcador(self,pantalla_principal):
        marcador_font=pg.font.SysFont("arial",30)
    

        marcador1 = marcador_font.render(str(self.contadorIzquierdo),True,(255,255,255))
        marcador2 = marcador_font.render(str(self.contadorDerecho),True,(255,255,255))
        
        jugador1 = marcador_font.render("Jugador1",True,(255,255,255))
        jugador2 = marcador_font.render("Jugador2",True,(255,255,255))


        pantalla_principal.blit(marcador1,(320,50))
        pantalla_principal.blit(marcador2,(450,50))
        pantalla_principal.blit(jugador1,(280,20))
        pantalla_principal.blit(jugador2,(420,20))

    @property
    def p_derecho(self):
        return self.pos_x + (self.radio)
    @property
    def p_izquierdo(self):
        return self.pos_x - (self.radio)
    @property
    def p_arriba(self):
        return self.pos_y - (self.radio)
    @property
    def p_abajo(self):
        return self.pos_y + (self.radio)
    
    def comprobar_choque(self,r1,r2):
        #logica de choque
        if self.p_derecho >= r2.p_izquierdo and\
            self.p_arriba <= r2.p_abajo and \
            self.p_abajo >= r2.p_arriba:
            self.vx = self.vx *-1
        if self.p_izquierdo <= r1.p_derecho and\
            self.p_arriba <= r1.p_abajo and \
            self.p_abajo >= r1.p_arriba:
            self.vx = self.vx *-1 
    
    def comprobar_choqueV2(self,*raquetas):
        #logica de choque
        for r in raquetas:
            if self.p_derecho >= r.p_izquierdo and\
                self.p_izquierdo <= r.p_derecho and\
                self.p_arriba <= r.p_abajo and \
                self.p_abajo >= r.p_arriba:
                self.vx = self.vx *-1     

    

