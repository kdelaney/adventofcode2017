import operator

operators = {'<': operator.lt, '>': operator.gt, '<=': operator.le, '>=': operator.ge, '==': operator.eq, '!=': operator.ne,
             'inc': operator.add, 'dec': operator.sub}

with open('input8.txt', 'r') as f:
    instructions = f.readlines()


def first(instructions):
    registers = {}
    for instruction in instructions:
        parts = instruction.split()
        if parts[0] not in registers.keys(): registers[parts[0]] = 0
        if parts[-3] not in registers.keys(): registers[parts[-3]] = 0

        if operators[parts[-2]](registers[parts[-3]], int(parts[-1])):
            registers[parts[0]] = operators[parts[1]](registers[parts[0]], int(parts[2]))

    return max(registers.values())

print(first(instructions))


def second(instructions):
    registers = {}
    highest_ever = 0
    for instruction in instructions:
        parts = instruction.split()
        if parts[0] not in registers.keys(): registers[parts[0]] = 0
        if parts[-3] not in registers.keys(): registers[parts[-3]] = 0

        if operators[parts[-2]](registers[parts[-3]], int(parts[-1])):
            registers[parts[0]] = operators[parts[1]](registers[parts[0]], int(parts[2]))
        highest_ever = max(highest_ever, max(registers.values()))
    return highest_ever

print(second(instructions))