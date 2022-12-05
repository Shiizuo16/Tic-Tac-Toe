import pygame as pg
from src.menuText import *

class InputBox:

    def __init__(self, length=200, height=50, xcor=0, ycor=0, rectWidth=5):
        self.rectWidth = rectWidth
        self.xcor = xcor
        self.ycor = ycor
        self.length = length
        self.height = height
        self.rectangle = pg.Rect(xcor, ycor, length, height)
        self.color_inactive = colors.get('richBlackFOGRA29')
        self.color_active = colors.get('white')
        self.color = self.color_inactive
        self.active = self.done = False
        self.text = ''
        self.renderText = self.text
        self.font = pg.font.Font("assets\\fonts\\Fontspring-DEMO-grotesco-bold.otf", height-20)
        self.text_color = colors.get('white')
        self.surface = None


    def getInput(self):
        pass


    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 10))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 1)
        # Blit the  cursor
        if time.time() % 1 > 0.5:

            # bounding rectangle of the text
            text_rect = self.txt_surface.get_rect(topleft = (self.rect.x + 5, self.rect.y + 10))

            # set cursor position
            self.cursor.midleft = text_rect.midright

            pygame.draw.rect(screen, self.color, self.cursor)