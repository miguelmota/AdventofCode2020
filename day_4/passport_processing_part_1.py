filename = "input.txt"

valid_props = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
}

f = open(filename, 'r')
passports=[]
passport=''
for line in f.readlines():
    line = line.strip()
    passport = passport + line + ' '
    if line == "":
        passports.append(passport.strip())
        passport = ''
passports.append(passport.strip())

valid = 0
for passport in passports:
    valid_prop_count = 0
    parts = passport.split(' ')
    for part in parts:
        kv = part.split(':')
        key = kv[0]
        value = kv[1]
        print(key, value)
        if key in valid_props:
            valid_prop_count += 1
    if valid_prop_count >= 7:
        valid += 1

print('valid = ', valid)
