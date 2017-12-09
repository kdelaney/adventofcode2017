input6 = '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'

banks = list(map(int, input6.split()))


def first(banks):
    states = []
    count = 0
    while banks not in states:
        states.append(banks[:])
        count += 1
        i = banks.index(max(banks))
        blocks = banks[i]
        banks[i] = 0
        for _ in range(blocks):
            i = (i + 1) % len(banks)
            banks[i] += 1

    return count


def second(banks):
    states = []
    count = 0
    while banks not in states:
        states.append(banks[:])
        count += 1
        i = banks.index(max(banks))
        blocks = banks[i]
        banks[i] = 0
        for _ in range(blocks):
            i = (i + 1) % len(banks)
            banks[i] += 1

    return count - states.index(banks)

print(second(banks))