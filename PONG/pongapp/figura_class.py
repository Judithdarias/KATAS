import pygame as pg
from pongapp.utils import *

class Raqueta:
    def __init__(self,posx,posy,color=COLOR_BLANCO,w=20, h=120):
        self.pos_x = posx
        self.pos_y = posy
        self.color = color
        self.w = w
        self.h = h


    def dibujar(self,screen):
        pg.draw.rect(screen, self.color, (self.pos_x-(self.w),(self.pos_y-self.h//2),self.w,self.h) )

    def mover(self,teclado_arriba,teclado_abajo):
        teclado = pg.key.get_pressed() 
        if teclado[teclado_arriba]==True and self.pos_y >=0+(self.h//2):
            self.pos_y = self.pos_y - 1  
        if teclado[teclado_abajo] == True and self.pos_y <=600-(self.h//2):
            self.pos_y = self.pos_y + 1
    @property
    def p_derecho(self):
        return self.pos_x + (self.w//2)     
    @property
    def p_izquierdo(self):
        return self.pos_x - (self.w//2)
    @property
    def p_arriba(self):
        return self.pos_y -(self.h//2)
    @property
    def p_abajo(self):
        return self.pos_y +(self.h//2)   
       

class Pelota:
    def __init__(self,posx,posy,color=COLOR_BLANCO,radio=20):
        self.pos_x = posx
        self.pos_y = posy
        self.color = color
        self.radio = radio
        self.vx = 1
        self.vy = 1


    def dibujar(self,screen):
        pg.draw.circle(screen, self.color, (self.pos_x,self.pos_y), self.radio)

    def mover(self,xmax=ANCHO,ymax=ALTO):
        self.pos_x = self.pos_x + self.vx
        self.pos_y = self.pos_y - self.vy
        
        #limite derecho
        if self.pos_x >= xmax+(8*self.radio):         
            self.pos_x = ANCHO//2
            self.pos_y = ALTO//2 
            self.vx = self.vx*-1   
            return "derecho"
        #limite izquierdo
        if self.pos_x <=0-(8*self.radio):
            self.pos_x = ANCHO//2
            self.pos_y = ANCHO//2
            self.vx = self.vx*-1
            return "izquierdo"  
            
        

        if self.pos_y >= ymax-(self.radio) or self.pos_y <=0+(self.radio):
            self.vy = self.vy*-1    
   
    @property
    def p_derecho(self):
        return self.pos_x + self.radio
    @property
    def p_izquierdo(self):
        return self.pos_x - self.radio
    @property
    def p_arriba(self):
        return self.pos_y - self.radio
    @property
    def p_abajo(self):
        return self.pos_y + self.radio   

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