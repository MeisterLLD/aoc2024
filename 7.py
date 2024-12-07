## P1
tots = [ ]
nums = [ ]
with open('7','r') as f:
    for ligne in f.read().splitlines():
        tot, num = ligne.split(': ')
        tot = int(tot)
        num = list(map(int, num.split(' ')))
        tots.append(tot)
        nums.append(num)

n = len(tots)

def explore(L, start, S):
    if L == [ ]:
        S.add(start)
    else:
        if start == None:
            explore(L[1::], L[0], S)
        else:
            explore(L[1::], start * L[0],S)
            explore(L[1::], start + L[0],S)

P1 = 0
for i in range(n):
    S = set()
    explore(nums[i], None, S)
    if tots[i] in S:
        P1 += tots[i]
print('Part 1 :', P1)

## P2
def cat(n,m):
    return int(str(n)+str(m))

def explore2(L, start, S, obj):
    if start is not None and start > obj:
        return 
    if L == [ ]:
        S.add(start)
    else:
        if start == None:
            explore2(L[1::], L[0], S, obj)
        else:
            explore2(L[1::], start * L[0],S, obj)
            explore2(L[1::], start + L[0],S, obj)
            explore2(L[1::], cat(start, L[0]), S, obj)

P2 = 0
for i in range(n):
    S = set()
    explore2(nums[i], None, S, tots[i])
    if tots[i] in S:
        P2 += tots[i]
print('Part 2 :', P2)
