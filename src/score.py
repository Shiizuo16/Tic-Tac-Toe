from pickle import *
from src.dt import *
import os

class Scores:

    def __init__(self):
        if not os.path.isfile("scores.dat") or not os.path.isfile("wins.dat") :
            self.initializeFiles()

    def initializeFiles(self):
        with open('scores.dat', 'wb') as file:
            dump(list(), file)
        with open('wins.dat', 'wb') as file:
            dump(list(), file)

    def playerExist(self, name):
        with open('scores.dat', 'rb') as file:
            lst = load(file)
            for rec in lst:
                if str(rec[0]).lower() == name.lower():
                    return True
            else:
                return False

    def addPlayer(self, name):
        with open('scores.dat', 'rb') as file:
            lst = load(file)
            lst.append([name.strip().lower(), 0])
        with open('scores.dat', 'wb') as file:
            dump(lst, file)

    
    def registerWin(self, winner, other):
        # scores file
        with open('scores.dat', 'rb') as file:
            lst = load(file)
            
            for rec in lst:
                if rec[0] == winner.strip().lower():
                    rec[1] += 1
                    break
            else:
                print('winner not found')
        with open('scores.dat', 'wb') as file:
            dump(lst, file)
                
            
        # wins file
        with open('wins.dat', 'rb') as file:
            lst = load(file)

            d = currDate()
            t = currTime()
            string = f"{winner} {other} {d} {t}"
            lst.append(string)
        
        with open('wins.dat', 'wb') as file:
            dump(lst, file)

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

            




