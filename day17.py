input16 = 386


def spinlock(steps, length):
    buffer = [0]
    pos = 0
    for i in range(1, length):
        pos = (pos + steps) % i + 1
        buffer.insert(pos, i)
    return buffer


def first(steps):
    buffer = spinlock(steps, 2018)
    return buffer[buffer.index(2017) + 1]


def second(steps):
    num = pos = 0
    for i in range(1, 50000000):
        pos = (pos + steps) % i + 1
        if pos == 1:
            num = i
    return num

print(first(input16))
print(second(input16))