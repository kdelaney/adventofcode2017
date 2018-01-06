class TuringMachine():
    def __init__(self, state, rules):
        self.tape = ['0']*10
        self.cur = 0
        self.state = state
        self.direction = {'right': 1, 'left': -1}
        self.rules = {}
        for i in range(0, len(rules), 10):
            self.rules[rules[i]] = self.parse_rule(rules[i + 1:i + 9])

    def parse_rule(self, lines):
        def rule():
            if self.tape[self.cur] == lines[0]:
                self.tape[self.cur] = lines[1]
                self.move(lines[2])
                self.state = lines[3]
            elif self.tape[self.cur] == lines[4]:
                self.tape[self.cur] = lines[5]
                self.move(lines[6])
                self.state = lines[7]
        return rule

    def move(self, direction):
        self.cur += self.direction[direction]
        if self.cur < 0:
            self.tape = ['0'] * 5 + self.tape
            self.cur += 5
        elif self.cur >= len(self.tape):

            self.tape = self.tape + ['0'] * 5

    def compute(self):
        self.rules[self.state]()


def parse():
    with open('input25.txt', 'r') as f:
        lines = f.read().splitlines()
    rules = [line.rstrip('.:').split(' ')[-1] for line in lines[3:]]
    state = lines[0].rstrip('.').split(' ')[-1]
    steps = int(lines[1].split(' ')[-2])
    tm = TuringMachine(state, rules)
    return tm, steps


def first():
    tm, steps = parse()

    for i in range(steps):
        tm.compute()

    on = sum(map(int, tm.tape))
    print(on)


first()

