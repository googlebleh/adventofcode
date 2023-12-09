#!/usr/bin/env python3

import fileinput

def derivative(seq):
    r = []
    for i in range(1, len(seq)):
        r.append(seq[i] - seq[i-1])
    return r

def get_next_value(seq):
    if all(e == 0 for e in seq):
        return 0
    v = get_next_value(derivative(seq))
    return seq[0] - v

total = 0
for line in fileinput.input():
    curr = []

    seq = list(map(int, line.split()))
    total += (get_next_value(seq))

print(total)
    # while True:
    #     curr.append(seq)
    #     next_ = derivative(seq)
    #     if all(e == 0 for e in next_):
    #
    #     seq = next_
