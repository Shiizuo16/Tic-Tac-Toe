import pygame
import sys

from src.const import *


class Main:

    def __init__(self):
        pygame.init()

        # Game Screen
        self.screen = pygame.display.set_mode((length, height))
    
    def mainloop(self):
        screen = self.screen

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

m = Main()
m.mainloop()
