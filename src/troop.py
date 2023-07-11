from math import sqrt

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))


class troop:
    def __init__(self, village):
        self.village=village
    def position(self, x, y):
        self.village[x][y]='B'
        return(self.village)
    def health(self, healthb, change):
        healthb=healthb-change
        return(healthb)
    #def move(self):
        
