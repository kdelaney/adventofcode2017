from day18 import Program

with open('input23.txt', 'r') as f:
    cmds = f.read().splitlines()


class Coprocessor(Program):
    def __init__(self):
        super().__init__()
        self.last_reg = {}
        self.last_line = 0

    def sub(self, x, y):
        self.registers[x] = self.get(x) - self.to_int(y)
        self.line += 1

    def jnz(self, x, y):
        if self.to_int(x) != 0:
            self.line += self.to_int(y)
        else:
            self.line += 1


def first():
    prog = Coprocessor()
    count = 0
    while prog.line < len(cmds):
        cmd = cmds[prog.line]
        getattr(prog, cmd.split()[0])(*cmd.split(' ')[1:])
        if cmd.split()[0] == 'mul':
            count += 1
    print(count)

first()


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def second():

    lo = 93
    lo = lo * 100 + 100000
    hi = lo + 17000
    count = 0
    for num in range(lo, hi + 1, 17):
        if not prime(num):
            count += 1
    print(count)
second()