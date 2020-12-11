from functools import *
import re
from itertools import *

dirs = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]




if __name__ == "__main__":
    with open("input/day11.txt") as file:
        seats = [['.'] + list(s) + ['.'] for s in file]
        seats = [['.'] * len(seats[0])] + seats + [['.'] * len(seats[0])]
        w = len(seats[0])-2
        h = len(seats)-2

        def s(): return "".join("".join(s) for s in seats)

        prev = s()
        while True:
            seats2 = [l.copy() for l in seats]
            for i in range(1, w+1):
                for j in range(1, h+1):
                    occ = [a for row in seats[j-1:j+2] for a in row[i-1:i+2]].count('#')
                    me = seats[j][i]
                    if me == '#' and occ >= 5:
                        seats2[j][i] = 'L'
                    elif me == 'L' and occ == 0:
                        seats2[j][i] = '#'

            seats = seats2
            next = s()
            if next == prev:
                break
            prev = next

        print(list(prev).count('#'))


    with open("input/day11.txt") as file:
        seats = [['.'] + list(s.strip()) + ['.'] for s in file]
        seats = [['.'] * len(seats[0])] + seats + [['.'] * len(seats[0])]
        w = len(seats[0])-2
        h = len(seats)-2

        def s(): return "".join("".join(s) for s in seats)

        def sight(x, y, dx, dy):
            if x < 0 or y < 0 or x >= w+2 or y >= h+2:
                return 0

            return 1 if seats[y][x] == '#' else sight(x+dx, y+dy, dx, dy) if seats[y][x] == '.' else 0

        prev = s()
        while True:
            seats2 = [l.copy() for l in seats]
            for i in range(1, w+1):
                for j in range(1, h+1):
                    occ = 0
                    for dx, dy in dirs:
                        occ += sight(i+dx, j+dy, dx, dy)
                    me = seats[j][i]
                    if me == '#' and occ >= 5:
                        seats2[j][i] = 'L'
                    elif me == 'L' and occ == 0:
                        seats2[j][i] = '#'

            seats = seats2
            next = s()
            if next == prev:
                break
            prev = next

        print(list(prev).count('#'))
