f = open('input.txt', 'r')

valid = 0
for line in f.readlines():
    parts = line.strip().split()
    ranges = parts[0].split('-')
    minN = int(ranges[0])
    maxN = int(ranges[1])
    letter = parts[1].split(':')[0]
    password = parts[2]
    count = password.count(letter)
    print(minN, maxN, letter, password, count)
    if maxN >= count >= minN:
        valid += 1
print('valid = ', valid)
