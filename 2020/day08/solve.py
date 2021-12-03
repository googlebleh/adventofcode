#!/usr/bin/env python3

import re
import sys

if len(sys.argv) < 2:
    with open("input") as f:
        code = f.read().split("\n")
else:
    with open(sys.argv[1]) as f:
        code = f.read().split("\n")

acc = 0
pc = 0

donepc = set()

while True:
    if pc in donepc:
        print("part1:", acc)
        break
    else:
        donepc.add(pc)

    line = code[pc]
    if line == "":
        print("error")
        break
    inst, op = line.split()

    if inst == "nop":
        if eval(str(pc) + op) == len(code)-1:
            print("part2:", acc)
            break
    elif inst == "acc":
        acc = eval(str(acc) + op)
    elif inst == "jmp":
        if pc == len(code)-2:
            print("part2:", acc)
            break
        pc = eval(str(pc) + op)
        continue

    pc += 1
