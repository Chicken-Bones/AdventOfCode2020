from itertools import *

if __name__ == "__main__":
    with open("input/day9.txt") as file:
        nums = [int(s) for s in file]
        w = 25
        for i in range(w, len(nums)):
            if not any(a+b == nums[i] for a, b in combinations(nums[i-w:i], 2)):
                n = nums[i]
                break

        print(n)

        c = [0] + list(accumulate(nums))
        for i, j in combinations(range(len(nums)+1), 2):
            if c[j] - c[i] == n:
                print(min(nums[i:j]) + max(nums[i:j]))
                break

        # a faster way
        i, j, s = (0, 0, 0)
        while s != n:
            if s < n:
                s += nums[j]
                j += 1
            else:
                s -= nums[i]
                i += 1

        print(min(nums[i:j]) + max(nums[i:j]))