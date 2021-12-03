#!/usr/bin/env python3

import copy
import pprint
import sys
import itertools

pp = pprint.PrettyPrinter(compact=True)

with open(sys.argv[1]) as f:
    grid = list(map(list, list(line.strip() for line in f)))


rows = len(grid)
cols = len(grid[0])

def in_range(c, r):
    return (0 <= c < cols) and (0 <= r < rows)

def checkadj(g, r, c):
    ntaken = 0
    # print("r={} c={} {}".format(r, c, g[r][c]))
    for xd in [-1, 0, 1]:
        for yd in [-1, 0, 1]:
            if xd == 0 and yd == 0:
                continue
            y = r + yd
            x = c + xd
            if in_range(x, y) and g[y][x] == "#":
                # print("check istaken ({} {})".format(y, x))
                ntaken += 1
    return ntaken

def checksight(g, r, c):
    ntaken = 0
    # print("r={} c={} {}".format(r, c, g[r][c]))

    for dr, dc in itertools.product([-1, 0, 1], repeat=2):
        if (dr, dc) == (0, 0):
            continue
        r_, c_ = r, c
        while True:
            r_ += dr
            c_ += dc
            if not in_range(c_, r_):
                break
            lookat = g[r_][c_]
            if lookat == "#":
                ntaken += 1
                break
            elif lookat == "L":
                break

    return ntaken

# print("\n".join(map(''.join, grid)))
# print(checksight(grid, 3, 3))
# 1/0

while True:
    newgrid = copy.deepcopy(grid)
    # print("\n".join(map(''.join, grid)))
    for r, row in enumerate(grid):
        for c, seat in enumerate(row):
            if seat == "L":
                if checksight(grid, r, c) == 0:
                    newgrid[r][c] = "#"
            elif seat == "#":
                if checksight(grid, r, c) >= 5:
                    newgrid[r][c] = "L"
            elif seat == ".":
                pass
            else:
                assert(0)
    if grid == newgrid:
        print("\n".join(map(''.join, grid)))
        print("part2:", str(grid).count("#"))
        break
    grid = newgrid
    # input('')
