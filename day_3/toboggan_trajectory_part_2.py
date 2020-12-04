import math

filename = 'input.txt'

def find_trees(x1, y1):
    x0 = 0
    y0 = 0

    m = abs((y0-y1)-(x0-x1))

    linecount=sum(1 for line in open(filename,'r') if line.strip())
    repeatcount=100
    grid=[]

    f = open(filename, 'r')
    i = 0
    for line in f.readlines():
        grid.append([])
        grid[i] = line.strip().split()
        i += 1

    clone = grid.copy()
    for j in range(repeatcount):
        for i in range(linecount):
            grid[i] = grid[i] + clone[i]

    i = 0
    for i in range(len(grid)):
        item = ''
        for x in grid[i]:
            item = item + x
        grid[i] = list(item)

    x = 0
    y = 0
    trees = 0

    print(len(grid[0]))
    while x < len(grid[0]) and y < linecount:
        spot = grid[y][x]
        if spot == '#':
            trees += 1
        x = x + x1
        y = y + y1

    print('trees = ', trees)
    return trees

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

multiplied_trees = 1
for slope in slopes:
    x1 = slope[0]
    y1 = slope[1]
    print(x1, y1)
    trees = find_trees(x1, y1)
    multiplied_trees *= trees

print('multiplied trees = ', multiplied_trees)
