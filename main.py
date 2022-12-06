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
            if not self.game.boxesDone:
                self.game.checkBoxes()

            self.screen.fill(colors.get('ming'))
            if self.showing == 0:
                self.game.showMenuScreen()
                self.game.menu.showBoxes()
                self.game.menu.showMenuStuff()

            else:
                self.game.showSquares()
                self.game.showPieces()


            # Bottom menu
            self.game.showMenu()
            self.game.showButtons()

            # Player turn text
            if self.showing == 1 and not(self.game.won or self.game.draw):
                self.game.showText()

            # Game Won
            elif self.game.won:
                if self.showing == 1:
                    self.game.line.showLine(self.screen)
                self.game.showWinner()
            
            # Game Draw
            elif self.game.draw:
                self.game.showDraw()
     

            for event in pygame.event.get():

                # Mouse button clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print('mouse down')
                    # Updating mouse position
                    mouse.update(event.pos)

                    # Clicked Input box
                    if not self.game.menu.active:
                        self.game.inputBoxClicked(event.pos)
                    
                    # Clicked row/col
                    clickedRow = mouse.y // sqSize
                    clickedCol = mouse.x // sqSize
                    print(clickedRow, clickedCol)

                    # Button clicked
                    if clickedRow == 3 and not self.game.menu.active:
                        print('clicked bottom bar') 
                        # Play/Pause
                        if mouse.x > self.game.buttons[0].X and mouse.x < self.game.buttons[0].Y:
                            if not (self.game.won or self.game.draw):
                                mouse.button = 'menu'
                                print('menu clicked')
                            else:
                                mouse.button = 'next'
                                print('next clicked')
                        # Reset
                        elif mouse.x < self.game.buttons[0].length and mouse.x < self.game.buttons[0].Y:
                            mouse.button = 'restart'
                            print('restart clicked')
                
                 # Mouse Button released
                elif event.type == pygame.MOUSEBUTTONUP:
                    button = mouse.button

                    if clickedRow<3 and self.showing == 1 and not self.game.won and not self.game.draw:
                        self.game.squareClicked(clickedRow, clickedCol)
                        self.game.turnImage()
                        # self.game.board.showGrid()
                        # print()

                        if not(self.game.won or self.game.draw): # game still running
                            # Checking for win
                            won,num,line =  self.game.board.calcWin()
                            if won:
                                print('game won', num, line)
                                self.game.won = True
                                # red line
                                self.game.line.dir = line
                                self.game.line.setLine()
                                
                                # next button
                                side = self.game.buttons[0].length
                                self.game.buttons[0].setButton("assets\\buttons-48px\\next.png")

                                # winner num
                                self.game.num = num
                                self.game.turn = int(num)
                                self.game.setWinner()
                                
                            
                            # Checking Draw
                            elif self.game.board.calcDraw():
                                print('game draw')
                                self.game.draw = True

                                # next button
                                side = self.game.buttons[0].length
                                self.game.buttons[0].setButton("assets\\buttons-48px\\next.png")

                                # winner num
                                self.game.num = num

                                self.showing = 0
                                self.game.changePlayPause(0)
                                

                            
            

                    # Menu Screen
                    elif clickedRow<3 and self.showing == 0 and not self.game.won and not self.game.draw:
                        button = self.game.menu.buttons[0]
                        button2 = self.game.menu.buttons[1]
                        x,y = button.X,button.Y
                        x2,y2 = button2.X,button2.Y 

                        # Scores button
                        if x-128<mouse.x<x+128 and y-64<mouse.y<y+64:
                            print('scores button clicked')
                            self.game.printScores()
                        # Reset Button
                        if x2-128<mouse.x<x2+128 and y2-64<mouse.y<y2+64:
                            print('reset button clicked')
                            ch = input('\nReset the scores? (Y/n)\n:: ').strip()
                            if ch == 'Y':
                                self.game.scores.initializeFiles()
                                print('Game Reset successful.')
                                for box in self.game.menu.boxes:
                                    box.text = box.renderText = ""
                                    box.active = False
                                    box.done = False
                                self.game.boxesDone = False

                    # Next Button
                    elif mouse.button == 'next':
                        if self.game.won:
                            self.game.changePlayPause(0)
                            # Saveing score
                            self.game.saveScore()
                            # Reseting box and boxes
                            self.game.board.clear()
                            # Menu; reseting flag variables
                            self.showing = 0
                            self.game.won = self.game.draw = False
                            # Reseting game
                            self.game.initializeGame()
                        elif self.game.draw:
                            self.game.board.clear()
                            # Menu; reseting flag variables
                            self.showing = 1
                            self.game.won = self.game.draw = False
                            # Reseting game
                            self.game.initializeGame()


                    else:
                        # Menu Button
                        if mouse.button == 'menu':
                            if self.game.boxesDone:
                                self.showing = 0 if self.showing==1 else 1
                                self.game.changePlayPause(self.showing)
                            


                        # Restart button
                        elif mouse.button == 'restart':
                            self.game.board.clear()
                            self.showing = 0
                            self.game.changePlayPause(0)
                        mouse.button = None


                elif event.type == pygame.KEYDOWN:
                    if self.game.menu.active:
                        if event.key == pygame.K_RETURN:
                            self.game.nextBox()
                            # self.game.inactivateBox(self.game.menu.activeBox)
                            if mouse.button == 'menu':
                                if self.game.boxesDone:
                                    self.showing = 0 if self.showing==1 else 1
                                    self.game.changePlayPause(self.showing)
                                    mouse.button = None
                        elif event.key == pygame.K_BACKSPACE:
                            self.game.delText()
                        else:
                            self.game.writeText(event.unicode)

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

m = Main()
m.mainloop()
