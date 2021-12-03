import fileinput
for line in fileinput.input():
    line = line.strip()
    row = list(range(128))
    col = list(range(8))
    for c in line:
        if c == 'F':
            row = row[:len(row)//2]
        if c == 'B':
            row = row[len(row)//2:]
        if c == 'R':
            col = col[len(col)//2:]
        if c == 'L':
            col = col[:len(col)//2]

        # print(row, col)
    assert(len(row)==1)
    assert(len(col)==1)
    print(row[0]*8 + col[0])
