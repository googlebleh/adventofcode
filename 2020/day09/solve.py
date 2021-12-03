#!/usr/bin/env python3

cachesize = 25
lasts = []

def sumoftwo(a, sum_):
    for i, x in enumerate(a):
        if any((x+y == sum_) for j, y in enumerate(a) if j != i):
            return True
    return False

target = None
nums = []
with open("input") as f:
    for x in map(int, f):
        nums.append(x)
        if len(lasts) < cachesize:
            lasts.append(x)
        else:
            if not sumoftwo(lasts, x):
                print("part1", x)
                target = x

            lasts.append(x)
            lasts = lasts[-cachesize:]


for i, e in enumerate(nums):
    if not(i < 2):
        for length in range(2, i):
            a = nums[i-length:i+1]
            if sum(a) == target:
                print("part2", min(a) + max(a))
                1/0
