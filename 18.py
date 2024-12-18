taille = 71
nbbytes = 1024
carte = [['.' for _ in range(taille)] for _ in range(taille)]
start = (0, 0)
end = (taille-1, taille-1)

with open('18','r') as f:
    for _ in range(nbbytes):
        x, y = map(int, f.readline().strip('\n').split(',') )
        carte[y][x] = '#'

def voisins(pos):
    i,j = pos
    pot = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)    ]
    return [ (x,y) for (x,y) in pot if x>=0 and y>=0 and x<taille and y<taille and carte[x][y] == '.'  ]

def distlarg(root):
    vus = {root}
    dist = { }
    file = [root]
    dist[root] = 0

    while len(file)>0:
        cour = file.pop(0)
        for s in voisins(cour):
            if s not in vus:
                vus.add(s)
                file.append(s)
                dist[s] = dist[cour] + 1

    return dist

dist = distlarg(start)
print('Part 1 :', dist[end])

## P2
carte = [['.' for _ in range(taille)] for _ in range(taille)]
dist = distlarg(start)

with open('18','r') as f:
    while end in dist:
        x, y = map(int, f.readline().strip('\n').split(',') )
        carte[y][x] = '#'
        dist = distlarg(start)

print('Part 2 :',(x,y))

