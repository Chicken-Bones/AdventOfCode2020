if __name__ == "__main__":
    with open("input/day10.txt") as file:
        nums = [int(s) for s in file]
        nums.sort()

        maxn = nums[-1] + 3
        full = [0] + nums + [maxn]
        diffs = [b - a for a, b in zip(full, full[1:])]
        print(diffs.count(1) * diffs.count(3))

        numpaths = [1] + [0] * maxn
        for i in full[1:]:
            numpaths[i] = sum(numpaths[max(0, i - 3):i])

        print(numpaths[maxn])
