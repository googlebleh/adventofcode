#!/usr/bin/env python3

nums = []
with open("small") as f:
    nums = list(map(int, f))


def check(acc):
    print(list(nums[i] for i in acc))
    last = 0
    for i in acc:
        if not (nums[i] - last < 4):
            return False
        last = nums[i]
    return True

total = 0
def dfs(l, acc):
    if len(l) == len(acc):
        if check(acc):
            total += 1
            return True
        else:
            return False

    for i in range(len(l)):
        if ((not acc) and (l[i] < 4)):
            newacc = acc + [i]
            if not dfs(l, newacc):
                return False
        elif (acc) and ((i not in acc) and (l[i] - l[acc[-1]] < 4)):
            newacc = acc + [i]
            if not dfs(l, newacc):
                return False


dfs(nums, [])
print(total)
