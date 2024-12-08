## P1
from collections import defaultdict

carte = [ ]
with open('8','r') as f:
    for ligne in f.read().splitlines():
        carte.append(ligne)

n, m = len(carte), len(carte[0])
antennes = defaultdict(list)
for i in range(n):
    for j in range(m):
        if  carte[i][j] not in '.#':
            antennes[carte[i][j]].append(complex(i,j))

def isvalid(point):
    return 0 <= point.real < n and 0 <= point.imag < m

antinodes = set()
for freq in antennes:
    for i in range(len(antennes[freq])):
        for j in range(i+1, len(antennes[freq])):
            a1, a2 = antennes[freq][i], antennes[freq][j]
            p1 = 2*a1-a2
            p2 = 2*a2-a1
            if isvalid(p1):
                antinodes.add(p1)
            if isvalid(p2):
                antinodes.add(p2)

print('Part 1 :',len(antinodes))

## P2
from math import gcd
points = set()
for freq in antennes:
    for i in range(len(antennes[freq])):
        for j in range(i+1, len(antennes[freq])):
            a1, a2 = antennes[freq][i], antennes[freq][j]
            dx, dy = int( (a2-a1).real ),  int( (a2-a1).imag )
            g = gcd(abs(dx), abs(dy))
            xstep, ystep = dx//g, dy//g

            # Go one direction
            pt = a1
            while isvalid(pt):
                points.add(pt)
                pt = pt + complex(xstep,ystep)

            # And the other
            pt = a1 - complex(xstep, ystep)
            while isvalid(pt):
                points.add(pt)
                pt = pt - complex(xstep,ystep)

print('Part 2 :',len(points))

