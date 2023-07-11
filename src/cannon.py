class cannon:
    def __init__(self, village):
        self.village = village

    def makecannon(self, i, j):
        self.village[i][j] = 'C'
        return self.village
