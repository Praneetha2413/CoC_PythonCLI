gw = 31
gh = 14


class wall:
    def __init__(self, village):
        self.village = village
    def buildwall(self):
        for i in range(int((gw-5)/2), int((gw+5)/2)):
            self.village[4][i] = 'W'
        for i in range(int((gw-5)/2), int((gw+5)/2)):
            self.village[9][i] = 'W'
        for j in range(int((gh/2)-3), int((gh/2)+3)):
            self.village[j][12] = 'W'
        for j in range(int((gh/2)-3), int((gh/2)+3)):
            self.village[j][18] = 'W'
        return(self.village)
    
