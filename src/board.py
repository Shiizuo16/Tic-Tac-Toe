from src.const import *
from src.square import Square
# from const import *
# from square import Square

class Board:

    def __init__(self):
        self.squares = [[(i,j) for j in range(cols)]for i in range(rows)]
        self.createBoard()

    def createBoard(self):
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row,col)

    def clear(self):
        self.createBoard()