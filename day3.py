import itertools

mysquare = 347991


def up(coords, steps):
    coords[1] += steps


def down(coords, steps):
    coords[1] -= steps


def left(coords, steps):
    coords[0] -= steps


def right(coords, steps):
    coords[0] += steps


def first(mysquare):
    coords = [0, 0]
    directions = [right, up, left, down]
    direction = 0
    steps = 1
    square = 1

    while square != mysquare:
        for _ in range(2):
            if (square + steps) < mysquare:
                square += steps
                directions[direction](coords, steps)
            else:
                directions[direction](coords, mysquare - square)
                square = mysquare
                break
            direction = (direction + 1) % len(directions)
        steps += 1
    return abs(coords[0]) + abs(coords[1])

print(first(mysquare))


def addneighbors(x, y, grid):
    xvalues = [x, x - 1, x + 1]
    yvalues = [y, y - 1, y + 1]
    return sum([grid[x][y] for (x,y) in itertools.product(xvalues, yvalues)])


def second(mysquare):
    directions = ['R', 'U', 'L', 'D']
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    x = y = 500
    grid[x][y] = 1
    direction = 0
    length = 1

    while True:
        for _ in range(2):
            for steps in range(length):
                grid[x][y] = addneighbors(x, y, grid)
                if grid[x][y] > mysquare:
                    return grid[x][y]
                if directions[direction] == 'U': y += 1
                elif directions[direction] == 'L': x -= 1
                elif directions[direction] == 'D': y -= 1
                else: x += 1
            direction = (direction + 1) % len(directions)
        length += 1

print(second(mysquare))