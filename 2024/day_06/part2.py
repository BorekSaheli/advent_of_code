import time

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.read().splitlines()

data = [x.strip() for x in data]


start_loc = None
for r, row in enumerate(data):
    for c, col in enumerate(row):
        if col == "^":
            start_loc = [r, c]
            break
    if start_loc is not None:
        break

original_data = [list(line) for line in data]


def out_of_bounds(row, column, grid):
    return row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0])


def up(cur_loc, grid):
    next_row = cur_loc[0] - 1
    current_col = cur_loc[1]
    turn = "up"
    turn_coor = ""

    if out_of_bounds(next_row, current_col, grid):
        return cur_loc, turn, True, turn_coor, grid

    look_ahead = grid[next_row][current_col]

    if look_ahead == "#":
        return cur_loc, "right", False, cur_loc.copy(), grid
    else:
        cur_loc = [next_row, current_col]

        return cur_loc, turn, False, turn_coor, grid


def down(cur_loc, grid):
    next_row = cur_loc[0] + 1
    curren_col = cur_loc[1]
    turn = "down"
    turn_coor = ""

    if out_of_bounds(next_row, curren_col, grid):
        return cur_loc, turn, True, turn_coor, grid

    look_ahead = grid[next_row][curren_col]

    if look_ahead == "#":
        return cur_loc, "left", False, cur_loc.copy(), grid
    else:
        cur_loc = [next_row, curren_col]

        return cur_loc, turn, False, turn_coor, grid


def left(cur_loc, grid):
    next_row = cur_loc[0]
    current_col = cur_loc[1] - 1
    turn = "left"
    turn_coor = ""

    if out_of_bounds(next_row, current_col, grid):
        return cur_loc, turn, True, turn_coor, grid

    look_ahead = grid[next_row][current_col]

    if look_ahead == "#":
        return cur_loc, "up", False, cur_loc.copy(), grid
    else:
        cur_loc = [next_row, current_col]

        return cur_loc, turn, False, turn_coor, grid


def right(cur_loc, grid):
    next_row = cur_loc[0]
    current_col = cur_loc[1] + 1
    turn = "right"
    turn_coor = ""

    if out_of_bounds(next_row, current_col, grid):
        return cur_loc, turn, True, turn_coor, grid

    look_ahead = grid[next_row][current_col]

    if look_ahead == "#":
        return cur_loc, "down", False, cur_loc.copy(), grid
    else:
        cur_loc = [next_row, current_col]

        return cur_loc, turn, False, turn_coor, grid


loop_counter = 0



for r in range(len(original_data)):
    print(f"Row {r} / {len(original_data)}")
    for c in range(len(original_data[0])):

        if (r, c) == (start_loc[0], start_loc[1]):
            continue
        if original_data[r][c] != ".":
            continue

        # must copy  over original data to avoid modifying it and must copy opever cant use .copy()
        current_grid = [row[:] for row in original_data]

        # place a new #
        current_grid[r][c] = "#"

        cur_loc = start_loc.copy()
        current_direction = "up"
        turn_coor = ""

        track_guard = {(tuple(start_loc), "up")}
        wall = False

        while not wall:
            if current_direction == "up":
                cur_loc, current_direction, wall, turn_coor, current_grid = up(
                    cur_loc, current_grid
                )
            elif current_direction == "down":
                cur_loc, current_direction, wall, turn_coor, current_grid = down(
                    cur_loc, current_grid
                )
            elif current_direction == "left":
                cur_loc, current_direction, wall, turn_coor, current_grid = left(
                    cur_loc, current_grid
                )
            elif current_direction == "right":
                cur_loc, current_direction, wall, turn_coor, current_grid = right(
                    cur_loc, current_grid
                )

            if wall:
                break

            state = (tuple(cur_loc), current_direction)
            if state in track_guard:
                # found loop
                loop_counter += 1
                break
            track_guard.add(state)

print(loop_counter)
print("\n=======================================")
print(f"--- {time.time() - start_time:.4f} seconds ---")
print("=======================================")
