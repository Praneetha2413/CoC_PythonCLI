 
gw=31
gh=20
def printvillage(village):
    temp= str(village)
    s2 = temp.replace('], [','\n')
    s3 = s2.replace('[','')
    s4 = s3.replace(']','\n')
    s5= s4.replace(',','')
    s6= s5.replace('\'','')
    print(s6)
def hut(i, j, village):
    village[i][j]='H'
    village[i-1][j]='H'
    village[i-1][j+1]='H'
    village[i][j+1]='H'
    return village
def wall(village):
    for i in range(int((gw-5)/2),int((gw+5)/2)):
        village[6][i]='W'
    for i in range(int((gw-5)/2),int((gw+5)/2)):
        village[13][i]='W'
    for j in range(int((gh/2)-4), int((gh/2)+4)):
        village[j][13]='W'
    for j in range(int((gh/2)-4), int((gh/2)+4)):
        village[j][17]='W'
    return village
def cannon(i, j, village):
    village[i][j]='C'
    village[i][j+1]='C'
    village[i+1][j]='C'
    village[i+2][j]='C'
    village[i+2][j+1]='C'
    return village

village=[]
row=[]

for i in range(gw):
    row.append('P')
village.append(row)
row=[]
for i in range(1,gh-1):
    row.append('P')
    for i in range(1,gw-1):
        row.append(' ')
    row.append('P')
    village.append(row)
    row=[]
for i in range(gw):
    row.append('P')
village.append(row)
row=[]

for i in range(int((gh/2)-2), int((gh/2)+2)):
    for j in range(int((gw-3)/2),int((gw+3)/2)):
        village[i][j]='0'

village=hut(4,5,village)
village=hut(7,11,village)
village=hut(16,25,village)
village=hut(18,19,village)
village=hut(13,3,village)
village=hut(6,27,village)
village=wall(village)
village=cannon(3,21, village)
village=cannon(15,7, village)

printvillage(village)

