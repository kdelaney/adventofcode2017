import operator
from functools import reduce

input10 = '76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229'


def tie(string, lengths, rounds=1):
    size = len(string)
    skip = 0
    offset = 0
    for _ in range(rounds):
        for length in lengths:
            if length:
                string = string[(length-1)::-1] + string[length:]
            string = string[(length+skip)%size:] + string[:(length+skip)%size]
            offset += length + skip
            skip += 1
    start = size - (offset % size)
    string = string[start:] + string[:start]
    return string


def first(input):
    lengths = list(map(int, input.split(',')))
    size = 256
    string = list(range(size))
    knot = tie(string, lengths)
    return knot[0] * knot[1]


def second(input):
    lengths = list(map(ord, input))
    lengths.extend([17, 31, 73, 47, 23])
    size = 256
    string = list(range(size))
    sparse = tie(string, lengths, 64)
    dense = [reduce(operator.xor, sparse[i*16:i*16+16]) for i in range(16)]
    return ''.join(map(lambda x: hex(x)[2:].rjust(2, '0'), dense))


print(second(input10))

