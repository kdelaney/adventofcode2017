with open('input11.txt', 'r') as f:
    input11 = f.read().split(',')

directions = {
    'n': (0, 2),
    'ne': (1, 1),
    'se': (1, -1),
    's': (0, -2),
    'sw': (-1, -1),
    'nw': (-1, 1)
}


def move(step, x, y):
    change = directions[step]
    x += change[0]
    y += change[1]
    return x, y


def steps_away(x, y):
    count = 0
    x = abs(x)
    y = abs(y)

    while x != 0:
        count += 1
        if y < 0:
            x, y = move('nw', x, y)
        else:
            x, y = move('sw', x, y)

    while y > 0:
        count += 1
        x, y = move('s', x, y)
    while y < 0:
        count += 1
        x, y = move('n', x, y)
    return count


def first(path):
    x = y = 0
    for step in path:
        x, y = move(step, x, y)
    return steps_away(x, y)


def second(path):
    x = y = 0
    max_steps = 0
    for step in path:
        x, y = move(step, x, y)
        steps = steps_away(x, y)
        max_steps = max(steps, max_steps)
    return max_steps


print(second(input11))