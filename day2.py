import re


def valid(s):
    min, max, key, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", s).groups()
    return int(min) <= pwd.count(key) <= int(max)


def valid2(s):
    min, max, key, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", s).groups()
    return (pwd[int(min)-1] == key) ^ (pwd[int(max)-1] == key)


if __name__ == "__main__":
    with open("input/day2.txt") as file:
        print(sum(valid(s) for s in file))

    with open("input/day2.txt") as file:
        print(sum(valid2(s) for s in file))
