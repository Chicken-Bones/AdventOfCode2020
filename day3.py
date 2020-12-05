if __name__ == "__main__":
    with open("input/day3.txt") as file:
        field = [s.strip() for s in file]

        def ride(dx, dy):
            return sum(y % dy == 0 and row[y//dy * dx % len(row)] == '#' for y, row in enumerate(field))

        print(ride(3, 1))
        print(ride(1, 1) * ride(3, 1) * ride(5, 1) * ride(7, 1) * ride(1, 2))
