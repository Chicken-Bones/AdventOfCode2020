import re

eye_colors = 'amb blu brn gry grn hzl oth'.split(' ')

validators = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': lambda v:
        150 <= int(v[:-2]) <= 193 if v[-2:] == 'cm' else
        59 <= int(v[:-2]) <= 76 if v[-2:] == 'in' else
        False,
    'hcl': lambda v: re.match(r"#[0-9a-f]{6}$", v),
    'ecl': lambda v: v in eye_colors,
    'pid': lambda v: len(v) == 9 and v.isnumeric()
}

if __name__ == "__main__":
    with open("input/day4.txt") as file:
        passports = [{k: v for k, v in re.findall(r"(\w+):(\S+)", s)} for s in file.read().split('\n\n')]
        print(sum(all(k in p for k in validators) for p in passports))
        print(sum(all(k in p and v(p[k]) for k, v in validators.items()) for p in passports))
