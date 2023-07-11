from src.buildings import buildings
gw = 31
gh = 14


class townhall(buildings):
    def __init__(self, village):
        self.village = village
        buildings.__init__(self, 100)

    def maketownhall(self):
        for i in range(int((gh/2)-2), int((gh/2)+2)):
            for j in range(int((gw-3)/2), int((gw+3)/2)):
                self.village[i][j] = '0'
        return(self.village)
    def damagehealth(self):
        return(buildings.decrement(self, 0, 0))
    def gethuthealth(self):
        return(buildings.gethealth(self, 0,0))
