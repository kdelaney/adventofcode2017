with open('input22.txt', 'r') as f:
    grid = list(map(list, f.read().splitlines()))


class Virus:
    def __init__(self, grid):
        self.grid = [line[:] for line in grid]
        self.x = (len(grid) // 2)
        self.y = self.x
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.facing = self.directions[0]
        self.count = 0

    def cur(self):
        return self.grid[self.y][self.x]

    def turn(self, direction):
        if direction == 'r':
            self.facing = self.directions[(self.directions.index(self.facing) + 1) % len(self.directions)]
        else:
            self.facing = self.directions[(self.directions.index(self.facing) - 1) % len(self.directions)]

    def move(self):
        self.y, self.x = map(sum, zip([self.y, self.x], self.facing))
        if self.y >= len(self.grid) or self.x >= len(self.grid) or self.y < 0 or self.x < 0:
            self.expand()

    def expand(self):
        newlen = len(self.grid) + 10
        self.grid = [['.']*newlen for _ in range(5)] + list(map(lambda x: ['.']*5 + x + ['.']*5, self.grid)) + [['.']*newlen for _ in range(5)]
        self.y += 5
        self.x += 5

    def infect(self):
        self.grid[self.y][self.x] = '#'
        self.turn('l')
        self.count += 1

    def clean(self):
        self.grid[self.y][self.x] = '.'
        self.turn('r')

    def __str__(self):
        temp = [row[:] for row in self.grid]
        temp[self.y][self.x] = '*'
        return '\n'.join(map(''.join, temp))


class EvolvedVirus(Virus):
    def process(self):
        if self.cur() == '.':
            self.grid[self.y][self.x] = 'W'
            self.turn('l')
        elif self.cur() == 'W':
            self.grid[self.y][self.x] = '#'
            self.count += 1
        elif self.cur() == '#':
            self.grid[self.y][self.x] = 'F'
            self.turn('r')
        else:
            self.grid[self.y][self.x] = '.'
            self.turn('l')
            self.turn('l')
        self.move()


def first():
    g = Virus(grid)
    for _ in range(10000):
        if g.cur() == '.':
           g.infect()
        else:
           g.clean()
        g.move()
    print(g.count)

first()

def second():
    g = EvolvedVirus(grid)
    for _ in range(10000000):
        g.process()

    print(g.count)
second()