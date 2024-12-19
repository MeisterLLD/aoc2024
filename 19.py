## P1
designs = [ ]
with open('19', 'r') as f:
    patterns = f.readline().strip('\n').split(', ')
    f.readline()
    for design in f.read().splitlines():
        designs.append(design)


dico = { }
def doable(design, patterns):
    if design in dico:
        return dico[design]

    if design == '':
        return True

    for pattern in patterns:
        T = len(pattern)
        if design[:T] == pattern:
            rest = design[T:]
            if doable(rest, patterns):
                dico[design] = True
                return True

    dico[design] = False
    return False

print('Part 1 :', sum([doable(design, patterns) for design in designs]))

## P2
from collections import defaultdict
dico2 = {}

def howmanyways(design, patterns):

    if design in dico2:
        return dico2[design]

    if design == '':
        return 1

    add = 0
    for pattern in patterns:
        T = len(pattern)
        if design[:T] == pattern:
            rest = design[T:]
            add += howmanyways(rest, patterns)

    dico2[design] = add
    return dico2[design]

print('Part 2 :', sum([howmanyways(design, patterns ) for design in designs]))



