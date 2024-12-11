L = list(map(int, open('11','r').read().split(' ')))
dico = { }

def howmanynewstones(steps, stone):
    if (steps, stone) in dico:
        return dico[(steps, stone)]

    if steps == 0:
        return 1

    if stone == 0:
        return howmanynewstones(steps-1, 1)

    c = str(stone)
    n = len(c)
    if n % 2 == 0:
        s1, s2 = int(c[:n//2]), int(c[n//2:])
        dico[(steps, stone)] = howmanynewstones(steps-1, s1) + howmanynewstones(steps-1, s2)
        return howmanynewstones(steps-1, s1) + howmanynewstones(steps-1, s2)

    return howmanynewstones(steps-1, 2024*stone)

print('Part 1 :', sum([howmanynewstones(25, x) for x in L]))
print('Part 2 :', sum([howmanynewstones(75, x) for x in L]))