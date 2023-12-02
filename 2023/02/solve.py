import fileinput
import re

max_reds = 12
max_greens = 13
max_blues = 14

cum_sum = 0

def check_one(line):
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

        # if round_.startswith("Game 4"):
        #     print(n_red, n_green, n_blue)

        if not ((n_red <= max_reds) and (n_green <= max_greens) and (n_blue <= max_blues)):
            return False

    return True

for line in fileinput.input():
    m = re.match(r"Game (\d+):.+", line)
    if not m:
        print(repr(line))
        1/0
    game_id = int(m.group(1))

    if check_one(line):
        print("yes", game_id)
        cum_sum += game_id
    else:
        print("no", game_id)


print(cum_sum)
