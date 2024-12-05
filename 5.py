## P1
first, second = [ ], [ ]
updates = [ ]

with open('5','r') as f:
    for ligne in f.read().splitlines():
        if '|' in ligne:
            f, s = map(int, ligne.split('|'))
            first.append(f)
            second.append(s)
        if ',' in ligne:
            updates.append( list(map(int,ligne.split(',')))   )

def isvalid(update):
    return all( (update.index(first[i]) < update.index(second[i])) for i in range(len(first)) if first[i] in update and second[i] in update)

P1 = 0
for update in updates:
    if isvalid(update):
        P1 += update[len(update)//2]
print('Part 1 :', P1)

## P2
wrong = [ ]
for update in updates:
    if not(isvalid(update)):
        wrong.append(update)

graphord = { first[i] :  [second[j] for j in range(len(second)) if first[j] == first[i]]   for i in range(len(first))    }

def tritopo(L, G):
    dejavu = set()
    tri = []

    def rec(s):
        if s not in dejavu:
            dejavu.add(s)
            for t in G[s]:
                if t in L:
                   rec(t)
            tri.append(s)

    for s in L:
        rec(s)

    return tri[::-1]

P2 = 0
for w in wrong:
    w = tritopo(w, graphord)
    P2 += w[len(w)//2]
print('Part 2 :',P2)
