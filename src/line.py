import pygame
from src.const import *

class Line:

    def __init__(self):
        self.dir = None
        self.texture = None
        self.textureRect = None

    def setLine(self):
        if self.dir == 'left':
            self.texture = pygame.image.load("assets\\red-line\\red-line-left.png")
            center = length//2, length//2
        elif self.dir == 'right':
            self.texture = pygame.image.load("assets\\red-line\\red-line-right.png")
            center = length//2, length//2
        elif self.dir[0] == 'v':
            self.texture = pygame.image.load("assets\\red-line\\red-line-vertical.png")
            row = int(self.dir[-1])
            center = rectSize*row + rectSize//2, length//2
        elif self.dir[0] == 'h':
            self.texture = pygame.image.load("assets\\red-line\\red-line-horizontal.png")
            col = int(self.dir[-1])
            center = length//2, rectSize*col + rectSize//2
        
        self.textureRect = self.texture.get_rect(center=center)
        
    def showLine(self,surface):
        surface.blit(self.texture, self.textureRect)