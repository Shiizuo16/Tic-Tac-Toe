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
                self.game.menu.showBoxes()
                
            else:
                self.game.showSquares()
                self.game.showPieces()

                



            

            # Bottom menu
            self.game.showMenu()
            self.game.showButtons()
            if self.showing == 1 and not(self.game.won or self.game.draw):
                self.game.showText()
            elif self.game.won:
                    if self.showing == 1:
                        self.game.line.showLine(self.screen)
                    self.game.showWinner()

            
                

            for event in pygame.event.get():
                # Mouse button clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Updating mouse position
                    mouse.update(event.pos)

                    # Clicked Input box
                    if not self.game.menu.active:
                        self.game.inputBoxClicked(event.pos)
                    
                    # Clicked row/col
                    clickedRow = mouse.y // sqSize
                    clickedCol = mouse.x // sqSize

                    # Button clicked
                    if clickedRow == 3 and not self.game.menu.active: 
                        # Play/Pause
                        if mouse.x > self.game.buttons[0].X and mouse.x < self.game.buttons[0].Y:
                            mouse.button = 'menu'
                            print('menu clicked')
                        # Reset
                        elif mouse.x < self.game.buttons[0].length and mouse.x < self.game.buttons[0].Y:
                            mouse.button = 'reset'
                            print('reset clicked')
                
                 # Mouse Button released
                elif event.type == pygame.MOUSEBUTTONUP:
                    button = mouse.button

                    if clickedRow<3 and self.showing == 1 and not self.game.won and not self.game.draw:
                        self.game.squareClicked(clickedRow, clickedCol)
                        self.game.turnImage()
                        self.game.board.showGrid()
                        print()

                        if not(self.game.won or self.game.draw):
                            # Checking Draw
                            if self.game.board.calcDraw():
                                print('game draw')
                                self.game.draw = True
                                self.showing = 0
                            
                            # Checking for win
                            won,num,line =  self.game.board.calcWin()
                            if won:
                                print('game won', num, line)
                                self.game.won = True
                                self.game.line.dir = line
                                self.game.line.setLine()
                                self.game.num = num
                                side = self.game.buttons[0].length
                                self.game.center = length//2+side*1.5, length+(menuHeight//2)
                                self.game.textureRect = self.game.image.get_rect(center=self.game.center)
                                self.game.buttons[0].setButton("assets\\buttons-48px\\next.png")

                    else:
                        # Menu Button
                        if mouse.button == 'menu':
                            self.showing = 0 if self.showing==1 else 1
                            self.game.changePlayPause(self.showing)

                        # Reset button
                        elif mouse.button == 'reset':
                            self.game.board.clear()
                            self.showing = 0
                            self.game.buttons[0].setButton("assets\\buttons-48px\play.png")
                            self.game.won = self.game.draw = False

                        mouse.button = None
                elif event.type == pygame.KEYDOWN:
                    if self.game.menu.active:
                        if event.key == pygame.K_RETURN:
                            self.game.inactivateBox()
                        elif event.key == pygame.K_BACKSPACE:
                            self.game.delText()
                        elif event.key == pygame.K_LEFT:
                            pass
                        elif event.key == pygame.K_RIGHT:   
                            pass
                        else:
                            self.game.writeText(event.unicode)

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

m = Main()
m.mainloop()
