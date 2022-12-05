import pygame

colors = dict(white = (255, 255, 255),
    englishViolet = (109, 70, 107),
    mistyRose = (234, 215, 215),
    wisteria = (180, 159, 204),
    darkPurple = (65, 34, 52),
    blanchedAlmond = (255, 236, 209),
    kobe = (120, 41, 15),
    ming = (21, 97, 109),
    richBlackFOGRA29 = (0, 21, 36))

class Text:

    def __init__(self, text, xcor=0, ycor=0, size=50, color=colors.get('white'), font="assets\\fonts\\Fontspring-DEMO-grotesco-bold.otf"):
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color)
        self.textRect = self.text.get_rect(center=(xcor, ycor))

    def show(self, surface):
        surface.blit(self.text, self.textRect)
    
