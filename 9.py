## P1
ligne = open('9','r').read().split('\n')[0]
#ligne = '2333133121414131402'

seq = [ ]
file = True
id = 0
for c in ligne:
    if not file:
        for _ in range(int(c)):
            seq.append('.')
    else:
        for _ in range(int(c)):
            seq.append(id)
        id += 1
    file = not file

M = len(seq)-seq.count('.')
s = 0
endind = len(seq)-1

i = 0
while i < M:
    if seq[i] != '.':
        s += i*seq[i]
    else:
        s += i*seq[endind]
        endind -= 1
        while seq[endind] == '.':
            endind -= 1
    i += 1

print('Part 1 :', s)

## P2
n = len(seq)
freeblocks = []
i = 0

# On fabrique la liste des [position, taille] des blocs libres
while i < n:
    while i < n and seq[i] != '.':
        i += 1
    long = 0
    j = i

    if i < n:
        while j < n and seq[j] == '.':
            long += 1
            j += 1
        freeblocks.append([i,long])
        i += long



end = len(seq)-1
for file in range(id-1,-1,-1):

    # Recherche du bloc à droite
    while seq[end] != file:
        end -= 1
    debblock = end
    while seq[debblock] == file:
        debblock -= 1
    tailleblock = end-debblock

    # Recherche d'une place libre
    for i,(pos, size) in enumerate(freeblocks):
        if size >= tailleblock and pos < debblock: # si on en trouve une
            seq[pos:pos+tailleblock] = tailleblock*[file]
            seq[end-tailleblock+1:end+1] = tailleblock*['.']

            if freeblocks[i][1] == tailleblock:
                freeblocks.pop(i)
            else:
                freeblocks[i][0] += tailleblock
                freeblocks[i][1] -= tailleblock

            break

    end -= tailleblock

print('Part 2 :', sum([i*seq[i] for i in range(len(seq)) if seq[i] != '.']))




