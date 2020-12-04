import math

x0 = 0
y0 = 0

x1 = 3
y1 = 1

m = (y0-y1)-(x0-x1)

filename = 'input.txt'
linecount=sum(1 for line in open(filename,'r') if line.strip())
repeatcount=math.ceil(linecount/m)
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

while x < len(grid[0]) and y < linecount:
    spot = grid[y][x]
    if spot == '#':
        trees += 1
    print(x, y, spot)
    x = x + x1
    y = y + y1

print('trees = ', trees)
