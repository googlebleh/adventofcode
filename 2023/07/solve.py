#!/usr/bin/env python3

import functools
import fileinput

def is_five(hand):
    card = hand[0]
    return all(e == card for e in hand[1:])

def is_four(hand):
    seen = {}
    for c in hand:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1

    return sorted(seen.values()) == [1, 4]

def is_full_house(hand):
    seen = {}
    for c in hand:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1
    return sorted(seen.values()) == [2, 3]

def is_three(hand):
    seen = {}
    for c in hand:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1
    return sorted(seen.values()) == [1, 1, 3]

def is_two_pair(hand):
    seen = {}
    for c in hand:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1
    return sorted(seen.values()) == [1, 2, 2]

def is_one_pair(hand):
    seen = {}
    for c in hand:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1
    return sorted(seen.values()) == [1, 1, 1, 2]

def is_high(hand):
    seen = {}
    for c in hand:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1
    return sorted(seen.values()) == [1, 1, 1, 1, 1]

fives = []
fours = []
full_houses = []
threes = []
twopairs = []
onepairs = []
highs = []

for line in fileinput.input():
    entry = line.split()
    hand, bid = entry

    if is_five(hand):
        fives.append(entry)
    elif is_four(hand):
        fours.append(entry)
    elif is_full_house(hand):
        full_houses.append(entry)
    elif is_three(hand):
        threes.append(entry)
    elif is_two_pair(hand):
        twopairs.append(entry)
    elif is_one_pair(hand):
        onepairs.append(entry)
    elif is_high(hand):
        highs.append(entry)
    else:
        print(entry)
        1/0


strength = [ "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2" ]

def compare(item1, item2):
    for i, c in enumerate(item1[0]):
        s1 = strength.index(c)
        s2 = strength.index(item2[0][i])
        if s1 < s2:
            return 1
        elif s1 > s2:
            return -1
    return 0

fives.sort(key=functools.cmp_to_key(compare))
fours.sort(key=functools.cmp_to_key(compare))
full_houses.sort(key=functools.cmp_to_key(compare))
threes.sort(key=functools.cmp_to_key(compare))
twopairs.sort(key=functools.cmp_to_key(compare))
onepairs.sort(key=functools.cmp_to_key(compare))
highs.sort(key=functools.cmp_to_key(compare))

all_ = highs + onepairs + twopairs + threes + full_houses + fours + fives
total = 0
for i, (hand, bid) in enumerate(all_):
    score = i + 1
    total += score * int(bid)
print(total)
