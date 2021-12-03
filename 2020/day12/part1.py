#!/usr/bin/env python3

import collections
import re
import sys

dirs = collections.deque([
    (1, 0), # east
    (0, -1),
    (-1, 0),
    (0, 1),
])

(x, y) = (0, 0)

with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(r"(\w)(\d+)", line)
        op, amt = m.groups()
        magnitude = int(amt)
        quarters = int(amt) // 90

        if op == "R":
            dirs.rotate(-quarters)

        elif op == "L":
            dirs.rotate(quarters)

        elif op == "E":
            x += magnitude

        elif op == "N":
            y += magnitude

        elif op == "W":
            x += -magnitude

        elif op == "S":
            y += -magnitude

        elif op == "F":
            x += dirs[0][0] * magnitude
            y += dirs[0][1] * magnitude

        else:
            print(repr(line))
            break

print("part1:", abs(x) + abs(y))
