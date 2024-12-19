designs = [ ]
with open('19', 'r') as f:
    patterns = f.readline().strip('\n').split(', ')
    f.readline()
    for design in f.read().splitlines():
        designs.append(design)

dico2 = { }
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

H = [howmanyways(design, patterns) for design in designs]
doable = sum([h>0 for h in H])
total = sum(H)
print('Part 1 :', doable)
print('Part 2 :', total)
