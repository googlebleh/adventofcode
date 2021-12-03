#!/usr/bin/env python3

import copy

with open("input") as f:
    code = f.read().split("\n")

n = 0

for pc, line in enumerate(code):

    if "jmp" in line:
        newcode = copy.deepcopy(code)
        newcode[pc] = line.replace("jmp", "nop")
        with open("modded/input" + str(n), "w") as out_f:
            out_f.write("\n".join(newcode))
        n += 1

    if "nop" in line:
        newcode = copy.deepcopy(code)
        newcode[pc] = line.replace("nop", "jmp")
        with open("modded/input" + str(n), "w") as out_f:
            out_f.write("\n".join(newcode))
        n += 1
