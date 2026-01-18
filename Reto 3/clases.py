import random as ra
import pygame as pg
class Rectangulo:
    def __init__(self, x, y, w, h, velocidad):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.velocidad = velocidad
        self.color = (255, 255, 255)

    def mover(self):
        self.y += self.velocidad
        if self.y > 600:
            self.y = ra.randint(-100, 0)
            self.x = ra.randint(0, 800)

    def dibujar(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.x, self.y, self.w, self.h))