from collections import deque

carte = { }
with open('20','r') as f:
    for y, ligne in enumerate(f.read().splitlines()):
        for x, char in enumerate(ligne):
            carte[(x,y)] = char

ymax, xmax = max( [p[1] for p in carte]   ), max( [p[0] for p in carte]   )

for y in range(ymax):
    for x in range(xmax):
        if carte[(x,y)] == 'S':
            start = (x,y)
            carte[(x,y)] = '.'
        if carte[(x,y)] == 'E':
            end = (x,y)
            carte[(x,y)] = '.'

def isvalid(pos):
    i, j = pos
    return 0 <= i < xmax and 0 <= j < ymax


def voisinsgraphe(pos):
    i,j = pos
    pot = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)    ]
    return [ (x,y) for (x,y) in pot if x>=0 and y>=0 and x<xmax and y<ymax and carte[(x,y)] == '.'  ]

def voisinsabsolus(pos):
    i,j = pos
    pot = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)    ]
    return [ (x,y) for (x,y) in pot if x>=0 and y>=0 and x<xmax and y<ymax]

def manhattan(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def distlarg(root):
    vus = {root}
    dist = { }
    file = deque([root])
    dist[root] = 0

    while len(file)>0:
        cour = file.popleft()
        for s in voisinsgraphe(cour):
            if s not in vus:
                vus.add(s)
                file.append(s)
                dist[s] = dist[cour] + 1

    return dist

dist_to_start = distlarg(start)
dist_to_end = distlarg(end)
initialdistance = dist_to_end[start]


def savings(cheat1, cheat2):
    d1 = dist_to_start[cheat1]
    d2 = dist_to_end[cheat2]
    newdistance = d1 + d2 + manhattan(cheat1, cheat2)
    return initialdistance - newdistance


def solution(lencheat):
    saves  = { }
    for i1 in range(xmax):
        for j1 in range(ymax):
            if (i1,j1) in dist_to_start:
                cheat1 = i1, j1

                # Travel up to 20 times without walls
                root = (i1,j1)
                vus = {root}
                dist = { }
                file = deque([root])
                dist[root] = 0
                cour = root

                while file and dist[cour] <= lencheat:
                    cour = file.popleft()
                    for s in voisinsabsolus(cour):
                        if s not in vus:
                            vus.add(s)
                            file.append(s)
                            dist[s] = dist[cour] + 1

                for v in dist:
                    if dist[v] <= lencheat and v in dist_to_end:
                        cheat2 = v
                        saves[(cheat1, cheat2)] = savings(cheat1, cheat2)

    return len( [k for k in saves if saves[k] >= 100 ] )

print('Part 1 :', solution(2))
print('Part 1 :', solution(20))