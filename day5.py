with open('input5.txt', 'r') as f:
    instructions = list(map(int, f.readlines()))

def first(instructions):
    count = 0
    i = j = 0
    while i < len(instructions):
        i += instructions[i]
        instructions[j] += 1
        j = i
        count += 1
    return count

# print(first(instructions))


def second(instructions):
    count = 0
    i = j = 0
    while i < len(instructions):
        offset = instructions[i]
        i += instructions[i]
        if offset < 3:
            instructions[j] += 1
        else:
            instructions[j] -= 1
        j = i
        count += 1
    return count

print(second(instructions))