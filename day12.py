dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

if __name__ == "__main__":
    with open("input/day12.txt") as file:
        x = 0
        y = 0
        a = 0
        for l in file:
            d = l[0]
            n = int(l[1:])

            if d == "N":
                y += n
            elif d == "S":
                y -= n
            elif d == "E":
                x += n
            elif d == "W":
                x -= n
            elif d == "R":
                a += n//90
            elif d == "L":
                a -= n//90
            elif d == "F":
                dx, dy = dirs[a % 4]
                x += dx * n
                y += dy * n
        print(abs(x) + abs(y))

    with open("input/day12.txt") as file:
        wx = 10
        wy = 1
        x = 0
        y = 0
        for l in file:
            d = l[0]
            n = int(l[1:])

            if d == "N":
                wy += n
            elif d == "S":
                wy -= n
            elif d == "E":
                wx += n
            elif d == "W":
                wx -= n
            elif d == "R":
                for _ in range(n//90):
                    wx, wy = (wy, -wx)
            elif d == "L":
                for _ in range(n//90):
                    wx, wy = (-wy, wx)
            elif d == "F":
                x += wx * n
                y += wy * n

        print(abs(x) + abs(y))
