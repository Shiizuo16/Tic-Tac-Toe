import pygame

from src.const import *
from src.board import Board
from src.buttons import *
from src.mouse import Mouse
from src.line import Line
from src.menuText import *
from src.score import Scores
from src.menuScreen import Menu
from src.score import Scores
from random import randint

class Game:

    def __init__(self, screen):
        self.draw = False
        self.won = False
        self.screen = screen
        self.buttons = buttons
        self.mouse = Mouse()
        self.board = Board()
        self.line = Line()
        self.menu = Menu(screen)
        self.boxesDone = False
        self.scores = Scores()

        # players
        self.players = dict()

        # scores
        self.scores = Scores()

        self.initializeGame()


    def initializeGame(self):
        # player turn
        self.turn = randint(0, 1) # (0-->O, 1-->X)
        self.text = Text('Turn : ', length//2-side//2, length+(menuHeight//2))
        
        # Bottom Menu turn image
        self.image = pygame.image.load("assets\\buttons-48px\\dot.png") if self.turn == 0 else pygame.image.load("assets\\buttons-48px\\cross.png")
        self.center = length//2+side, length+(menuHeight//2)
        self.textureRect = self.image.get_rect(center=self.center)

        # winner
        self.winner = Text('Winner : ', length//2-side*0.75, length+(menuHeight//2))
        
        # Draw text
        self.draw_text = Text('DRAW', length//2, length+(menuHeight//2))

    def writePlayerNames(self):
        # Getting player names
        names = list()
        for box in self.menu.boxes:
            names.append(str(box.text).capitalize())

        # Existing player record? 
        for name in names:
            if not self.scores.playerExist(name):
                self.scores.addPlayer(name)

    def checkBoxes(self):
        for box in self.menu.boxes:
            if not box.done:
                self.boxesDone = False
                break
        else:
            self.boxesDone = True


    def changePlayPause(self, n):
        if n == 0:
            self.buttons[0].setButton("assets\\buttons-48px\play.png")
        else:
            self.buttons[0].setButton("assets\\buttons-48px\pause.png")
    
    def squareClicked(self, row, col):
        if self.board.squares[row][col].piece == -1: # doesn't have a piece
            self.board.squares[row][col].piece = self.turn
            if self.turn == 0:
                t = self.board.squares[row][col].texture = "assets\\buttons-128px\\dot.png"
                self.turn = 1
            else:
                t = self.board.squares[row][col].texture = "assets\\buttons-128px\\cross.png"
                self.turn = 0
            self.board.squares[row][col].img = pygame.image.load(t)
            center = col*rectSize + (rectSize)//2, row*rectSize + (rectSize)//2
            self.board.squares[row][col].textureRect = self.board.squares[row][col].img.get_rect(center=center)
    
    def turnImage(self):
        if self.turn == 0:
           self.image = pygame.image.load("assets\\buttons-48px\\dot.png")
        else:
            self.image = pygame.image.load("assets\\buttons-48px\\cross.png")


    def inputBoxClicked(self, pos):
        for box in self.menu.boxes:
            if box.rectangle.collidepoint(pos):
                self.activateBox(box)
            else:
                self.inactivateBox(box)

    def activateBox(self, box):
        box.active = True
        box.color = box.color_active

        self.menu.active = True
        self.menu.activeBox = box
                
    
    def inactivateBox(self, box):
        if box.text != '':
            box.active = False
            box.color = box.color_inactive
            box.done = True

            self.menu.active = False
            self.menu.activeBox = None

    def checkText(self):
        text = self.menu.activeBox.text
        if text != "":
            self.menu.active = False
        

    def nextBox(self):
        box = self.menu.activeBox
        index = self.menu.boxes.index(box)
        try:
            box2 = self.menu.boxes[index+1]
            box2.active = True
            box2.color = box.color_active
            self.menu.active = True
            self.menu.activeBox = box2
        except:
            self.boxesDone = True
            self.menu.active = False
            self.menu.activeBox = None
            self.mouse.button = 'menu'
            self.writePlayerNames()
        finally:
            box.color = box.color_inactive
            box.active = False
            box.done = True
            

    def writeText(self, char):
        box = self.menu.activeBox
        box.text += char
        l= box.font.size(box.renderText)[0]
        while l>box.length-side:
            box.renderText = box.renderText[1:]
            l = box.font.size(box.renderText)[0]

        box.renderText += char


    def delText(self):
        box = self.menu.activeBox

        if box.text != '':
            box.text = box.text[:-1]
            box.renderText = box.renderText[:-1]

            text_l = box.font.size(box.text)[0]
            if text_l>box.length-side:
                index = box.text.index(box.renderText)
                box.renderText = box.text[index-1] + box.renderText

    def saveScore(self):
        num = int(self.num)
        if num == 0:
            winner = self.menu.p2.text
            otherPlayer = self.menu.p1.text
        else: 
            winner = self.menu.p1.text
            otherPlayer = self.menu.p2.text
        print('winner-->',winner)
        self.scores.registerWin(winner, otherPlayer)
        # self.printScores()

    def setWinner(self):
        self.center = length//2+side*1.5, length+(menuHeight//2)
        self.textureRect = self.image.get_rect(center=self.center)
        self.turnImage()

    
    # Show Methods
    def printScores(self):
        entries = self.scores.getWins()
        lst = self.scores.getScores()

        print("\n\n\n***SCORES***")
        print('Name\tScore')
        for rec in lst:
            print(f"{rec[0]}\t{rec[1]}")
        
        print('\n\n***Entries***')
        print('Winner\tOther\tDate\t\tTime')
        for entry in entries:
            for i in entry.split():
                print(i.capitalize(), end='\t')
            print()
        print()

    def showSquares(self):
        for row in range(rows):
            for col in range(cols): 
                rect = (col*rectSize + 1 , row*rectSize + 1, sqSize, sqSize) # rect 
                pygame.draw.rect(self.screen, squareColor, rect) # drawing the rect

    def showMenuScreen(self):
        m_rect = (m_xcor, m_ycor, m_length, m_height)
        pygame.draw.rect(self.screen, m_screen_color, m_rect)


    def showMenu(self):        
        menuRect = (0, length, menuLength, menuHeight)
        pygame.draw.rect(self.screen, menuColor, menuRect)

    def showButtons(self):
        for button in self.buttons:
            button.blitButton(self.screen)

    def showPieces(self):
        for row in range(rows):
            for col in range(cols):
                sq = self.board.squares[row][col]
                if sq.piece != -1:
                    self.screen.blit(sq.img, sq.textureRect)
    
    def showText(self):
        self.text.show(self.screen)
        self.showImage()

    def showImage(self):
        self.screen.blit(self.image, self.textureRect)

    def showWinner(self):
        self.winner.show(self.screen)
        self.showImage()
    
    def showDraw(self):
        self.draw_text.show(self.screen)

