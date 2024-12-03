#!/usr/bin/env python3

import sys

xs = []
ys = []

with open(sys.argv[1]) as f:
    for line in f:
        xstr, ystr = line.split()
        x = int(xstr)
        y = int(ystr)
        xs.append(x)
        ys.append(y)

# part1
total_dist = 0
for x, y in zip(sorted(xs), sorted(ys)):
    total_dist += abs(x - y)
print(total_dist)

# part2
counts = {}
for y in ys:
    if y in counts:
        counts[y] += 1
    else:
        counts[y] = 1
similarity_score = 0
for x in xs:
    if x in counts:
        similarity_score += x * counts[x]
print(similarity_score)
