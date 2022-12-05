import pygame
from src.const import *
from src.menuText import colors

class Button:

    def __init__(self, h, l, xcor, ycor=0, color=colors.get('englishViolet'),scale=0): #248,237,235
        self.height = h
        self.length = l
        self.X = xcor
        self.Y = length+(menuHeight-self.height)//2 if ycor == 0 else ycor
        self.rect = (self.X, self.Y, length, height)
        self.color = color
        self.scale = scale


    # Blitting
    def setButton(self, texture):
        self.img = pygame.image.load(texture)
        if self.scale != 0:
            self.img = pygame.transform.scale(self.img, (self.length-self.scale, self.height-self.scale))
        self.center = self.X+self.length//2, self.Y+self.height//2
        self.textureRect = self.img.get_rect(center=self.center)

    def setMenuButton(self, texture):
        self.img = pygame.image.load(texture)
        if self.scale != 0:
            self.img = pygame.transform.scale(self.img, (self.length-self.scale, self.height-self.scale))
        self.center = self.X, self.Y
        self.textureRect = self.img.get_rect(center=self.center)

    def blitButton(self, surface):       
        surface.blit(self.img, self.textureRect)

