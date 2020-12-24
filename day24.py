if __name__ == "__main__":
    with open("input/day24.txt") as file:
        flipped = set()
        def move(x, y, dir):
            if dir == "e":
                x += 1
            elif dir == "w":
                x -= 1
            elif dir == "ne":
                if y % 2 == 0:
                    x += 1
                y += 1
            elif dir == "nw":
                if y % 2 != 0:
                    x -= 1
                y += 1
            elif dir == "se":
                if y % 2 == 0:
                    x += 1
                y -= 1
            elif dir == "sw":
                if y % 2 != 0:
                    x -= 1
                y -= 1

            return x, y

        def flip(x, y):
            if (x, y) in flipped:
                flipped.remove((x, y))
            else:
                flipped.add((x, y))

        for l in file:
            l = l.strip()
            x, y = (0, 0)
            while l != "":
                d = l[:2] if l[0] == "n" or l[0] == "s" else l[0]
                l = l[len(d):]
                x, y = move(x, y, d)

            flip(x, y)

        print(len(flipped))

        def adj(x, y):
            for dir in ["e", "w", "ne", "se", "sw", "nw"]:
                yield move(x, y, dir)

        for _ in range(100):
            flip_white = []
            flip_black = []
            for x, y in flipped:
                n = list(adj(x, y))
                if sum(t in flipped for t in n) != 1:
                    flip_white.append((x, y))

                for x2, y2 in n:
                    if sum(t in flipped for t in adj(x2, y2)) == 2:
                        flip_black.append((x2, y2))

            flipped.difference_update(flip_white)
            flipped.update(flip_black)

        print(len(flipped))