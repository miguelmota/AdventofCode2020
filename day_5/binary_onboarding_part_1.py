import math

def get_seat_id(seat):
    i = 1
    x = 0
    y = 127
    result = 0
    for p in seat:
        if i < 8:
            if p == 'F':
                y = math.floor(y - ((y-x)/2))
            if p == 'B':
                x = math.ceil(x + ((y-x)/2))
        if i == 7:
            if p == 'F':
                result = x
            if p == 'B':
                result = y
            #print('row = ', result)
            x = 0
            y = 7
        if i >= 8:
            if p == 'L':
                y = math.floor(y - ((y-x)/2))
            if p == 'R':
                x = math.ceil(x + ((y-x)/2))
            #print(p, x, y)
        if i == 10:
            if p == 'L':
                column = x
            if p == 'R':
                column = y
            #print('column = ', column)
            result = result * 8 + column
        i += 1
    return result

f = open('input.txt', 'r')

seat_ids = []
for line in f.readlines():
    seat = line.strip()
    seat_ids.append(get_seat_id(seat))

print(seat_ids)
print('max seat id =', max(seat_ids))
