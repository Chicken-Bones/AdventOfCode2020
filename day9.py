from itertools import *

if __name__ == "__main__":
    with open("input/day9.txt") as file:
        nums = [int(s) for s in file]
        for i in range(25, len(nums)):
            prevs = nums[i-25:i]
            if not any(k > j and a+b == nums[i] for j, a in enumerate(prevs) for k, b in enumerate(prevs)):
                print(nums[i])
                break

        n = 32321523
        c = list(accumulate(nums))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if c[j] - c[i] == n:
                    print(min(nums[i+1:j+1]) + max(nums[i+1:j+1]))
                    break

