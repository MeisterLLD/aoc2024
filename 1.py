## P1

with open('1','r') as f:
    L1 = [ ]
    L2 = [ ]
    for ligne in f.read().splitlines():
        n1, n2 = map(int, ligne.split('   '))
        L1.append(n1)
        L2.append(n2)

L1.sort()
L2.sort()

print('Part 1 : ', sum( [abs(L1[i]-L2[i]) for i in range(len(L1))]   ))

## P2
sim = 0
for x in set(L1):
    sim += x*sum( [y==x for y in L2]   )
print('Part 2 : ', sim)