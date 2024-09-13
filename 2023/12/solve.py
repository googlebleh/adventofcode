import fileinput
import re


def dfs(row, lens, depth=0):
    print("\t"*depth, "dfs(", row, lens, ")")
    # breakpoint()
    if not lens:
        if row.find("#") == -1:
            return 1
        else:
            return 0

    n = lens[0]
    if len(lens) > 1:
        m = re.match("[.?]*?([?#]{" + str(n) + "})[.?]", row)
    else:
        m = re.match("[.?]*?([?#]{" + str(n) + "})", row)
    if m is None:
        return 0

    new_row = row[m.end():]
    new_lens = lens[1:]
    r = dfs(new_row, new_lens, depth+1)
    # breakpoint()
    if "#" not in m.group(1):
        r += dfs(row[m.start()+1], lens, depth+1)
    print("\t"*depth, r)
    return r


total = 0
lines = list(fileinput.input())

for i, line in enumerate(lines):
    if i != 1:
        continue
    row, nums = line.split()

    lens = list(map(int, nums.split(",")))
    r = dfs(row, lens)
    # print(row, nums, r)
    total += r
    break

print(total)
