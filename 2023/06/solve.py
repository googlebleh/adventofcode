import fileinput

for line in fileinput.input():
    toks = line.split()

    label = toks[0]
    rest = int(''.join(toks[1:]))
    if label.startswith("Time"):
        times = rest
    elif label.startswith("Distance"):
        dists = rest

t = times
dists = [dists]
i = 0
for guess in range(t):
    if (t - guess) * guess > dists[i]:
        begin = guess
        break

for guess in range(t-1, -1, -1):
    if (t - guess) * guess > dists[i]:
        end = guess
        break


print(end-begin+1)
