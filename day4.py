import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def valid(s):
    return sum(f in fields for f, _ in re.findall(r"(\w+):(\S+)", s)) == len(fields)


def valid2(s):
    return sum(valid_value(f, v) for f, v in re.findall(r"(\w+):(\S+)", s)) == len(fields)


def valid_value(f, v):
    if f == 'byr':
        return 1920 <= int(v) <= 2002
    if f == 'iyr':
        return 2010 <= int(v) <= 2020
    if f == 'eyr':
        return 2020 <= int(v) <= 2030
    if f == 'hgt':
        if v[-2:] == 'cm':
            return 150 <= int(v[:-2]) <= 193
        if v[-2:] == 'in':
            return 59 <= int(v[:-2]) <= 76
    if f == 'hcl':
        return re.match(r"#[0-9a-f]{6}$", v) is not None
    if f == 'ecl':
        return v in 'amb blu brn gry grn hzl oth'.split(' ')
    if f == 'pid':
        return len(v) == 9 and v.isnumeric()

    return False


if __name__ == "__main__":
    with open("input/day4.txt") as file:
        passports = file.read().split('\n\n')
        print(sum(valid(p) for p in passports))
        print(sum(valid2(p) for p in passports))
