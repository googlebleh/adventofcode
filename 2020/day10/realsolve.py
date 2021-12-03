#!/usr/bin/env python3

import functools
import copy

with open("sample") as f:
    nums = tuple(sorted(map(int, f)))

target = max(nums) + 3

@functools.lru_cache(None)
def check(rm_is):
    removed = [e for i, e in enumerate(nums) if i not in set(rm_is)]

    if len(removed) < 2:
        return True
    elif not (removed[0] < 4):
        return False
    elif not (target - removed[-1] < 4):
        return False

    prev = removed[0]
    for e in removed[1:]:
        if not (e - prev < 4):
            return False
        prev = e

    return True

@functools.lru_cache(None)
def num_distinct(rm_is, visited):
    print("num_distinct({!r}, )".format(rm_is))
    acc = 1
    starti = max(visited) if visited else 0
    for i in range(starti, len(nums)):
        if i in visited:
            continue

        new_rms = rm_is + tuple([i])
        if check(new_rms):
            acc += num_distinct(new_rms, visited + tuple([i]))
    return acc

print(num_distinct(tuple([]), tuple([])))
