import sys

with open(sys.argv[1]) as f:
    for line in f:
        ops = line.split()
        acc = 0
        while True:

def evalline(a):
    while len(a) > 1:
        a = [eval(a[0] + a[1] + a[2])] + a[3:]
    assert(len(a) == 1)
    return a[0]

def recurse(start, nleft):
    i = start
    while True:
        if line[i] == "(":
            start = i + 1
            end = recurse(start, nleft + 1)

def process(line):
    rs = []
    i = 0
    acc = 0
    start, end = 0, 0
    while True:
        if line[i] == "(":
            rs.append(acc)
            acc = 0
        elif line[i] == ")":
            acc = rs.pop()
        elif line[i].isdigit():

