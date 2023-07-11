import os
from src.cannon import cannon
from src.wall import wall
from src.hut import hut
from src.townhall import townhall
from src.troop import troop
from src.king import king
from input import *
from colorama import Fore, Back, Style
import time
gw = 31
gh = 14
file1 = open("replay/myfile.txt","r+")
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk), end=' ')
def prRed(skk): print("\033[91m{}\033[00m" .format(skk),  end=' ')
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk), end=' ')
def prBlack(skk): print("\033[98m{}\033[00m" .format(skk), end=' ')
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk), end=' ')
def clearConsole():
    command = 'clear'
    os.system(command)


class villagemap:
    def __init__(self):
        self.village = []

    def main(self):
        self.row = []
        for i in range(gw):
            self.row.append('G')
        self.village.append(self.row)
        self.row = []
        for i in range(1, gh-1):
            self.row.append('G')
            for i in range(1, gw-1):
                self.row.append(' ')
            self.row.append('G')
            self.village.append(self.row)
            self.row = []
        for i in range(gw):
            self.row.append('G')
        self.village[1][6]='S'
        self.village[12][15]='S'
        self.village[6][29]='S'
        for i in range(2, gw-2):
            self.village[2][i]='V'
        for i in range(2, gw-2):
            self.village[11][i]='V'
        for j in range(2, gh-2):
            self.village[j][2]='V'
        for j in range(2, gh-2):
            self.village[j][28]='V'


        self.village.append(self.row)

    def makehuts(self):
        self.village = hut(self.village)
        self.village = self.village.makehut(5, 5)
        self.village = hut(self.village)
        self.village = self.village.makehut(7, 9)
        self.village = hut(self.village)
        self.village = self.village.makehut(4, 26)
        self.village = hut(self.village)
        self.village = self.village.makehut(6, 21)
        self.village = hut(self.village)
        self.village = self.village.makehut(9, 20)

    def buildtownhall(self):
        self.village = townhall(self.village)
        self.village = self.village.maketownhall()
    def getvillage(self):
        return(self.village)

    def buildwalls(self):
        self.village = wall(self.village)
        self.village = self.village.buildwall()

    def makecannons(self):
        self.village = cannon(self.village)
        self.village = self.village.makecannon(10, 6)
        self.village = cannon(self.village)
        self.village = self.village.makecannon(7, 26)

    def startking(self, x, y, health, change):
        king.__init__(self, self.village)
        self.village = king.position(self, x, y)
        health=king.health(self, health, change)
        print("King's health = ",health)
    def attack(self, x, y):
        flag=0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if flag ==1:
                    break  
                if self.village[i][j] == 'V' or self.village[i][j] == 'W':
                    self.village[i][j] = ' '
                if self.village[i][j] == 'H' and hut(self.village).damagehealth(i,j)==0:
                    self.village[i][j] = ' '
                if self.village[i][j] == '0':
                    a= townhall(self.village).damagehealth()
                    flag =1
                    if townhall(self.village).gethuthealth()==0:
                        for i in range(int((gh/2)-2), int((gh/2)+2)):
                            for j in range(int((gw-3)/2), int((gw+3)/2)):
                                self.village[i][j] = ' '
                if flag ==1:
                    break                  


                
    def spawn(self, x, y, change):
        troop.__init__(self, self.village)
        self.village = troop.position(self, x, y)
        #self.village = troop.move(self)
    def replay(self, replayline):
        file1.writelines(replayline)
        file1.writelines("\n")        
        replays=file1.readlines()
        for replayline in replays:
            clearConsole()
            print("REPLAYING OLD GAME")
            time.sleep(1.5)

            village1 = villagemap()
            village1.main()
            village1.makehuts()
            village1.buildwalls()
            village1.makecannons()
            village1.buildtownhall()
            village1.startking(12, 29, 100, 0)
            x = 12
            y = 29
            for command in replayline:
                
                switcher = {
                    'a': 2,
                    'w': 1,
                    's': -1,
                    'd': -2,
                    '1': 3,
                    '2': 4,
                    '3':5,
                    ' ':-3,
                    "None": -5
                }
                func = switcher.get(command, 'Invalid')
                x1=x
                y1=y
                village1.getvillage()[x][y]=' '
                if func == 2:
                    y = y-1
                if func == 1:
                    x = x-1
                if func == -1:
                    x = x+1
                if func == -2:
                    y = y+1
                if func == 5:
                    x=12
                    y=15
                    village1.spawn(x,y, 0)
                if func == 3:
                    x=1
                    y=6
                    village1.spawn(x,y, 0)
                if func == 4:
                    x= 6
                    y= 29
                    village1.spawn(x,y, 0)
                if func == -5:
                    time.sleep(0.1)
                if func == -3:
                    village1.attack(x, y)
                if village1.getvillage()[x][y]==' ' or village1.getvillage()[x][y]=='S':
                    village1.startking(x, y, 100, 0)
                else:
                    village1.startking(x1,y1, 100, 0)
                    x=x1
                    y=y1
                village1.printvillage()
                time.sleep(0.1)

    def printvillage(self):
        for i in range(gh):
            for j in range(gw):
                if self.village[i][j] == 'H' and hut(self.village).gethuthealth(i,j) >=50:
                    prGreen(self.village[i][j])
                elif self.village[i][j] == 'H' and hut(self.village).gethuthealth(i,j) >20 and hut(self.village).gethuthealth(i,j) < 50:
                    prYellow(self.village[i][j])   
                elif self.village[i][j] == 'H' and hut(self.village).gethuthealth(i,j) <=20:
                    prRed(self.village[i][j]) 
                elif self.village[i][j] == '0' and townhall(self.village).gethuthealth() >=50:
                    prGreen(self.village[i][j])
                elif self.village[i][j] == '0' and townhall(self.village).gethuthealth() <=20:
                    prRed(self.village[i][j])
                elif self.village[i][j] == '0' and townhall(self.village).gethuthealth() >20 and  townhall(self.village).gethuthealth() <50:
                    prYellow(self.village[i][j])
                elif self.village[i][j] == 'W' or self.village[i][j] == 'V':
                    prPurple(self.village[i][j])
                elif self.village[i][j] == 'G':
                    prBlack(self.village[i][j])
                elif self.village[i][j] == 'K':
                    prBlack(self.village[i][j])
                else:
                    print(self.village[i][j], end=' ')
            print('\n')
    def checkvillage(self):
        f=0
        for i in range(gh):
            for j in range(gw):
                if self.village[i][j] == 'H' or self.village[i][j] == '0':
                    f=1
        return(f)



