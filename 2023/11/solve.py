import copy
import fileinput
import pprint
import re
import functools

board = ""
height = 0
boardl = []
for line in fileinput.input():
    row = line.strip()
    width = len(row)
    height += 1
    board += row
    boardl.append(list(row))

def board_i(row, col):
    if (0 <= row < height) and (0 <= col < width):
        return row * width + col
    return None

def rowcol(bi):
    return bi // width, bi % width

def all_adjacent(rc):
    row, col = rc
    for drow in range(-1, 2):
        for dcol in range(-1, 2):
            if drow == 0 and dcol == 0:
                continue

            adj_row = row + drow
            adj_col = col + dcol
            if (0 <= adj_row < height) and (0 <= adj_col < width):
                yield (adj_row, adj_col)

gap_size = 1000000 - 1
@functools.cache
def empty_rows(src_i, dst_i):
    # a, b = edge
    # ar, ac = rowcol(a)
    # br, bc = rowcol(b)

    [(ar, ac), (br, bc)] = sorted([rowcol(src_i), rowcol(dst_i)])
    nrows = 0
    for r in range(ar, br):
        if boardl[r] == ["."] * width:
            nrows += gap_size
    # print("ER:", nrows)
    return nrows

@functools.cache
def empty_cols(src_i, dst_i):
    [(ar, ac), (br, bc)] = sorted([rowcol(src_i), rowcol(dst_i)], key=lambda x: x[1])
    ncols = 0
    for c in range(ac, bc):
        if all(boardl[r][c] == "." for r in range(height)):
            ncols += gap_size
    return ncols

shortest_paths = {}
total_dist = 0
for src_m in re.finditer(r"#", board):
    src_i = src_m.start()
    for dst_m in re.finditer(r"#", board):
        dst_i = dst_m.start()
        [(ar, ac), (br, bc)] = sorted([rowcol(src_i), rowcol(dst_i)])
        edge = (src_i, dst_i) if src_i < dst_i else (dst_i, src_i)
        if dst_i == src_i or edge in shortest_paths:
            continue

        nrows = empty_rows(src_i, dst_i)
        ncols= empty_cols(src_i, dst_i)
        dist = abs(ar - br) + abs(ac - bc) + nrows + ncols
        # print(f"{edge} has {nrows} empty_rows and {ncols} empty_cols")

        shortest_paths[edge] = dist
        total_dist += dist

# pprint.pprint(shortest_paths)
# print(len(shortest_paths))
print(total_dist)

# shortest_paths = {}
# for src_m in re.finditer(r"#", board):
#     src_i = src_m.start()
#     for dst_m in re.finditer(r"#", board):
#         dst_i = dst_m.start()
#         edge = (src_i, dst_i) if src_i < dst_i else (dst_i, src_i)
#         if dst_i == src_i or edge in shortest_paths:
#             continue
#
#         frontier = {src_i: 0}
#         visited = copy.copy(frontier)
#         while True:
#             new_frontier = {}
#             for i in frontier:
#                 row, col = rowcol(i)
#
#                 right_i = board_i(row, col + 1)
#                 left_i = board_i(row, col - 1)
#                 up_i = board_i(row - 1, col)
#                 down_i = board_i(row + 1, col)
#
#                 for next_i in filter(lambda x: x is not None, [right_i, left_i, up_i, down_i]):
#                     if next_i == dst_i
#                     new_frontier[next_i] = frontier[i] + 1
#
#             if new_frontier == {}:
#                 break
#             else:
#                 visited = dict(visited, **new_frontier)
#                 frontier = new_frontier
