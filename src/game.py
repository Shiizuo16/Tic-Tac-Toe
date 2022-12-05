import pygame

from src.const import *
from src.board import Board
from src.buttons import *
from src.mouse import Mouse
from src.line import Line
from src.menuText import *
from src.score import Scores
from src.menuScreen import Menu

class Game:

    def __init__(self, screen):
        self.draw = False
        self.won = False
        self.screen = screen
        self.buttons = buttons
        self.mouse = Mouse()
        self.board = Board()
        self.turn = 0 # (0-->O, 1-->X)
        self.line = Line()
        self.menu = Menu(screen)


        # player turn
        self.text = Text('Turn : ', length//2-side//2, length+(menuHeight//2))
        
        # Bottom Menu turn image
        self.image = pygame.image.load("assets\\buttons-48px\\dot.png")
        self.center = length//2+side, length+(menuHeight//2)
        self.textureRect = self.image.get_rect(center=self.center)

        # winner
        self.winner = Text('Winner : ', length//2-side*0.75, length+(menuHeight//2))
        
        # players
        self.players = dict()

        # scores
        self.scores = Scores()

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
                box.active = True
                box.color = box.color_active
                self.menu.active = True
                self.menu.activeBox = box
                break                        
            box.color = False
            
    def inactivateBox(self):
        box = self.menu.activeBox
        box.color = box.color_inactive
        box.active = False
        box.done = True
        self.menu.active = False
        self.menu.activeBox = None

    def writeText(self, char):
        box = self.menu.activeBox
        box.text += char
        l= box.font.size(box.renderText)[0]
        while l>box.length-side:
            box.renderText = box.renderText[1:]
            l = box.font.size(box.renderText)[0]

        box.renderText += char
        print()
        print('rtext-->',box.renderText,'  text-->', box.text)


    def delText(self):
        box = self.menu.activeBox

        text_l = box.font.size(box.text)[0]
        if text_l>box.length-side:
            index = box.text.index(box.renderText)
            box.renderText = box.text[index-1] + box.renderText[:-1]
        else:
            box.renderText = box.text
        box.text = box.text[:-1]
        print()
        print('rtext-->',box.renderText,'  text-->', box.text)



    
    # Show Methods
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

