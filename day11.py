dirs = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]


def simulate(seats, neighbour_func, occ_threshold):
    def occupied(x, y):
        return sum(seats[pt] == '#' for pt in neighbour_func(x, y) if pt in seats)

    def ca(v, occ):
        return \
            'L' if v == '#' and occ >= occ_threshold else \
            '#' if v == 'L' and occ == 0 else \
            v

    while True:
        new_seats = {pt: ca(v, occupied(*pt)) for pt, v in seats.items()}
        if seats == new_seats:
            break
        seats = new_seats

    return sum(v == '#' for v in seats.values())


if __name__ == "__main__":
    with open("input/day11.txt") as file:
        plane = {(x, y): c for y, line in enumerate(file) for x, c in enumerate(line.strip())}
        seats = {k: v for k, v in plane.items() if v == 'L'}

        def neighbours_1(x, y):
            return ((x + dx, y + dy) for dx, dy in dirs)
        print(simulate(seats, neighbours_1, 4))

        def neighbours_2(x, y):
            for dx, dy in dirs:
                pt = (x+dx, y+dy)
                while pt not in seats and pt in plane:
                    pt = (pt[0]+dx, pt[1]+dy)
                yield pt

        print(simulate(seats, neighbours_2, 5))
