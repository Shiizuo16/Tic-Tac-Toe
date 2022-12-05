import pygame

from src.inputBox import InputBox

class Menu():

    def __init__(self, screen):
        self.screen = screen
        self.boxes = list()
        self.active = False
        self.activeBox = None

        # Boxes
        self.p1 = InputBox()
        self.p2 = InputBox(ycor=200)
        self.boxes.extend([self.p1, self.p2])

    def showBoxes(self):
        for box in self.boxes:
            box.surface = box.font.render(box.renderText, True, box.text_color)
            self.screen.blit(box.surface, (box.xcor+5, box.ycor+3))
            pygame.draw.rect(self.screen, box.color, box.rectangle, box.rectWidth)
