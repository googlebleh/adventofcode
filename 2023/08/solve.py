#!/usr/bin/env python3

import math
import re
import fileinput

moves = None
map_ = {}

for line in fileinput.input():
    m = re.match(r"([RL]+)$", line)
    if m:
        moves = m.group(0)
        print(moves)

    m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
    if m:
        n, left, right = m.groups()
        map_[n] = (left, right)

def get_starting_nodes():
    r = []
    for k, _ in map_.items():
        if k.endswith("A"):
            r.append(k)
    return r

curr = get_starting_nodes()

def doit(curr):
    i = 0
    while True:
        move = moves[i % len(moves)]
        if move == "R":
            next_ = map_[curr][1]
        elif move == "L":
            next_ = map_[curr][0]
        else:
            1/0

        curr = next_
        i += 1

        # print(f"i={i} curr={curr} move={move}")
        if curr.endswith("Z"):
            return i

all_counts = [doit(c) for c in curr]
print(math.lcm(*all_counts))
