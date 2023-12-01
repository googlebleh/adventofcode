import fileinput
import string

a = []
for line in fileinput.input():
    for c in line:
        if c.isdigit():
            first = c
            break
    for c in reversed(line):
        if c.isdigit():
            last = c
            break

    a.append(int(first+last))
print(sum(a))
