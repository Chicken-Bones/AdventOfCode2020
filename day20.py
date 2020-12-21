import operator
from itertools import *
from math import *
from functools import *
from collections import *


def flip(img):
    return img[::-1]


def rotate(img):
    return [''.join(row[-y-1] for row in img) for y, _ in enumerate(img[0])]


def match(img, mask, x, y):
    if y + len(mask) > len(img) or x + len(mask[0]) > len(img[0]):
        return False

    return all(img_v == '#' for img_r, mask_r in zip(img[y:], mask) for img_v, mask_v in zip(img_r[x:], mask_r) if mask_v == '#')


class Tile:
    idx_n = 0
    idx_e = 1
    idx_s = 7
    idx_w = 4

    def __init__(self, src):
        lines = src.split("\n")
        self.id = int(lines[0][5:9])
        n = lines[1]
        s = lines[-1]
        w = "".join(l[0] for l in lines[1:])
        e = "".join(l[-1] for l in lines[1:])

        self.sides = [n, e, s[::-1], w[::-1], w, n[::-1], e[::-1], s]
        self.img = [l[1:-1] for l in lines[2:-1]]

    def rotate(self):
        self.sides = [self.sides[i] for i in [1, 2, 3, 0, 5, 6, 7, 4]]
        self.img = rotate(self.img)

    def flip(self):
        self.sides = self.sides[::-1]
        self.img = flip(self.img)

    def orient_to(self, side_value, dst_side_id):
        src_side_id = self.sides.index(side_value)
        if src_side_id & 4 != dst_side_id & 4:
            self.flip()

        while self.sides[dst_side_id] != side_value:
            self.rotate()


if __name__ == "__main__":
    with open("input/day20.txt") as file:
        tiles = [Tile(s) for s in file.read().strip().split("\n\n")]
        c = Counter(s for t in tiles for s in t.sides)

        def unique(side): return c[side] == 1

        corners = [t.id for t in tiles if sum(unique(s) for s in t.sides) == 4]
        print(reduce(operator.mul, corners, 1))

        t0 = next(t for t in tiles if t.id == corners[0])
        while not unique(t0.sides[Tile.idx_n]) or not unique(t0.sides[Tile.idx_w]):
            t0.rotate()

        gsize = int(sqrt(len(tiles)))
        grid = [[t0 for _ in range(gsize)] for _ in range(gsize)]
        tiles.remove(t0)

        for y in range(gsize):
            for x in range(gsize):
                if x == 0 and y == 0:
                    continue

                adj_tile, side1, side2 = (grid[y-1][x], Tile.idx_s, Tile.idx_n) if y > 0 else (grid[y][x-1], Tile.idx_e, Tile.idx_w)
                side = adj_tile.sides[side1]
                t = next(t for t in tiles if side in t.sides)
                tiles.remove(t)
                t.orient_to(side, side2)
                grid[y][x] = t

        img = [''.join(t.img[i] for t in tilerow) for tilerow in grid for i, _ in enumerate(t0.img)]
        transforms = deque([rotate, rotate, rotate, flip, rotate, rotate, rotate])

        oroborus = ['                  # ',
                    '#    ##    ##    ###',
                    ' #  #  #  #  #  #   ']

        imgsize = len(img)
        while not (sneks := sum(match(img, oroborus, x, y) for x in range(imgsize) for y in range(imgsize))):
            img = transforms.pop()(img)

        oroborus_thicc = sum(c == '#' for row in oroborus for c in row)
        img_rough = sum(c == '#' for row in img for c in row)
        print(img_rough - oroborus_thicc * sneks)