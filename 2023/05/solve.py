#!/usr/bin/env python

import pprint
import copy
import fileinput
import re


def translate(seed, map_):
    # print(f"translate({seed}, {map_})")
    to, from_, len_ = map_

    # print(f"  from_={from_} seed={seed} len_={len_}")
    if not (from_ <= seed < from_+len_):
        return None
    # print("what?", from_ <= seed, seed <= (from_+len_))
    offset = seed - from_
    return to + offset


def mk_translate():


def main():
    seeds = []
    level = -1
    level_key = {}
    maps = {}
    for line in fileinput.input():
        line = line.strip()
        if line == "":
            continue
        tokens = line.split()

        if "seeds" in line:
            for i in range(1, len(tokens), 2):
                lo = int(tokens[i])
                n = int(tokens[i+1])
                seeds.append((lo, lo+n))
            # seeds.extend(list(map(int, tokens[1:])))
        elif "map:" in line:
            level += 1
            level_key[level] = tokens[0]
            maps[level] = []
        else:
            maps[level].append(list(map(int, tokens)))

    print("seeds:", seeds)

    curr = copy.copy(seeds)
    for l in range(level + 1):
        for seed_i in range(len(seeds)):
            s = curr[seed_i]
            if s is None:
                continue
            first = True
            for m in maps[l]:
                new = translate(s, m)
                # print("->", new)
                if new is not None:
                    if not first:
                        1/0
                    curr[seed_i] = new
                    first = False
            break
        print(curr)

    print(min(curr))


if __name__ == "__main__":
    main()
