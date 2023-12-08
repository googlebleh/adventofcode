#!/usr/bin/env python3

import re
import fileinput

moves = None
map_ = {}

for line in fileinput.input():
    # RL
    #
    # AAA = (BBB, CCC)
    # BBB = (DDD, EEE)
    # CCC = (ZZZ, GGG)
    # DDD = (DDD, DDD)
    # EEE = (EEE, EEE)
    # GGG = (GGG, GGG)
    # ZZZ = (ZZZ, ZZZ)

    m = re.match(r"([RL]+)$", line)
    if m:
        moves = m.group(0)
        print(moves)

    m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
    if m:
        n, left, right = m.groups()
        map_[n] = (left, right)

i = 0
curr = "AAA"
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

    print(f"i={i} curr={curr} move={move}")
    if curr == "ZZZ":
        print(i)
        break
