P1 = 0
nummachines = (len(open('13','r').read().splitlines())+1)//4
with open('13','r') as f:
    for _ in range(nummachines):
        doable = False
        l1, l2 = f.readline().strip('\n').split(', ')
        a11, a21 = int(l1.split('+')[1]), int(l2.split('+')[1])
        l1, l2 = f.readline().strip('\n').split(', ')
        a12, a22 = int(l1.split('+')[1]), int(l2.split('+')[1])
        l1, l2 = f.readline().strip('\n').split(', ')
        b1, b2 = int(l1.split('=')[1]), int(l2.split('=')[1])
        f.readline()

        # L1 <- L1*a21, L2 <- L2*a11,
        a11, a12, b1, a21, a22, b2 = a11*a21, a12*a21, b1*a21, a21*a11, a22*a11, b2*a11
        # L2 <- L2 - L1
        a21 = a21 - a11
        a22 = a22 - a12
        b2 = b2 - b1
        if b2 % a22 == 0:
            numb = b2 // a22
        if numb and (b1 - a12*numb) % a11 == 0:
            numa = (b1 - a12*numb) // a11
            doable = True
        if doable and 0 <= numa <= 100 and 0 <= numb <= 100:
            P1 += 3*numa + numb

        numa, numb = 0, 0

print('Part 1 :', P1)
## P2
P2 = 0
nummachines = (len(open('13','r').read().splitlines())+1)//4
with open('13','r') as f:
    for _ in range(nummachines):
        doable = False
        l1, l2 = f.readline().strip('\n').split(', ')
        a11, a21 = int(l1.split('+')[1]), int(l2.split('+')[1])
        l1, l2 = f.readline().strip('\n').split(', ')
        a12, a22 = int(l1.split('+')[1]), int(l2.split('+')[1])
        l1, l2 = f.readline().strip('\n').split(', ')
        b1, b2 = 10000000000000+int(l1.split('=')[1]), 10000000000000+int(l2.split('=')[1])
        f.readline()

        # L1 <- L1*a21, L2 <- L2*a11,
        a11, a12, b1, a21, a22, b2 = a11*a21, a12*a21, b1*a21, a21*a11, a22*a11, b2*a11
        # L2 <- L2 - L1
        a21 = a21 - a11
        a22 = a22 - a12
        b2 = b2 - b1
        if b2 % a22 == 0:
            numb = b2 // a22
        if numb and (b1 - a12*numb) % a11 == 0:
            numa = (b1 - a12*numb) // a11
            doable = True
        if doable and 0 <= numa and 0 <= numb:
            P2 += 3*numa + numb

        numa, numb = 0, 0

print('Part 2 :', P2)
