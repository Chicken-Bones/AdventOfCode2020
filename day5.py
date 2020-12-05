def seatID(p):
    row = int(p[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(p[7:10].replace('R', '1').replace('L', '0'), 2)
    return row * 8 + col


if __name__ == "__main__":
    with open("input/day5.txt") as file:
        seats = [seatID(p) for p in file]
        print(max(seats))

        seats.sort()
        print(next(s1+1 for s1, s2 in zip(seats, seats[1:]) if s2 - s1 == 2))


