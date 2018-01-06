with open('input24.txt', 'r') as f:
    components = [list(map(int, line.split('/'))) for line in f.read().splitlines()]


def possibilities(nextport, components):
    return [c for c in components if c.__contains__(nextport)]


def dfsearch(bridge, strength, nextport, components, key):
    p = possibilities(nextport, components)
    if len(p) == 0:
        return bridge, strength
    else:
        strongest = bridge
        max_strength = strength
        for component in p:
            b = bridge[:] + [component[:]]
            s = strength + sum(component)
            n = component[1 - component.index(nextport)]
            c = components[:]
            c.remove(component)
            br, st = dfsearch(b, s, n, c, key)
            if key(br, st, strongest, max_strength):
                strongest = br
                max_strength = st
        return strongest, max_strength


def best(key):
    starters = [c for c in components if c.__contains__(0)]
    strongest = []
    max_strength = 0
    for s in starters:
        c = components[:]
        c.remove(s)
        br, st = dfsearch([s], sum(s), s[1 - s.index(0)], c, key)
        if key(br, st, strongest, max_strength):
            strongest = br
            max_strength = st
    return max_strength


def first():
    def key(br, st, strongest, max_strength):
        return st > max_strength
    return best(key)


def second():
    def key(br, st, strongest, max_strength):
        return len(br) > len(strongest) or ((len(br) == len(strongest)) and st > max_strength)
    return best(key)

print(first())
print(second())
