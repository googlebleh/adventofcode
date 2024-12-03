#!/usr/bin/env python3

import sys

def safe_pop(levels, i):
    return (levels[:i] + levels[i+1:])

def inc_or_dec(levels):
    return ((levels == sorted(levels)) or (list(reversed(levels)) == sorted(levels)))

def is_safe(levels, recurse=True):
    for i in range(1, len(levels)):
        delta = abs(levels[i] - levels[i-1])
        if not(1 <= delta <= 3):
            if recurse:
                for i in range(len(levels)):
                    if is_safe(safe_pop(levels, i), False):
                        return True
            return False

    if inc_or_dec(levels):
        return True
    elif recurse:
        for i in range(len(levels)):
            if is_safe(safe_pop(levels, i), False):
                return True
    return False

with open(sys.argv[1]) as f:
    nsafe = 0
    for line in f:
        levels = list(map(int, line.split()))
        if is_safe(levels):
            nsafe += 1
    print(nsafe)
