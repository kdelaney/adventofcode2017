with open('input21.txt', 'r') as f:
    rules = [line.split(' => ') for line in f.read().splitlines()]

rules2 = [rule for rule in rules if rule[0].count('/') == 1]
rules3 = [rule for rule in rules if rule[0].count('/') == 2]


def split(square):
    return square.split('/')


def flip(square):
    return list(map(lambda s: ''.join(reversed(s)), square))


def rotate(square):
    return list(map(lambda x: ''.join(x), zip(*square[::-1])))


def permute(square):
    for _ in range(4):
        square = rotate(square)
        yield square
        yield flip(square)


def enhance(square, r):
    for rule in r:
        for permutation in permute(square):
            if permutation == split(rule[0]):
                return split(rule[1])


def partition(square, div):
    if div == 2:
        for i in range(0, len(square), 2):
            for j in range(0, len(square), 2):
                yield [square[i][j:j+2], square[i+1][j:j+2]]
    else:
        for i in range(0, len(square), 3):
            for j in range(0, len(square), 3):
                yield [square[i][j:j+3], square[i+1][j:j+3], square[i+2][j:j+3]]


def combine(sections):
    if len(sections) == 1:
        return sections[0]
    else:
        square = []
        div = int(len(sections)**(1/2))
        for i in range(div):
            for j in range(len(sections[0])):
                row = []
                for k in range(div):
                    row.append(sections[i*div + k][j])
                square.append(''.join(row))
        return square

square = """.#.
..#
###"""
square = square.split('\n')

for i in range(18):
    print(i)
    sections = []
    if len(square) % 2 == 0:
        div = 2
        rule = rules2
    else:
        div = 3
        rule = rules3
    for p in partition(square, div):
        sections.append(enhance(p, rule))

    square = combine(sections)
    if i == 4 or i == 17:
        print(sum([line.count('#') for line in square]))