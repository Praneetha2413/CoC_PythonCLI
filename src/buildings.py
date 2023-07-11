healt=[]
class buildings(object):
    def __init__(self, health):
        healt.append(health)
    def decrement(self, i, j):
        if i+j==10:
            health=healt[0]-20
            healt[0]=health
        if i+j==16:
            health=healt[1]-20
            healt[1]=health
        if i+j==30:
            health=healt[2]-20
            healt[2]=health

        if i+j==27:
            health=healt[3]-20
            healt[3]=health
        if i+j==29:
            health=healt[4]-20
            healt[4]=health
        if i+j==0:
            health=healt[5]-20
            healt[5]=health
        return(health)
    def gethealth(self, i, j):
        if i+j==10:
            health=healt[0]
        if i+j==16:
            health=healt[1]
        if i+j==30:
            health=healt[2]
        if i+j==27:
            health=healt[3]
        if i+j==29:
            health=healt[4]
        if i+j==0:
            health=healt[5]
        return(health)

