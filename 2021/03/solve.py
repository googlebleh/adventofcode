import fileinput

lines = [line.strip() for line in fileinput.input()]
nbits = len(lines[0])


def get_counts(lines):
    counts = [[0, 0] for _ in range(nbits)]

    for line in lines:
        for i, e in enumerate(line):
            x = int(e)
            counts[i][x] += 1

    return counts


def part1():
    counts = get_counts(lines)
    val = 0
    other = 0
    for nzeros, nones in counts:
        if nzeros > nones:
            val = (val << 1)
            other = (other << 1) | 1
        elif nones > nzeros:
            val = (val << 1) | 1
            other = (other << 1)
        else:
            breakpoint()
            val = (val << 1)
            other = (other << 1) | 1

    print(val * other)


def split_lines(ls, i):
    zs, juans = [], []
    for e in ls:
        if e[i] == "0":
            zs.append(e)
        elif e[i] == "1":
            juans.append(e)
        else:
            assert False, e
    return zs, juans


def get_oxygen():
    lines_ = lines
    for i in range(nbits):
        zeros, ones = split_lines(lines_, i)
        if not zeros:
            lines_ = ones
        elif not ones:
            lines_ = zeros
        elif len(zeros) > len(ones):
            lines_ = zeros
        else:
            lines_ = ones
    return lines_[0]


def get_co2():
    lines_ = lines
    for i in range(nbits):
        zeros, ones = split_lines(lines_, i)
        if not zeros:
            lines_ = ones
        elif not ones:
            lines_ = zeros
        elif len(ones) < len(zeros):
            lines_ = ones
        else:
            lines_ = zeros
    return lines_[0]


def part2():
    o2 = get_oxygen()
    co2 = get_co2()

    print(int(o2, base=2) * int(co2, base=2))


# part1()
part2()
