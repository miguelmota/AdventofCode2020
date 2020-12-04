import re

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
            if key == 'byr':
                if len(value) != 4:
                    continue
                if int(value) < 1920:
                    continue
                if int(value) > 2002:
                    continue
            if key == 'iyr':
                if len(value) != 4:
                    continue
                if int(value) < 2010:
                    continue
                if int(value) > 2020:
                    continue
            if key == 'eyr':
                if len(value) != 4:
                    continue
                if int(value) < 2020:
                    continue
                if int(value) > 2030:
                    continue
            if key == 'hgt':
                x = re.match('^([0-9]+)(cm|in)$', value)
                if x is None:
                    continue
                num = x.groups()[0]
                unit = x.groups()[1]
                if unit == 'cm':
                    if int(num) < 150 or int(num) > 193:
                        continue
                if unit == 'in':
                    if int(num) < 59 or int(num) > 76:
                        continue
            if key == 'hcl':
                x = re.match('^#[0-9a-f]{6}$', value)
                if x is None:
                    continue
            if key == 'ecl':
                colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
                if value not in colors:
                    continue
            if key == 'pid':
                x = re.match('^[0-9]{9}$', value)
                if x is None:
                    continue
            valid_prop_count += 1
    if valid_prop_count >= 7:
        valid += 1

print('valid = ', valid)
