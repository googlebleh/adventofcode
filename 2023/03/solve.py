import re
import fileinput

board = ""
height = 0
for line in fileinput.input():
    row = line.strip()
    width = len(row)
    height += 1
    board += row

def board_i(row, col):
    return row * width + col

def rowcol(board_i):
    return board_i // width, board_i % width

def all_adjacent(i):
    row, col = rowcol(i)
    for drow in range(-1, 2):
        for dcol in range(-1, 2):
            adj_row = row + drow
            adj_col = col + dcol
            if (0 <= adj_row < height) and (0 <= adj_col < width):
                yield (adj_row, adj_col)

def is_partnum(m):
    i = m.start(0)
    row, col = rowcol(i)
    for i in range(m.start(), m.end()):
        for x, y in all_adjacent(i):
            if re.match(r"[^.\d]", board[board_i(x, y)]):
                return True

# for m in re.finditer(r"[^.\d]", board):
total = 0
for m in re.finditer(r"\d+", board):
    if is_partnum(m):
        total += int(m.group(0))
print(total)