village1 = villagemap()
village1.main()
village1.makehuts()
village1.buildwalls()
village1.makecannons()
village1.buildtownhall()
village1.startking(12, 29, 100, 0)
village1.printvillage()
x = 12
y = 29
replayline=[]
while(1):
    
    command = input_to(Get(), 1)
    clearConsole()
    if command!= None:
        replayline.append(command)
    if command == '0':
        file1.writelines(replayline)
        file1.writelines("\n")    
        print("You have exited")
        break
    if village1.checkvillage()==0:
        file1.writelines(replayline)
        file1.writelines("\n")    
        print("You Won")
        break
    
    
    switcher = {
        'a': 2,
        'w': 1,
        's': -1,
        'd': -2,
        '1': 3,
        '2': 4,
        '3':5,
        ' ':-3,
        'r':-4
    }
    func = switcher.get(command, 'Invalid')
    x1=x
    y1=y
    village1.getvillage()[x][y]=' '
    if func == 2:
        y = y-1
    if func == 1:
        x = x-1
    if func == -1:
        x = x+1
    if func == -2:
        y = y+1
    if func == 5:
        x=12
        y=15
        village1.spawn(x,y, 0)
    if func == 3:
        x=1
        y=6
        village1.spawn(x,y, 0)
    if func == 4:
        x= 6
        y= 29
        village1.spawn(x,y, 0)
    if func == -4:
        village1.replay(replayline)

    if func == -3:
        village1.attack(x, y)
    if village1.getvillage()[x][y]==' ' or village1.getvillage()[x][y]=='S':
        village1.startking(x, y, 100, 0)
    else:
        village1.startking(x1,y1, 100, 0)
        x=x1
        y=y1
    village1.printvillage()
