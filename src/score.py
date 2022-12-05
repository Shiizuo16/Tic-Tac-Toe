from pickle import *
from src.dt import *

class Scores:

    def __init__(self):
        pass

    def initializeFiles(self):
        with open('scores.dat', 'wb') as file:
            dump(list())
        with open('wins.dat', 'wb') as file:
            pass

    def playerExist(self, name):
        with open('scores.dat', 'rb') as file:
            lst = load(file)
            for rec in lst:
                if rec[0] == name.lower():
                    return True
            else:
                return False

    def addPlayer(self, name):
        with open('scores.dat', 'rb') as file:
            lst = load(file)
            lst.append([name, 0])
        with open('scores.dat', 'wb') as file:
            dump(lst)

    
    def registerWin(self, winner, other):
        # scores file
        with open('scores.dat', 'rb') as file:
            lst = load(file)
            f = False
            for rec in lst:
                if rec[0] == name.lower():
                    rec[1] += 1
                    f = True
                    break
            
        # wins file
        with open('wins.dat', 'rb') as file:
            lst = load(file)

            d = currDate()
            t = currTime()
            string = f"{winner} {other} {d} {t}"
            lst.append(string)
        
        with open('wins.dat', 'wb') as file:
            dump(lst)

    def getScores(self):
        with open('scores.dat', 'rb') as file:
            lst = load(file)
            for rec in lst:
                rec[0] = str(rec[0]).capitalize()
            
            a = len(lst)
            for i in range(a):
                for j in range(i,a):
                    if lst[i][1] < lst[j][1]:
                        lst[i],lst[j] = lst[j],lst[i]
            
            return lst

    def getWins(self):
        with open('wins.dat', 'rb') as file:
            lst = load(file)
            return lst

            




