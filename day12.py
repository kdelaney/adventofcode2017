import re

with open('input12.txt', 'r') as f:
    input12 = f.readlines()


def reachable(id, lines):
    reachable = {id}
    num_pipes = 1
    while True:
        for line in lines:
            ids = re.findall(r'\d+', line)
            for id in ids:
                if id in reachable:
                    reachable = reachable.union(ids)
                    break
        if num_pipes == len(reachable):
            break
        else:
            num_pipes = len(reachable)
    return reachable


def first(lines):
    return len(reachable('0', lines))


def second(lines):
    ids = set()
    count = 0
    for line in lines:
        ids = ids.union(re.findall(r'\d+', line))
    while len(ids) > 0:
        count += 1
        ids = ids.difference(reachable(min(ids), lines))
    return count

print(second(input12))