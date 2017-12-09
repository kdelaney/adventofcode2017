import itertools

with open('input4.txt', 'r') as f:
    passes = f.readlines()

no_repeats = lambda x: len(x) == len(set(x))

def first(passes):
    return sum(map(no_repeats, map(lambda x: x.split(), passes)))

def isvalid(password):
    permutations = []
    for word in password.split():
        permutations.extend(list(set([''.join(p) for p in itertools.permutations(word)])))
    return no_repeats(permutations)


def second(passes):
    return sum(map(isvalid, passes))


print(first(passes))
print(second(passes))
