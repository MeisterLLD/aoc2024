codes = open('21', 'r').read().splitlines()

def numpart(c):
    return int(c[:-1])

from itertools import pairwise, product

numpad = {c:(i//3, i%3) for i, c in enumerate("789456123 0A")}
dirpad = {c:(i//3, i%3) for i, c in enumerate(" ^A<v>")}

def paths(A, B, keypad):
    (y1, x1), (y2, x2) = keypad[A], keypad[B],
    (ygap, xgap) = keypad[' ']
    vertical = (y2-y1)*'v' + (y1-y2)*'^'
    horizontal = (x2-x1)*'>' + (x1-x2)*'<'
    if y1 == ygap and x2 == xgap: return {vertical+horizontal+'A'}
    if y2 == ygap and x1 == xgap: return {horizontal+vertical+'A'}
    else: return {horizontal+vertical+'A', vertical+horizontal+'A'}

def createseqs(c, keypad):
    ''' returns the list of ways to enter code c on keypad keypad '''
    return {"".join(x) for x in product(*[paths(*p,keypad) for p in pairwise('A'+c)])}

P1 = 0
for code in codes:
    seqs1 = createseqs(code, numpad)
    seqs2 = set()
    for seq1 in seqs1:
        for seq2 in createseqs(seq1, dirpad):
            seqs2.add(seq2)

    seqs3 = set()
    for seq2 in seqs2:
        for seq3 in createseqs(seq2, dirpad):
            seqs3.add(seq3)

    P1 += numpart(code)*min( [len(x) for x in seqs3]    )
print('Part 1 :', P1)

## P2
dico = {}
def minlen(seq, depth):

    if depth == 0: return len(seq)

    if (seq,depth) in dico:
        return dico[(seq, depth)]

    S = 0
    for morceau in seq[:-1].split('A'):
        S += min( minlen(seq, depth-1) for seq in  createseqs(morceau+'A', dirpad)   )

    dico[(seq, depth)] = S
    return S


P2 = 0
for code in codes:
    P2 += min( minlen(seq, 25) for seq in createseqs(code, numpad)         )*numpart(code)
print('Part 2 :', P2)