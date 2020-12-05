if __name__ == "__main__":
    with open("input/day1.txt") as file:
        arr = [int(s) for s in file]
        print(next(i * j for i in arr for j in arr if i + j == 2020))
        print(next(i * j * k for i in arr for j in arr for k in arr if i + j + k == 2020))
