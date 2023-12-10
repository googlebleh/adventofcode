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

def rowcol(board_i):
    return board_i // width, board_i % width

def all_adjacent(i):
    row, col = rowcol(i)
    for drow in range(-1, 2):
        for dcol in range(-1, 2):
            if drow == 0 and dcol == 0:
                continue

            adj_row = row + drow
            adj_col = col + dcol
            if (0 <= adj_row < height) and (0 <= adj_col < width):
                yield board_i(adj_row, adj_col)

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
while True:
    new_frontier = {}
    for i in frontier:
        row, col = rowcol(i)

        right_i = board_i(row, col + 1)
        left_i = board_i(row, col - 1)
        up_i = board_i(row - 1, col)
        down_i = board_i(row + 1, col)

        print(f"src={board[i]}")

        if right_i not in visited:
            if board[i] in "S-LF" and board[right_i] in "-J7":
                visited.add(right_i)
                new_frontier[right_i] = depth
        if left_i not in visited:
            if board[i] in "S-J7" and board[left_i] in "-LF":
                visited.add(left_i)
                new_frontier[left_i] = depth
        if up_i not in visited:
            if board[i] in "S|LJ" and board[up_i] in "|7F":
                visited.add(up_i)
                new_frontier[up_i] = depth
        if down_i not in visited:
            if board[i] in "S|7F" and board[down_i] in "|LJ":
                visited.add(down_i)
                new_frontier[down_i] = depth
    if new_frontier == {}:
        for k, v in frontier.items():
            print(f"{rowcol(k)}:{v}")
        break
    frontier = new_frontier
    depth += 1
