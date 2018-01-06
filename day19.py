with open('input19.txt', 'r') as f:
    inpt = f.readlines()
maxlen = len(max(inpt, key=len))
inpt = [line.ljust(maxlen) for line in inpt]

x = y = 0
direction = (1, 0)
letters = []
steps = 0

while inpt[y][x] != '|':
    x += 1

while True:
    if inpt[y][x] == '|' or inpt[y][x] == '-':
        pass
    elif inpt[y][x] == '+':
        if direction[0] != 0:
            if x+1 < len(inpt[0]) and inpt[y][x+1] == '-':
                direction = (0, 1)
            else:
                direction = (0, -1)
        else:
            if y+1 < len(inpt) and inpt[y+1][x] == '|':
                direction = (1, 0)
            else:
                direction = (-1, 0)
    elif inpt[y][x].isalpha():
        letters.append(inpt[y][x])
    else:
        break
    y, x = map(sum, zip([y, x], direction))
    steps += 1

print(''.join(letters))
print(steps)