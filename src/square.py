from const import *

class Square:

    def __init__(self, row, col, texture=None, textureRect=None):
        self.piece = -1
        self.row = row
        self.col = col
        self.texture = texture
        self.textureRect = textureRect