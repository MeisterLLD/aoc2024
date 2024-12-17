## P1
reg = {'pointer':0}
with open('17','r') as f:
    reg['A'] = int(f.readline().split(': ')[1].strip('\n'))
    reg['B'] = int(f.readline().split(': ')[1].strip('\n'))
    reg['C'] = int(f.readline().split(': ')[1].strip('\n'))
    f.readline()
    L = list(map(int, f.readline().split(': ')[1].strip('\n').split(',')))
oldreg = reg.copy()

def combo(literal, A, B, C):
    if literal in (0,1,2,3):
        return literal
    if literal == 4:
        return reg['A']
    if literal == 5:
        return reg['B']
    if literal == 6:
        return reg['C']
    if literal == 7:
        raise "7 is reserved and will not appear in valid programs."

printed = [ ]

def instruction(opcode, operand, A, B, C):
    match opcode:
        case 0: #adv
            reg['A'] = int(A/(2**combo(operand, A, B, C)))
            reg['pointer'] += 2
        case 1: #bxl
            reg['B'] = B^operand
            reg['pointer'] += 2
        case 2: #bst
            reg['B'] = combo(operand, A, B, C) % 8
            reg['pointer'] += 2
        case 3: #jnz
            if reg['A'] == 0:
                reg['pointer'] += 2
            else:
                reg['pointer'] = operand
        case 4: #bxc
            reg['B'] = B^C
            reg['pointer'] += 2
        case 5: #out
            printed.append( combo(operand, A, B, C) % 8)
            reg['pointer'] += 2
        case 6: # bdv
            reg['B'] = int(A/2**combo(operand, A, B, C))
            reg['pointer'] += 2
        case 7: # cdv
            reg['C'] = int(A/2**combo(operand, A, B, C))
            reg['pointer'] += 2


while reg['pointer'] <= len(L)-1:
    pointer = reg['pointer']
    instruction(L[pointer], L[pointer+1], reg['A'], reg['B'], reg['C'])

output = ','.join([str(x) for x in printed])
print('Part 1 :', output)

## P2
''' I have no idea why this works. At first it seems that the first octal digit
of A can give you last digit of the output, the second of A the second-to-last
of the output and so on... But weirdly at some point you need to increment A
more than just the current digit, so you modify A's *previous* digits you
computed. Nonetheless it works. I can't see the logic in here, it's purely
heuristic  '''
N = 1
A = 0
while N <= 16:
    while L[-N:] != printed[-N:]:
        A += 8**(16-N)
        oldprinted = printed.copy()
        printed = [ ]
        reg = oldreg.copy()
        reg['A'] =  A
        while reg['pointer'] <= len(L)-1:
            pointer = reg['pointer']
            instruction(L[pointer], L[pointer+1], reg['A'], reg['B'], reg['C'])
    N += 1
print('Part 2 :', A)