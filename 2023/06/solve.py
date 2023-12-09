import fileinput

for line in fileinput.input():
    toks = line.split()

    label = toks[0]
    rest = list(map(int, toks[1:]))
    if label.startswith("Time"):
        times = rest
    elif label.startswith("Distance"):
        dists = rest

total = 1
for i, t in enumerate(times):
    ways_to_win = 0
    for guess in range(t):
        if (t - guess) * guess > dists[i]:
            ways_to_win += 1
    total *= ways_to_win

print(total)
