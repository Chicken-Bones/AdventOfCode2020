import re
from functools import reduce


def move(t, dir):
    x, y = t
    if len(dir) > 1:
        x += y % 2
        x += 0 if "e" in dir else -1
        y += 1 if "n" in dir else -1
    else:
        x += 1 if "e" in dir else -1

    return x, y


if __name__ == "__main__":
    with open("input/day24.txt") as file:
        flipped = set()
        def flip(t):
            if t in flipped:
                flipped.remove(t)
            else:
                flipped.add(t)

        for l in file:
            flip(reduce(move, re.findall(r'([ns]?[ew])', l), (0, 0)))

        print(len(flipped))

        def adj(t):
            return (move(t, d) for d in ["e", "w", "ne", "se", "sw", "nw"])

        for _ in range(100):
            flip_white = set()
            flip_black = set()
            for b in flipped:
                neighbours = list(adj(b))
                if sum(t in flipped for t in neighbours) != 1:
                    flip_white.add(b)

                flip_black.update(n for n in neighbours if sum(t in flipped for t in adj(n)) == 2)

            flipped -= flip_white
            flipped |= flip_black

        print(len(flipped))
