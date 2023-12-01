import fileinput
import string

digit_words = {
    "zero": 0,
    "one":      1,
    "two":      2,
    "three":    3,
    "four":     4,
    "five":     5,
    "six":      6,
    "seven":    7,
    "eight":    8,
    "nine":     9,
}

def startswith_digit(s):
    for dw in digit_words.keys():
        if s.startswith(dw):
            return digit_words[dw]
    return None

def is_digit(s, i):
    if s[i].isdigit():
        return int(s[i])

    rv = startswith_digit(s[i:])
    if rv is not None:
        return rv
    return None

a = []
for line in fileinput.input():
    for i in range(len(line)):
        rv = is_digit(line, i)
        if rv is not None:
            first = str(rv)
            break

    for i in reversed(range(len(line))):
        r = is_digit(line, i)
        if r is not None:
            last = str(r)
            break

    print(first, last)
    a.append(int(first+last))
print(sum(a))
