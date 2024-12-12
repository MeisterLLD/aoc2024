carte = [ ]
with open('12','r') as f:
    for ligne in f.read().splitlines():
        carte.append(ligne)
n, m = len(carte), len(carte[0])

def voisinsgraphe(coord):
    i,j = coord
    pot = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)    ]
    return [ (x,y) for (x,y) in pot if x>=0 and y>=0 and x<n and y<m and carte[i][j] == carte[x][y]  ]

def voisinsphysiques(coord):
    i,j = coord
    return [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)    ]

P1, P2 = 0, 0
totalvus = set( )
for i in range(n):
    for j in range(m):
        if (i,j) not in totalvus:
            root = (i,j)
            area, perimeter, edges = 0, 0, 0
            vus = {root}
            totalvus.add(root)
            file = [root]
            while len(file) > 0:
                x = file.pop(0)
                for s in voisinsgraphe(x):
                    if s not in vus:
                        vus.add(s)
                        totalvus.add(s)
                        file.append(s)

            # On a la composante connexe
            for x in vus:
                area += 1
                perimeter += len(set(voisinsphysiques(x)) - set(voisinsgraphe(x)))

                edges     += len(set(voisinsphysiques(x)) - set(voisinsgraphe(x)))
                p, q = x
                if (p-1, q) in vus:
                    if  (p,q+1) not in vus and (p-1,q+1) not in vus:
                        edges -= 1
                    if  (p,q-1) not in vus and (p-1,q-1) not in vus:
                        edges -= 1
                if (p, q-1) in vus:
                    if (p-1, q-1) not in vus and  (p-1,q) not in vus:
                        edges -= 1
                    if (p+1, q-1) not in vus and (p+1, q) not in vus:
                        edges -= 1

            P1 += area*perimeter
            P2 += area*edges


print('Part 1 :', P1)
print('Part 2 :', P2)