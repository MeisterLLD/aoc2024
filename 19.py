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

total = sum([howmanyways(design, patterns) for design in designs])
doable = len(set([k for k in dico2 if dico2[k] > 0]).intersection(designs))
print('Part 1 :', doable)
print('Part 2 :', total)

