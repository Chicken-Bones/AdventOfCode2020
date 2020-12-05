def seatID(p):
    row = int(p[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(p[7:10].replace('R', '1').replace('L', '0'), 2)
    return row * 8 + col


if __name__ == "__main__":
    with open("input/day5.txt") as file:
        seats = [seatID(p) for p in file]
        num_seats = max(seats)
        min_seat = min(seats)
        print(num_seats)

        has_seat = [False] * (num_seats+1)
        for s in seats:
            has_seat[s] = True

        print(has_seat[min_seat:].index(False) + min_seat)


