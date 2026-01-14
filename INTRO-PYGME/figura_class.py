import pygame as pg

class Figura:
    def __init__(self,pos_x,pos_y,color=(255,255,255),w=30,h=30,radio=30):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.radio = radio 
        self.vx = 1
        self.vy = 1

    def mover(self,x_max,y_max):
        self.pos_x = self.pos_x + self.vx
        self.pos_y = self.pos_y + self.vy
        if self.pos_x==0 or self.pos_x == x_max:
            self.vx = self.vx*-1 
        if self.pos_y==0 or self.pos_y == y_max:
            self.vy = self.vy*-1 

    def dibujar_rectangulo(self,sourface):
        pg.draw.rect(sourface,self.color,(self.pos_x,self.pos_y,self.w,self.h))

    def dibujar_circulo(self,sourface):
        pg.draw.circle(sourface,self.color,(self.pos_x,self.pos_y),self.radio)
        
    