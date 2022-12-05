import pygame

from src.inputBox import InputBox
from src.menuText import *
from src.const import *
from src.button import Button

class Menu():

    def __init__(self, screen):
        self.screen = screen
        self.boxes = list()
        self.active = False
        self.activeBox = None
        self.texts = list()
        self.buttons = list()
        self.images = list()

        # Boxes
        self.p1 = InputBox(xcor=280, ycor=400)
        self.p2 = InputBox(xcor=280, ycor=500)
        self.boxes.extend([self.p1, self.p2])

        self.initializeMenu()

    def initializeMenu(self):
        menu = Text('TIC-TAC-TOE', xcor=length//2, ycor=115 ,size=100, font="assets\\fonts\\NERGON.ttf")
        p1 = Text('Player 1 : ', xcor=self.p1.xcor-130, ycor=self.p1.ycor+25)
        p2 = Text('Player 2 : ', xcor=self.p2.xcor-130, ycor=self.p2.ycor+25)
        scores_text = Text('SCORES', length*0.25-8, 275-10)
        reset_text = Text('RESET', length*0.75-8, 275-10)
        self.texts.extend([menu, p1, p2, scores_text, reset_text])

        scores = Button(100, 128, length*0.25, 275 , color=colors.get('white'))
        scores.setMenuButton("assets\\buttons-256px\\button.png")

        reset = Button(100, 128, length*0.75, 275 , color=colors.get('white'))
        reset.setMenuButton("assets\\buttons-256px\\button.png")
        self.buttons.extend([scores, reset])

        dot = pygame.image.load("assets\\buttons-48px\\dot.png")
        dotCenter = self.p2.xcor + 200 + 55, self.p2.ycor+26
        dotTextureRect = dot.get_rect(center=dotCenter)
        dot_tup = dot, dotTextureRect

        cross = pygame.image.load("assets\\buttons-48px\\cross.png")
        crossCenter = self.p1.xcor + 200 + 55, self.p1.ycor+26
        crossTextureRect = cross.get_rect(center=crossCenter)
        cross_tup = cross, crossTextureRect

        self.images.extend([dot_tup, cross_tup])

        


    def showMenuStuff(self):
        for text in self.texts:
            text.show(self.screen)
        for button in self.buttons:
            button.blitButton(self.screen)
        for image in self.images:
            self.screen.blit(image[0], image[1])

    def showBoxes(self):
        for box in self.boxes:
            box.surface = box.font.render(box.renderText, True, box.text_color)
            self.screen.blit(box.surface, (box.xcor+10, box.ycor+3))
            pygame.draw.rect(self.screen, box.color, box.rectangle, box.rectWidth)
