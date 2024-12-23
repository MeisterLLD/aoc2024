from collections import defaultdict
G = defaultdict(list)
with open('23','r') as f:
    for ligne in f.read().splitlines():
        a, b = ligne.split('-')
        G[a].append(b)
        G[b].append(a)


## P1
triangles = set()
for a in G:
    for b in G[a]:
        for c in G[b]:
            if a in G[c]:
                triangles.add(frozenset({a,b,c}))

P1 = 0
for triangle in triangles:
    for x in triangle:
        if x[0] == 't':
            P1 += 1
            break
print('Part 1 :', P1)

## P2
cliques = set()

for v in G:
    clique = set([v])
    for w in G:
        if all( z in G[w] for z in clique    ):
            clique.add(w)
    cliques.add(frozenset(clique))


cliquemax = max(cliques, key = len)
print('Part 2 :', ','.join(sorted(cliquemax)))