import pygame

from src.const import *
from src.board import Board
from src.buttons import *
from src.mouse import Mouse


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.buttons = buttons
        self.mouse = Mouse()
        self.board = Board()
        self.turn = 0 # (0-->O, 1-->X)

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
            # pygame.draw.rect(self.screen, button.color, button.rect)
            button.blitButton(self.screen)

    def showPieces(self):
        for row in range(rows):
            for col in range(cols):
                sq = self.board.squares[row][col]
                if sq.piece != -1:
                    self.screen.blit(sq.img, sq.textureRect)




