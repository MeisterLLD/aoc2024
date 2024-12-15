from copy import deepcopy
arrowtocomplex = {'<' : -1+0j, '^' : -1j, '>' : 1+0j, 'v' : 1j}
moves = [ ]

carte = [ ]
with open('15','r') as f:
    for ligne in f.read().splitlines():
        if ligne == '':
            continue
        elif ligne[0] == '#':
            carte.append([x for x in ligne])
        else:
            for x in ligne:
                moves.append(arrowtocomplex[x])

carteoriginale = deepcopy(carte)

def get(carte, cplx):
    return carte[int(cplx.imag)][int(cplx.real)]

def display(carte, start):
    i = 0
    for row in carte:
        if i == int(start.imag):
            print(''.join([x if j != int(start.real) else '@' for j,x in enumerate(row) ]  ) )
        else:
            print(''.join(row))
        i+=1
    print('\n')


n, m = len(carte), len(carte[0])
for i in range(n):
    for j in range(m):
        if carte[i][j] == '@':
            start = complex(j,i)
            carte[i][j] = '.'

for dir in moves:
    curseur = start
    crates = False
    while get(carte, curseur+dir) == 'O':
        curseur = curseur + dir
        crates = True
    if get(carte, curseur+dir ) == '#':
        continue
    elif get(carte, curseur+dir) == '.':
        start += dir
        carte[int(start.imag)][int(start.real)] = '.'
        if crates: carte[int((curseur+dir).imag)][int((curseur+dir).real)] = 'O'


P1 = 0
for i in range(n):
    for j in range(m):
        if carte[i][j] == 'O':
            P1 += 100*i + j

print('Part 1 :', P1)
## P2
carte2 = [ ]
for row in carteoriginale:
    row2 = [ ]
    for x in row:
        if x == '#': row2 += '##'
        if x == 'O': row2 += '[]'
        if x == '.': row2 += '..'
        if x == '@': row2 += '@.'
    carte2.append(row2)

n, m = len(carte2), len(carte2[0])
for i in range(n):
    for j in range(m):
        if carte2[i][j] == '@':
            start2 = complex(j,i)
            carte2[i][j] = '.'


def getblockofcrates(pos, dir):
    tile = get(carte2, pos + dir)
    if tile not in ('[', ']'):
        return set()

    elif dir in (1j, -1j) and tile == '[':
        return set([pos+dir, pos+dir+1]).union(getblockofcrates(pos+dir, dir)).union(getblockofcrates(pos+dir+1, dir))
    elif dir in (1j, -1j) and tile == ']':
        return set([pos+dir, pos+dir-1]).union(getblockofcrates(pos+dir, dir)).union(getblockofcrates(pos+dir-1, dir))
    elif dir in (-1, 1):
        return set([pos+dir]).union( getblockofcrates(pos+dir, dir) )


for dir in moves:
    block = getblockofcrates(start2, dir)

    if block == set() and get(carte2, start2+dir) == '.':
        start2 += dir

    elif block != set():
        if dir == 1: # right
            y = int(next(iter(block)).imag)
            xmin, xmax = min([int(p.real) for p in block]), max([int(p.real) for p in block])
            if get(carte2, complex(xmax+1,y)) == '.':
                carte2[y][xmax+1] = ']'
                for x in range(xmax, xmin, -1):
                    carte2[y][x] = carte2[y][x-1]
                carte2[y][xmin] = '.'
                start2 += dir

        if dir == -1: # left
            y = int(next(iter(block)).imag)
            xmin, xmax = min([int(p.real) for p in block]), max([int(p.real) for p in block])
            if get(carte2, complex(xmin-1,y)) == '.':
                carte2[y][xmin-1] = '['
                for x in range(xmin, xmax, 1):
                    carte2[y][x] = carte2[y][x+1]
                carte2[y][xmax] = '.'
                start2 += dir


        if dir == 1j: # down
            # Can we move it ?
            moveable = True
            xs = set([int(p.real) for p in block])
            for x in xs:
                ymax = max([int(p.imag) for p in block if int(p.real) == x])
                if carte2[ymax+1][x] != '.':
                    moveable = False
                    break
            # Move it
            if moveable:
                for x in xs:
                    ymin = min([int(p.imag) for p in block if int(p.real) == x])
                    ymax = max([int(p.imag) for p in block if int(p.real) == x])
                    for y in range(ymax+1, ymin, -1):
                        carte2[y][x] = carte2[y-1][x]
                    carte2[ymin][x] = '.'
                start2 += dir


        if dir == -1j: # up
            # Can we move it ?
            moveable = True
            xs = set([int(p.real) for p in block])
            for x in xs:
                ymin = min([int(p.imag) for p in block if int(p.real) == x])
                if carte2[ymin-1][x] != '.':
                    moveable = False
                    break
            # Move it
            if moveable:
                for x in xs:
                    ymin = min([int(p.imag) for p in block if int(p.real) == x])
                    ymax = max([int(p.imag) for p in block if int(p.real) == x])
                    for y in range(ymin-1, ymax):
                        carte2[y][x] = carte2[y+1][x]
                    carte2[ymax][x] = '.'
                start2 += dir

P2 = 0
for i in range(n):
    for j in range(m-1):
        if carte2[i][j] == '[' and carte2[i][j+1] == ']':
            P2 += 100*i + j

print('Part 2 :', P2)