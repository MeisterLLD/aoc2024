## P1
with open('4','r') as f:
    carte = [ ]
    for ligne in f.read().splitlines():
        carte.append(ligne)

ymax, xmax = len(carte[0]), len(carte)
dirs = [ (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)    ]

def valid(pos):
    return 0 <= pos[0] < ymax and 0 <= pos[1] < xmax

def next(pos, dir):
    return pos[0]+dir[0], pos[1]+dir[1]

def isthereaxmas(pos, dir):
    j, i = pos
    r = 0
    while r<4 and valid((j,i)) and carte[j][i] == 'XMAS'[r]:
        j, i = next((j,i), dir)
        r += 1
    return r == 4

P1 = 0
for x in range(xmax):
    for y in range(ymax):
        pos = y, x
        for dir in dirs:
            if isthereaxmas(pos, dir):
                P1 += 1
print('Part 1 :', P1)

## P2
def prec(pos, dir):
    return pos[0]-dir[0], pos[1]-dir[1]

def isthereamas(pos, dir):
    j,i = pos
    jprec, iprec = prec(pos, dir)
    jnext, inext = next(pos, dir)
    return  valid((jprec, iprec)) and valid((jnext, inext)) and carte[j][i] == 'A' and (  carte[jprec][iprec] == 'M' and carte[jnext][inext] == 'S'     or  carte[jprec][iprec] == 'S' and carte[jnext][inext] == 'M'  )


P2 = 0
for x in range(xmax):
    for y in range(ymax):
        pos = y, x
        if isthereamas(pos, (1,1)) and isthereamas(pos, (1,-1)):
                P2 += 1
print('Part 2 :', P2)
