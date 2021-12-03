#!/usr/bin/env python3

import functools

with open("sample") as f:
    nums = tuple(sorted(map(int, f)))

target = max(nums) + 3

@functools.lru_cache(None)
def check(a):
    if len(a) < 2:
        return True
    elif not (a[0] < 4):
        return False
    elif not (target - a[-1] < 4):
        return False

    prev = a[0]
    for e in a[1:]:
        if not (e - prev < 4):
            return False
        prev = e

    return True


@functools.lru_cache(None)
def num_distinct(a, starti):
    acc = 1
    for i in range(starti, len(a)):
        removed = tuple(e for j, e in enumerate(a) if j != i)
        if check(removed):
            acc += num_distinct(removed, i)
    return acc

print(num_distinct(nums, 0))
