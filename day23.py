from itertools import *


def play(cups, steps):
    num_cups = len(cups)

    next = [0] * (num_cups + 1)
    for c1, c2 in zip(cups, cups[1:] + cups[:1]):
        next[c1] = c2

    current = cups[0]
    for m in range(steps):
        pickup = []
        c = current
        for _ in range(3):
            pickup.append(c := next[c])

        next[current] = next[c]

        c = current - 1
        while c < 1 or c in pickup:
            c = num_cups if c < 1 else c - 1

        next[pickup[-1]] = next[c]
        next[c] = pickup[0]
        current = next[current]

    c = 1
    while True:
        yield (c := next[c])


if __name__ == "__main__":
    with open("input/day23.txt") as file:
        starting_cups = [int(c) for c in file.read().strip()]
        result = takewhile(lambda x: x != 1, play(starting_cups, 100))
        print(''.join(str(i) for i in result))

        cups = starting_cups + list(range(len(starting_cups)+1, 1000000+1))
        a, b = islice(play(cups, 10000000), 2)
        print(a * b)
