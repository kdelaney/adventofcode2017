with open('input13.txt', 'r') as f:
    input13 = f.readlines()


def caught(pico, rng):
    return (pico % (2 * (rng-1))) == 0


def first(lines):
    severity = 0
    for line in lines:
        depth, rng = map(int, line.split(': '))
        if caught(depth, rng):
            severity += depth*rng
    return severity


def second(lines):
    lines = [tuple(map(int, line.split(': '))) for line in lines]
    delay = 0
    while True:
        if all(map(lambda x: not caught(x[0]+delay, x[1]), lines)):
            break
        delay += 1
    return delay



print(second(input13))