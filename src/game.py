import pygame

from src.const import *
from src.board import Board


class Game:

    def __init__(self, screen):
        self.screen = screen

    def showBackground(self):
        for row in range(rows):
            for col in range(cols):
                
                # Picking color of squares
                color = (241,217,192) 
                rect = (col*rectSize + 1 , row*rectSize + 1, sqSize, sqSize) # rect 

                pygame.draw.rect(self.screen, color, rect) # drawing the rect