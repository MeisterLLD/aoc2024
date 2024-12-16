from collections import defaultdict
from math import inf
from heapq import heappop, heappush

carte = { }
with open('16','r') as f:
    for y, ligne in enumerate(f.read().splitlines()):
        for x, char in enumerate(ligne):
            carte[complex(x,y)] = char

ymax, xmax = max( [int(p.imag) for p in carte]   ), max( [int(p.real) for p in carte]   )

for y in range(ymax):
    for x in range(xmax):
        if carte[complex(x,y)] == 'S':
            start = complex(x,y)
            carte[complex(x,y)] = '.'
        if carte[complex(x,y)] == 'E':
            end = complex(x,y)
            carte[complex(x,y)] = '.'


def isvalid(pos):
    return 0 <= int(pos.real) < xmax and 0 <= int(pos.imag) < ymax and carte[pos] == '.'

def voisins(state):
    ''' returns a list of tuples (cost, neighbor)
    Graph nodes are tuples of complex numbers (pos, dir) '''
    pos, dir, = state
    vois = []
    for newdir in [dir, 1j*dir, -1j*dir]: # turns
        newpos = pos + newdir
        if isvalid(newpos):
            vois.append(((1 if newdir == dir else 1001)  , (newpos, newdir)) )
    return vois


# Modified dijkstra on a graph of states : (pos, dir) (except the ending one)
# Careful, 1j is *down* and -1j is *up*

def dijkstra2(debut, end):
    ''' debut is a graph node (pos, dir) but fin is just the ending *pos* '''
    q = [(0, 0, debut)]
    dists = {debut: 0}
    predecessors = defaultdict(set)
    counter = 0

    while len(q) > 0:
        dist, _, state = heappop(q)
        pos, dir = state

        if pos == end:
            return dir, dist, predecessors

        for (cost, v) in voisins(state):
            if dist + cost <= dists.get(v,inf):
                counter += 1
                dists[v] = dist + cost
                if dist + cost < dists.get(v,inf):
                    predecessors[v] = {state}
                else:
                    predecessors[v].add(state)
                heappush(q, (dist + cost, counter, v))

def getpreds(pos):
    if pos == debut:
        return set()
    else:
        peres = predecessors[pos]
        return peres.union(*[getpreds(p) for p in predecessors[pos]])

debut = (start, 1)
dir, dist, predecessors = dijkstra2(debut, end)
tiles = set([x[0] for x in getpreds((end, dir))]).union(set([end]))
print('Part 1 :', dist)
print('Part 2 :', len(tiles))