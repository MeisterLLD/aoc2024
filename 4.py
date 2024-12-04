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
    i, j = pos
    r = 0
    while r<4 and valid((i,j)) and carte[i][j] == 'XMAS'[r]:
        i, j = next((i,j), dir)
        r += 1
    return r == 4

P1 = 0
for x in range(xmax):
    for y in range(ymax):
        pos = x, y
        for dir in dirs:
            if isthereaxmas(pos, dir):
                P1 += 1
print('Part 1 :', P1)

## P2
def prec(pos, dir):
    return pos[0]-dir[0], pos[1]-dir[1]

def isthereamas(pos, dir):
    i,j = pos
    iprec, jprec = prec(pos, dir)
    inext, jnext = next(pos, dir)
    return  valid((iprec, jprec)) and valid((inext, jnext)) and carte[i][j] == 'A' and (  carte[iprec][jprec] == 'M' and carte[inext][jnext] == 'S'     or  carte[iprec][jprec] == 'S' and carte[inext][jnext] == 'M'  )


P2 = 0
for x in range(xmax):
    for y in range(ymax):
        pos = x, y
        if isthereamas(pos, (1,1)) and isthereamas(pos, (1,-1)):
                P2 += 1
print('Part 2 :', P2)