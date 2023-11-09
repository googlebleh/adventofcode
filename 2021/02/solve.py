import fileinput

# x, y = 0, 0
# for line in fileinput.input():
#     cmd, val = line.split()
#     val = int(val)
#
#     if cmd == "forward":
#         x += val
#     elif cmd == "down":
#         y += val
#     elif cmd == "up":
#         y -= val
#     else:
#         print(f"{line:!r}")
#
# print(x, y)
# print(x * y)


x, y = 0, 0
aim = 0
for line in fileinput.input():
    cmd, val = line.split()
    val = int(val)

    if cmd == "forward":
        x += val
        y += aim * val
    elif cmd == "down":
        aim += val
    elif cmd == "up":
        aim -= val
    else:
        print(f"{line:!r}")


print(x, y)
print(x * y)
