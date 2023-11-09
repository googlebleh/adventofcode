#!/usr/bin/env python3


with open("input.txt") as f:
    lines = list(map(int, f))

a = []
for i, line in enumerate(lines):
    if i < 2:
        continue

    window = sum(lines[i-2:i+1])
    a.append(window)


incs = 0
last_depth = a[0]
for line in a[1:]:
    depth = int(line)
    if depth > last_depth:
        incs += 1
    last_depth = depth

print(incs)


