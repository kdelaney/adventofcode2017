import re, string

with open('input16.txt', 'r') as f:
    moves = f.read().split(',')


def spin(programs, X, _):
    X = int(X)
    programs = programs[-X:] + programs[:-X]
    return programs


def exchange(programs, A, B):
    A = int(A)
    B = int(B)
    programs[A], programs[B] = programs[B], programs[A]
    return programs


def partner(programs, A, B):
    a = programs.index(A)
    b = programs.index(B)
    programs[a] = B
    programs[b] = A
    return programs


def parse(move):
    return re.match(r'(.)([0-9]{1,2}|[a-z])/?([0-9]{1,2}|[a-z])?', move).groups()


def dance(programs, moves):
    steps = {'s': spin, 'x': exchange, 'p': partner}
    for move in moves:
        step, *args = parse(move)
        programs = steps[step](programs, *args)
    return programs


def first(moves):
    programs = list(string.ascii_lowercase[:16])
    return ''.join(dance(programs, moves))


def dances_til_back(moves):
    programs = list(string.ascii_lowercase[:16])
    start = programs[:]
    count = 0
    while True:
        count += 1
        programs = dance(programs, moves)
        if programs == start:
            break
    return count


def second(moves):
    programs = list(string.ascii_lowercase[:16])
    num = 10**9 % dances_til_back(moves)
    for _ in range(num):
        programs = dance(programs, moves)
    return ''.join(programs)


assert(''.join(spin(list('abcde'), 1, None)) == 'eabcd')
assert(''.join(exchange(list('eabcd'), 3, 4)) == 'eabdc')
assert(''.join(partner(list('eabdc'), 'e', 'b')) == 'baedc')

print(first(moves))
print(second(moves))