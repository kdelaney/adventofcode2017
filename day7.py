import re
from itertools import chain

with open('input7.txt', 'r') as f:
    input7 = f.readlines()


def parse(discs):
    tower = {}
    weights = {}
    for disc in discs:
        bottom = disc.split()[0]
        weights[bottom] = int(disc.split()[1][1:-1])
        top = re.findall(r"[>|,] (\w+)", disc)

        if bottom in tower.keys():
            tower[bottom].extend(top)
        else:
            tower[bottom] = top
    return tower, weights


def first():
    tower, weights = parse(input7)
    for k in tower.keys():
        if k not in list(chain(*tower.values())):
            return k


def is_balanced(program, tower, weights):
    cum_weights = [get_weight(prog, tower, weights) for prog in tower[program]]
    if len(set(cum_weights)) > 1:
        return False
    return True


def get_weight(program, tower, weights):
    return weights[program] + sum([get_weight(prog, tower, weights) for prog in tower[program]])


def correct_weight(program, tower, weights):
    for prog in tower[program]:
        if not is_balanced(prog, tower, weights):
            return correct_weight(prog, tower, weights)
    cum_weights = [get_weight(prog, tower, weights) for prog in tower[program]]
    unique = list(set(cum_weights))
    if cum_weights.count(unique[0]) > 1:
        right_weight, wrong_weight = unique
    else:
        wrong_weight, right_weight = unique
    idx = cum_weights.index(wrong_weight)
    return weights[tower[program][idx]] + right_weight - wrong_weight


def second():
    tower, weights = parse(input7)
    for program in weights.keys():
        if not is_balanced(program, tower, weights):
            return correct_weight(program, tower, weights)


print(second())