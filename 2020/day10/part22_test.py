#!/usr/bin/env python3
import copy
import functools


with open("small") as f:
    nums = list(map(int, f))

nums.sort()

@functools.lru_cache(None)
def check(acc):
    last = 0
    for i in acc:
        if not (i - last < 4):
            print(0, acc)
            return False
        last = i
    print(1, acc)
    return True


def dfs(starti, path):
    if starti >= len(nums):
        return []

    combos = []
    # print(starti, len(nums))
    for i, e in enumerate(range(starti, len(nums))):
        r = dfs(starti+1, path)
        if r:
            combos.extend(r)

        newpath = copy.copy(path)
        newpath.append(e)
        if check(tuple(newpath)):
            r = dfs(starti+1, newpath)
            if r:
                combos.extend(r)

    return combos

print(len(dfs(0, [])))
