import time

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.readlines()

data = [x.strip() for x in data]

for r, row in enumerate(data):
    for c, col in enumerate(row):
        if data[r][c] == "^":
            start_loc = [r, c]
            break

grid = data.copy()


def up(cur_loc):
    cur_loc[0] = cur_loc[0] - 1

    turn = "up"
    wall = False
    row = grid[cur_loc[0]]
    row = row[: cur_loc[1]] + "X" + row[cur_loc[1] + 1 :]

    look_ahead = grid[cur_loc[0] - 1][cur_loc[1]]
    if look_ahead == ".":
        pass
    elif look_ahead == "#":
        turn = "right"
    if cur_loc[0] == 0 or cur_loc[0] == len(grid) - 1:
        wall = True
    grid[cur_loc[0]] = row

    return cur_loc, turn, wall


def down(cur_loc):
    cur_loc[0] = cur_loc[0] + 1

    turn = "down"
    wall = False
    row = grid[cur_loc[0]]
    row = row[: cur_loc[1]] + "X" + row[cur_loc[1] + 1 :]
    if cur_loc[0] == 0 or cur_loc[0] == len(grid) - 1:
        wall = True
    else:
        look_ahead = grid[cur_loc[0] + 1][cur_loc[1]]
        if look_ahead == ".":
            pass
        elif look_ahead == "#":
            turn = "left"
    grid[cur_loc[0]] = row

    return cur_loc, turn, wall


def left(cur_loc):
    cur_loc[1] = cur_loc[1] - 1

    turn = "left"
    wall = False
    row = grid[cur_loc[0]]
    row = row[: cur_loc[1]] + "X" + row[cur_loc[1] + 1 :]

    look_ahead = grid[cur_loc[0]][cur_loc[1] - 1]
    if look_ahead == ".":
        pass
    elif look_ahead == "#":
        turn = "up"
    if cur_loc[1] == 0 or cur_loc[1] == len(grid[0]) - 1:
        wall = True
    grid[cur_loc[0]] = row

    return cur_loc, turn, wall


def right(cur_loc):
    cur_loc[1] = cur_loc[1] + 1

    turn = "right"
    wall = False
    row = grid[cur_loc[0]]
    row = row[: cur_loc[1]] + "X" + row[cur_loc[1] + 1 :]
    if cur_loc[1] == 0 or cur_loc[1] == len(grid[0]) - 1:
        wall = True
    else:
        look_ahead = grid[cur_loc[0]][cur_loc[1] + 1]
        if look_ahead == ".":
            pass
        elif look_ahead == "#":
            turn = "down"

    grid[cur_loc[0]] = row

    return cur_loc, turn, wall


cur_loc = start_loc
turn = "up"
wall = False
while not wall:
    print(turn,wall)
    if turn == "up":
        cur_loc, turn, wall = up(cur_loc)
    elif turn == "down":
        cur_loc, turn, wall = down(cur_loc)
    elif turn == "left":
        cur_loc, turn, wall = left(cur_loc)
    elif turn == "right":
        cur_loc, turn, wall = right(cur_loc)

for row in grid:
    print(row)
counter = 0
for row in grid:
    for i in range(len(row)):
        if row[i] == "X":
            counter += 1

print(counter)

print("")
print("=======================================")
print(f"--- {(time.time() - start_time)}s seconds ---")
print("=======================================")
