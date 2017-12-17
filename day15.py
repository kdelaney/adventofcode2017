A = 634
B = 301
factorA = 16807
factorB = 48271
divisor = 2147483647
bitmask = sum(2**n for n in range(16))


def first(a, b):
    count = 0
    for _ in range(40000000):
        a = (a * factorA) % divisor
        b = (b * factorB) % divisor
        if (a & bitmask) == (b & bitmask):
            count += 1
    return count


def find_a(a):
    while True:
        a = (a * factorA) % divisor
        if not (a % 4):
            break
    return a


def find_b(b):
    while True:
        b = (b * factorB) % divisor
        if not (b % 8):
            break
    return b


def second(a, b):
    count = 0
    for _ in range(5000000):
        a = find_a(a)
        b = find_b(b)
        if (a & bitmask) == (b & bitmask):
            count += 1
    return count



print(second(A, B))