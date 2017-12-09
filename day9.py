with open('input9.txt', 'r') as f:
    input9 = list(f.read())


def remove_garbage(stream):
    count = 0
    stream.pop(0)
    while stream[0] != '>':
        if stream[0] == '!':
            stream.pop(0)
        else:
            count += 1
        stream.pop(0)
    stream.pop(0)
    return count


def process(stream):
    group = 0
    score = 0
    count = 0

    while len(stream):
        if stream[0] == '<':
            count += remove_garbage(stream)
        elif stream[0] == '{':
            stream.pop(0)
            group += 1
        elif stream[0] == '}':
            stream.pop(0)
            score += group
            group -= 1
        else:
            stream.pop(0)
    return score, count

print("Part 1: {0} Part 2: {1}".format(*process(input9)))


