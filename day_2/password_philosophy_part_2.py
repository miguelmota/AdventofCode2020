f = open('input.txt', 'r')

valid = 0
for line in f.readlines():
    parts = line.strip().split()
    ranges = parts[0].split('-')
    a = int(ranges[0]) - 1
    b = int(ranges[1]) - 1
    letter = parts[1].split(':')[0]
    password = parts[2]
    print(password, password[a], password[b], letter)
    if (password[a] == letter) is not (password[b] == letter):
        valid += 1
print('valid = ', valid)
