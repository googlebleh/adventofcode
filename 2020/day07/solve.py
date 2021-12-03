#!/usr/bin/env python3

import re

line_regex = re.compile(r"([\w ]+) bags contain (.+)", re.DOTALL)
color_regex = re.compile(r"(\d+) ([\w ]+) bags?.\s")

lu_outers = {}
lu_inners = {}

with open("input") as f:
    for line in f:
        line_m = line_regex.match(line)
        if line_m is None:
            continue

        out_color = line_m.group(1)
        in_colors = [m.group(2) for m in color_regex.finditer(line_m.group(2))]
        contents = [m.groups() for m in color_regex.finditer(line_m.group(2))]
        
        for color in in_colors:
            if color in lu_outers:
                lu_outers[color].append(out_color)
            else:
                lu_outers[color] = [out_color]

        if out_color in lu_inners:
            lu_inners[out_color].extend(contents)
        else:
            lu_inners[out_color] = contents

results = set()
frontier = set(lu_outers["shiny gold"])

while frontier:
    results |= frontier
    new_frontier = set()
    for color in frontier:
        if color in lu_outers:
            new_frontier |= {out for out in lu_outers[color]}
    new_frontier -= frontier
    frontier = new_frontier

print("Part 1:", len(results))


def dfs(node):
    if node not in lu_inners:
        return 0

    r = 0
    for n_str, color in lu_inners[node]:
        r += int(n_str) * (1 + dfs(color))
    return r

print("Part 2:", dfs("shiny gold"))
