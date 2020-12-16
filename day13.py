dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

if __name__ == "__main__":
    with open("input/day13.txt") as file:
        start = int(file.readline())
        bus_table = [(int(s), i) for i, s in enumerate(file.readline().split(",")) if s != "x"]
        busses = [b for b, _ in bus_table]
        bus = min(busses, key=lambda b: b - (start % b))
        print(bus * (bus - (start % bus)))

        lcm = 1
        dept = 0
        for b, d in bus_table:
            i = next(i for i in range(b) if (dept+lcm*i) % b == (b-d) % b)
            dept += lcm*i
            lcm *= b

        print(dept)

