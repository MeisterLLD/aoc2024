## P1 & P2
with open('3','r') as f:
    texte = f.read()
    N = len(texte)

    i = 0
    ind_deb = [ ]
    ind_fin = [ ]
    do =  [ ]
    dont = [ ]

    for i in range(N-4):
        if texte[i:i+4] == 'mul(':
            ind_deb.append(i+4)
        if texte[i:i+4] == 'do()':
            do.append(i+4)
        if i <= N-7 and texte[i:i+7] == "don't()":
            dont.append(i+7)

    for deb in ind_deb:
        i = deb
        while texte[i] != ')':
            i += 1
        ind_fin.append(i)

from math import inf
def shouldidoit(i, do, dont):
    maxdo = max( [x for x in do if x <= i], default= -inf   )
    maxdont = max( [x for x in dont if x <= i], default= -inf  )
    return maxdo >= maxdont



P1, P2 = 0, 0
for i in range(len(ind_deb)):
    check = texte[ind_deb[i]:ind_fin[i]]
    if ',' in check:
        L = check.split(',')
        if len(L) == 2:
            l1, l2 = L
            if l1.isnumeric() and l2.isnumeric():
                P1 += int(l1)*int(l2)
                if shouldidoit(ind_deb[i], do, dont):
                    P2 += int(l1)*int(l2)

print('Part 1 :', P1)
print('Part 2 :', P2)