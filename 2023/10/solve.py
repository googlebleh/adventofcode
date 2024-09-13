import fileinput
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position

board = ""
height = 0
for line in fileinput.input():
    row = line.strip()
    width = len(row)
    height += 1
    board += row

def board_i(row, col):
    return row * width + col

def rowcol(bi):
    return bi // width, bi % width

def is_valid_move(src, dst):
    if board[src] == "|":
        return board[dst] in "L|J"
    elif board[src] == "-":
        return board[dst] in "L|J"
    elif board[src] == "L":
        return board[dst] in "L|J"
    elif board[src] == "J":
        return board[dst] in "L|J"
    elif board[src] == "7":
        return board[dst] in "L|J"
    elif board[src] == "F":
        return board[dst] in "L|J"
    else:
        print("error:", rowcol(src), rowcol(dst))
        1/0

visited = {None}
frontier = {}
start_i = board.index("S")
frontier[start_i] = 0
depth = 1
edges = []
while True:
    new_frontier = {}
    for i in frontier:
        row, col = rowcol(i)

        right_i = board_i(row, col + 1)
        left_i = board_i(row, col - 1)
        up_i = board_i(row - 1, col)
        down_i = board_i(row + 1, col)

        # print(f"src={board[i]}")

        if right_i not in visited:
            if board[i] in "S-LF" and board[right_i] in "-J7":
                visited.add(right_i)
                new_frontier[right_i] = depth
                edges.append(((row, col), rowcol(right_i)))
        if left_i not in visited:
            if board[i] in "S-J7" and board[left_i] in "-LF":
                visited.add(left_i)
                new_frontier[left_i] = depth
                edges.append(((row, col), rowcol(left_i)))
        if up_i not in visited:
            if board[i] in "S|LJ" and board[up_i] in "|7F":
                visited.add(up_i)
                new_frontier[up_i] = depth
                edges.append(((row, col), rowcol(up_i)))
        if down_i not in visited:
            if board[i] in "S|7F" and board[down_i] in "|LJ":
                visited.add(down_i)
                new_frontier[down_i] = depth
                edges.append(((row, col), rowcol(down_i)))
    if new_frontier == {}:
        # for k, v in frontier.items():
        #     print(f"{rowcol(k)}:{v}")
        break
    frontier = new_frontier
    depth += 1

def zoomout(edge_list):
    for ((r1, c1), (r2, c2)) in edge_list:
        yield ((r1 * 10, c1 * 10), (r2 * 10, c2 * 10))

edges = zoomout(edges)

# newboard = ""
# for r in range(height):
#     row = []
#     for c in range(width):
#         row.append(board[board_i(r, c)])
#         row.extend("0" * 9)
#     newboard.append("".join(row) + ("0" * len(row) * 9))

def intersect(p1, p2, p3, p4):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0: # parallel
        return None
    ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    if ua < 0 or ua > 1: # out of range
        return None
    ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if ub < 0 or ub > 1: # out of range
        return None
    x = x1 + ua * (x2-x1)
    y = y1 + ua * (y2-y1)
    return (x,y)

def any_intersect(p1, p2):
    for p3, p4 in edges:
        if intersect(p1, p2, p3, p4) is not None:
            return True
    return False

def zoomout_pair(x, y):
    return (x * 10, y * 10)

def my_rowcol(i):
    return ((i // width) * 10, (i % width) * 10)

def all_adjacent(rc):
    row, col = rc
    for drow in range(-1, 2):
        for dcol in range(-1, 2):
            if drow == 0 and dcol == 0:
                continue

            adj_row = row + drow
            adj_col = col + dcol
            if (0 <= adj_row < (height*10)) and (0 <= adj_col < (width * 10)):
                yield (adj_row, adj_col)
            else:
                yield "out!"


def can_escape(rc, seen=set()):
    for next_i in all_adjacent(rc):
        print("checking", rc, "-->", next_i)
        if next_i == "out!":
            return True
        if any_intersect(rc, next_i):
            continue
        if next_i not in seen:
            seen.add(next_i)
            if can_escape(next_i, seen):
                return True
    return False

ntiles = 0
for i, c in enumerate(board):
    if c != ".":
        continue
    if not can_escape(my_rowcol(i)):
        print(rowcol(i))
        ntiles += 1
print("part2", ntiles)
