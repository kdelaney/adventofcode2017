import re
import math
import numpy as np

with open('input20.txt', 'r') as f:
    buffer = f.readlines()


def distance(i):
    x, y, z = i
    return math.sqrt(abs(x)**2 + abs(y)**2 + abs(z)**2)


def parse():
    p = []
    v = []
    a = []

    for line in buffer:
        props = re.findall(r"[-+]?[0-9]+", line)
        p.append(props[:3])
        v.append(props[3:6])
        a.append(props[6:])

    p = np.array(p, dtype=np.int64)
    v = np.array(v, dtype=np.int64)
    a = np.array(a, dtype=np.int64)
    return p, v, a


def first():
    p, v, a = parse()

    for _ in range(1000):
        p = np.add(p, v)
        v = np.add(v, a)

    p = list(p.tolist())
    mn = min(p, key=distance)
    return p.index(mn)


def second():
    p, v, a = parse()

    for _ in range(100):
        v = np.add(v, a)
        p = np.add(p, v)
        index = [True]*len(p)
        for i in range(len(p)):
            for j in range(len(p)):
                if i != j and p[i][0] == p[j][0] and p[i][1] == p[j][1] and p[i][2] == p[j][2]:
                    index[i] = False
                    break
        v = v[index]
        p = p[index]
        a = a[index]

    return len(p)

print(first())
print(second())




