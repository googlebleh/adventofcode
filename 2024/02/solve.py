#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    nsafe = 0
    for line in f:
        levels = list(map(int, line.split()))
        if (levels == sorted(levels)) or (list(reversed(levels)) == sorted(levels)):
            is_safe = 1
            for i in range(1, len(levels)):
                delta = abs(levels[i] - levels[i-1])
                if not(1 <= delta <= 3):
                    is_safe = 0
                    break
            nsafe += is_safe
    print(nsafe)
