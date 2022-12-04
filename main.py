import pygame
import sys

from src.const import *
from src.game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.showing = 0    # (0 = menu, 1 = squares)
        
    
        # Game Screen
        self.screen = pygame.display.set_mode((length, height))
        self.game = Game(self.screen)

        
    def mainloop(self):
        mouse = self.game.mouse
        while True:
            if self.showing == 0:
                self.game.showMenuScreen()
            else:
                self.game.showSquares()
                self.game.showPieces()
            self.game.showMenu()
            self.game.showButtons()
                

            for event in pygame.event.get():
                # Mouse button clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Updating mouse position
                    mouse.update(event.pos)

                    # Clicked row/col
                    clickedRow = mouse.y // sqSize
                    clickedCol = mouse.x // sqSize

                    # Play/Pause clicked
                    if clickedRow == 3:
                        if mouse.x > self.game.buttons[0].X and mouse.x < self.game.buttons[0].Y:
                            mouse.button = 'menu'
                            print('menu clicked')
                
                 # Mouse Button released
                elif event.type == pygame.MOUSEBUTTONUP:
                    button = mouse.button

                    if clickedRow<3 and self.showing == 1:
                        print(clickedRow, clickedCol)
                        self.game.squareClicked(clickedRow, clickedCol)
                    else:

                        if mouse.button == 'menu':
                            self.showing = 0 if self.showing==1 else 1
                            self.game.changePlayPause(self.showing)
                            mouse.button = None


                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

m = Main()
m.mainloop()
