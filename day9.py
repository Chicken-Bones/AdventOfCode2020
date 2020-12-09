from itertools import *

if __name__ == "__main__":
    with open("input/day9.txt") as file:
        nums = [int(s) for s in file]
        w = 25
        for i in range(w, len(nums)):
            if not any(a+b == nums[i] for a, b in combinations(nums[i-w:i], 2)):
                key = nums[i]
                break

        print(key)

        n = 32321523
        c = [0] + list(accumulate(nums))
        for i, j in combinations(range(len(nums)+1), 2):
            if c[j] - c[i] == n:
                print(min(nums[i:j]) + max(nums[i:j]))
                break

