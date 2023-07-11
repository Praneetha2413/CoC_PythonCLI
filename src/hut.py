from src.buildings import buildings
class hut(buildings):
    def __init__(self, village):
        self.village = village
        buildings.__init__(self, 100)
    def makehut(self, i, j):
        self.village[i][j] = 'H'
        return(self.village)
    def damagehealth(self, i, j):
        return(buildings.decrement(self, i,j))
    def gethuthealth(self, i, j):
        return(buildings.gethealth(self, i,j))
            

    
