class Program:
    def __init__(self):
        self.line = 0
        self.registers = {}
        self.freq = 0

    def get(self, reg):
        return self.registers.get(reg, 0)

    def to_int(self, val):
        if val.lstrip('-').isnumeric():
            return int(val)
        else:
            return self.get(val)

    def snd(self, x):
        self.freq = self.to_int(x)
        self.line += 1

    def set(self, x, y):
        self.registers[x] = self.to_int(y)
        self.line += 1

    def add(self, x, y):
        self.registers[x] = self.get(x) + self.to_int(y)
        self.line += 1

    def mul(self, x, y):
        self.registers[x] = self.get(x) * self.to_int(y)
        self.line += 1

    def mod(self, x, y):
        self.registers[x] = self.get(x) % self.to_int(y)
        self.line += 1

    def rcv(self, x):
        if self.to_int(x) != 0:
            self.registers[x] = self.freq
        self.line += 1

    def jgz(self, x, y):
        if self.to_int(x) > 0:
            self.line += self.to_int(y)
        else:
            self.line += 1

with open('input18.txt', 'r') as f:
    cmds = f.read().splitlines()


def first():
    prog = Program()
    while prog.line < len(cmds):
        cmd = cmds[prog.line]
        getattr(prog, cmd.split()[0])(*cmd.split(' ')[1:])
        if cmd.split()[0] == 'rcv' and prog.freq != 0:
            print(prog.freq)
            break

# first()


class Duetter(Program):
    def __init__(self, num, partner):
        self.line = 0
        self.registers = {'p': num}
        self.queue = []
        self.partner = partner
        self.snd_cnt = 0
        self.deadlock = False

    def snd(self, x):
        self.snd_cnt += 1
        self.partner.queue.append(self.to_int(x))
        self.line += 1
        self.partner.deadlock = False

    def rcv(self, x):
        if len(self.queue) > 0:
            self.registers[x] = self.queue.pop(0)
            self.line += 1
        else:
            self.deadlock = True


def second():
    prog0 = Duetter(0, None)
    prog1 = Duetter(1, prog0)
    prog0.partner = prog1

    while not (prog0.deadlock and prog1.deadlock):
        cmd1 = cmds[prog1.line]
        getattr(prog1, cmd1.split()[0])(*cmd1.split(' ')[1:])
        cmd0 = cmds[prog0.line]
        getattr(prog0, cmd0.split()[0])(*cmd0.split(' ')[1:])
    return prog1.snd_cnt

# print(second())

