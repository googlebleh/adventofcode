#!/usr/bin/env python3

cachesize = 5
lasts = []

def sumoftwo(a, sum_):
    for i, x in enumerate(a):
        if any((x+y == sum_) for j, y in enumerate(a) if j != i):
            return True
    return False

with open("sample") as f:
    for x in map(int, f):
        if len(lasts) < cachesize:
            lasts.append(x)
        else:
            if not sumoftwo(lasts, x):
                print("part1", x)

            lasts.append(x)
            lasts = lasts[-cachesize:]
