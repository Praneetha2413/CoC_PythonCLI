class king:
    def __init__(self, village):
        self.village=village
    def position(self, x, y):
        self.village[x][y]='K'
        return(self.village)
    def health(self, health, change):
        health=health-change
        return(health)