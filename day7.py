import re
from functools import *


def parserule(s):
    bag, contents = re.match(r"(.+?) bags contain (.+?)\.", s).groups()
    return bag, [(int(n), b) for n, b in re.findall(r"(\d+) (.+?) bag", contents)]


if __name__ == "__main__":
    with open("input/day7.txt") as file:
        rules = dict(parserule(s) for s in file)

        @lru_cache(maxsize=0)
        def contains(p, bag):
            return any(b == bag or contains(b, bag) for _, b in rules[p])

        print(sum(contains(p, "shiny gold") for p in rules))

        @lru_cache(maxsize=0)
        def size(bag):
            return sum(n * size(b) for n, b in rules[bag]) + 1

        print(size("shiny gold") - 1)


