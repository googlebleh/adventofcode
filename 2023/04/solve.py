#!/usr/bin/env python3

import fileinput
import re

cum_score = 0

for line in fileinput.input():
    tokens = line.split()
    state = "winning"
    card_id = None
    winning_nums = []
    my_nums = []

    for i, e in enumerate(tokens):
        if e == "Card":
            card_id = int(tokens[i+1][:-1])
            print("set", card_id)
            continue

        if card_id is None:
            continue
        if e == f"{card_id}:":
            continue
        if state == "winning" and e != "|":
            winning_nums.append(e)
            continue
        if e == "|":
            state = "mine"
            continue
        if state == "mine":
            my_nums.append(e)
            continue

        print("unknown state", state)
        1/0

    score = 0
    for n in my_nums:
        if n in winning_nums:
            if score == 0:
                score = 1
            else:
                score *= 2

    print(winning_nums)
    print(my_nums)
    print(score)

    cum_score += score

    # print(line)

print(cum_score)






def main():
    pass

main()
