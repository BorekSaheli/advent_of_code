
import time

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.readlines()

data = [x.strip() for x in data]

zeros = []
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == "0":
            zeros.append([row, col])


def next_location(current_pos, data):
    row, col = current_pos
    directions = [
        (row, col - 1),  # left
        (row + 1, col),  # down
        (row, col + 1),  # right
        (row - 1, col),  # up
    ]

    next_loc = []
    for new_row, new_col in directions:
        if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]):
            next_loc.append([new_row, new_col])

    return next_loc


def find_branches(coord, data):
    current_num, current_pos = coord
    if current_num == 9:
        return [[-1, [-1, -1]]]  # 9 reached
    else:
        next_loc = next_location(current_pos, data)
        branch_from = []

        next_int = str(current_num + 1)
        for pot_loc in next_loc:
            pot_val = data[pot_loc[0]][pot_loc[1]]
            if next_int == pot_val:
                branch_from.append([current_num + 1, pot_loc])

        return branch_from


trail_order = 0
sum_trails = 0

for zero in zeros:
    trail_count = 0  
    queue = []

    current_step = [0, zero]

    while current_step is not None:
        current_num, current_pos = current_step
        row, col = current_pos

        branches = find_branches(current_step, data)

        if branches == [[-1, [-1, -1]]]:
            # 9 reached
            trail_count += 1
            current_step = None

            # load queue
            if queue:
                current_step = queue.pop(0)
            continue

        if len(branches) > 1:
            # add to queue if more than one branch exists
            for branch in branches[1:]:
                queue.append(branch)

        if branches:
            next_num, next_pos = branches[0]
            current_step = [next_num, next_pos]
        else:
            current_step = None
            if queue:
                current_step = queue.pop(0)

    sum_trails += trail_count

print("--")
print(f"sum of trailhead ratings: {sum_trails}")


print("")
print("=======================================")
print(f"--- {(time.time() - start_time)}s seconds ---")
print("=======================================")

