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
from functools import cmp_to_key

graphord = { first[i] :  [second[j] for j in range(len(second)) if first[j] == first[i]]   for i in range(len(first))    }

def comp(a,b):
    if a in graphord and b in graphord[a]: return -1
    else: return 1

P2 = 0
for w in updates:
    if not(isvalid(w)):
        w.sort(key=cmp_to_key(comp))
        P2 += w[len(w)//2]

print('Part 2 :',P2)