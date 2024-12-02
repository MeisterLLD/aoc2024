## P1, P2
def check(a):
    return (all(a[i] <= a[i + 1] for i in range(len(a) - 1)) or (all(a[i] >= a[i + 1] for i in range(len(a) - 1))) ) and  all(1 <= abs(a[i] - a[i+1]) <= 3 for i in range(len(a)-1))

score1, score2 = 0, 0
with open('2','r') as f:
    for ligne in f.read().splitlines():
        a = list(map(int, ligne.split(' ')))
        if check(a) :
            score1 += 1
            score2 += 1
        else:
            for i in range(len(a)):
                b = a.copy()
                b.pop(i)
                if check(b):
                    score2 += 1
                    break

print('Part 1 :', score1)
print('Part 2 :', score2)
