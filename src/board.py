from src.const import *
from src.square import Square

class Board:

    def __init__(self):
        self.squares = [[0 for i in range(cols)]for j in range(rows)]
        self.createBoard()

    def createBoard(self):
        for row in rows:
            for col in cols:
                self.squares[row][col] = Square(row,col)