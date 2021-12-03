import fileinput

l = sorted(list(map(int, fileinput.input())))
for i, e in enumerate(l):
    if l[i-1] != e-1:
        print(e)
    if l[i+1] != e+1:
        print(e)
