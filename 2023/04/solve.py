#!/usr/bin/env python3

import fileinput
import re

cum_score = 0

orig_cards = list(fileinput.input())
copied_cards = {}
num_copied = 0

for line in orig_cards:
    tokens = line.split()
    state = "winning"
    card_id = None
    winning_nums = []
    my_nums = []

    for i, e in enumerate(tokens):
        if e == "Card":
            card_id = int(tokens[i+1][:-1])
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
            score += 1

    for copy_i in range(score):
        if card_id not in copied_cards:
            copied_cards[card_id] = []

        num_to_cp = 1
        for key, value in copied_cards.items():
            targ = card_id + copy_i + 1
            # print(f"inner: {key}, {value}, {copy_i}")
            if card_id in value:
                x = value.count(card_id)
                # print("targ in value +=", x)
                num_to_cp += x

        # print(f"for card_id={card_id}, copy_i={copy_i}, num_to_cp={num_to_cp}")
        v = [card_id+copy_i+1] * num_to_cp
        copied_cards[card_id].extend(v)
        num_copied += num_to_cp

        # print(copied_cards)

    # print()

# print("end")
# print(copied_cards)

print(len(orig_cards) + (num_copied))






def main():
    pass

main()
