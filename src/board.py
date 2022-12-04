from src.const import *
from src.square import Square

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

    def calcDraw(self):
        flag = False
        f = False
        for row in self.squares:
            for sq in row:
                if sq.piece == -1:
                    f = True
                    break
            if f:
                break
        else:
            flag = True

        return flag
    
    def listPieces(self):
        lst = [[-1 for i in range(cols)] for j in range(rows)]

        for row in range(rows):
            for col in range(cols):
                lst[row][col] = str(self.squares[row][col].piece).zfill(2)
        
        return lst

    def calcWin(self):
        lst = self.listPieces()
        
        #diagonals
        if lst[0][0] == lst[1][1] == lst[2][2] and lst[1][1] != '-1':
            return True, lst[1][1]
        elif lst[2][0] == lst[1][1] == lst[0][2] and lst[1][1] != '-1':
            return True, lst[1][1]
        
        # row-wise
        for row in range(rows):
            if lst[row][0] == lst[row][1] == lst[row][2]and lst[row][1] != '-1':
                return True, lst[row][1]
        # col-wise
        for col in range(cols):
            if lst[0][col] == lst[1][col] == lst[2][col]and lst[1][col] != '-1':
                return True, lst[1][col]

        return False, -1


    # Show methods
    def showGrid(self):
        lst = self.listPieces()
        for row in lst:
            print(row)
