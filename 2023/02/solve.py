import fileinput
import re

max_reds = 12
max_greens = 13
max_blues = 14

cum_sum = 0

def check_one(line):
    min_red = 0
    min_green = 0
    min_blue = 0

    for round_ in line.split(";"):
        n_red = 0
        n_green = 0
        n_blue = 0

        m = re.search(r"(\d+) red", round_)
        if m:
            n_red = int(m.group(1))
        m = re.search(r"(\d+) green", round_)
        if m:
            n_green = int(m.group(1))
        m = re.search(r"(\d+) blue", round_)
        if m:
            n_blue = int(m.group(1))

        # if not ((n_red <= max_reds) and (n_green <= max_greens) and (n_blue <= max_blues)):
        #     return False

        min_red = max(min_red, n_red)
        min_green = max(min_green, n_green)
        min_blue = max(min_blue, n_blue)

    return min_red * min_green * min_blue
    # return True

for line in fileinput.input():
    m = re.match(r"Game (\d+):.+", line)
    if not m:
        print(repr(line))
        1/0
    game_id = int(m.group(1))

    # if check_one(line):
    #     # print("yes", game_id)
    #     cum_sum += game_id
    # else:
    #     # print("no", game_id)
    #     pass

    power = check_one(line)
    cum_sum += power


print(cum_sum)
