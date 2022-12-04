from src.const import *

class Square:

    def __init__(self, row, col):
        self.piece = -1 # (0-->O, 1-->X)
        self.row = row
        self.col = col
        self.texture = None
        self.textureRect = None
        self.img = None
