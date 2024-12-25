from itertools import product
keys = set()
locks = set()

lignes = open('25','r').read().splitlines()
for i in range(500):
    maison = lignes[8*i:8*i+7]
    if maison[0] == 5*'#': # c'est un lock
        block = maison[1:]
        lock = tuple( max([i+1 for i in range(6) if block[i][j] == '#'], default = 0) for j in range(5)  )
        locks.add(lock)

    elif maison[6] == 5*'#': # c'est une key
        block = maison[:-1][::-1]
        key = tuple( max([i+1 for i in range(6) if block[i][j] == '#'], default = 0) for j in range(5)  )
        keys.add(key)

P1 = 0
for key in keys:
    for lock in locks:
        if all( key[i] + lock[i] <= 5 for i in range(5)):
            P1 += 1

print('Part 1 :', P1)