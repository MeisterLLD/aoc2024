## P1
from itertools import product
from collections import defaultdict, deque

numbers = list(map(int, open('22','r').read().splitlines()))
def nextnum(n):
    m = ((n << 6) ^ n)  % 16777216
    l = ((m >> 5) ^ m) % 16777216
    k = ((l << 11) ^ l) % 16777216
    return k

P1 = 0

digits = defaultdict(list)
changes = { }

for num in numbers:
    n = num
    digits[num].append(n % 10)
    for _ in range(2000):
        n = nextnum(n)
        digits[num].append(n % 10)
    P1 += n

print('Part 1 :', P1)

## P2
for num in numbers:
    changes[num] = [ digits[num][i+1] - digits[num][i] for i in range(len(digits[num])-1)  ]

def shifting_window(iterable):
  window = deque(maxlen=4)
  for item in iterable:
    window.append(item)
    if len(window) == 4:
      yield tuple(window)

price = { }
for n in numbers:
    c = changes[n]
    for j,seq in enumerate(shifting_window(c)):
        if (n,seq) not in price:
            price[(n,seq)] = digits[n][j+4]

P2 = 0
for seq in product(range(-9,10), repeat=4):
    curprice = 0
    for n in numbers:
        curprice += price.get((n, seq), 0)

    P2 = max(curprice, P2)

print('Part 2 :', P2)