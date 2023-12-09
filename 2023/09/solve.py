#!/usr/bin/env python3

import fileinput

def derivative(seq):
    return [seq[i] - seq[i-1] for i in range(1, len(seq))]

def get_next_value(seq):
    if all(e == 0 for e in seq):
        return 0

    return seq[0] - get_next_value(derivative(seq))

total = 0
for line in fileinput.input():
    curr = []

    seq = list(map(int, line.split()))
    total += (get_next_value(seq))

print(total)
