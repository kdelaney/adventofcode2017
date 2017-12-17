from day10 import second as knot_hash

input14 = 'oundnydw'


def used(inpt, row):
    return str(bin(int(knot_hash(inpt+'-'+str(row)), 16))[2:].zfill(128))


def first(inpt):
    count = 0
    for row in range(128):
        count += used(inpt, row).count('1')
    return count

print(first(input14))


def regionalize(disk, i, j, region):
    for (x, y) in [(i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < 128 and 0 <= y < 128 and 1 <= disk[x][y] < region:
            disk[x][y] = region
            regionalize(disk, x, y, region)


def second(inpt):
    disk = [list(map(int, used(inpt, row))) for row in range(128)]
    region = 2
    for i in range(128):
        for j in range(128):
            if disk[i][j] == 1:
                regionalize(disk, i, j, region)
                region += 1
    return region - 2

print(second(input14))