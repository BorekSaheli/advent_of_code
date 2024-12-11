import time

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.read().strip()

if len(data) % 2 != 0:
    data += "0"

highest_id = int(len(data) / 2) - 1
left = []
right = []
file_id = 0
gap_len = 0
local_gap = []
local_id_repeat = []

for i in range(0, len(data), 2):
    front_file_len = int(data[i])
    front_gap_len = int(data[i + 1])

    for j in range(front_file_len):
        left.append(file_id)
    for j in range(front_gap_len):
        left.append(".")
        gap_len += 1
    local_gap.append(front_gap_len)

    back_file_len = int(data[len(data) - 2 - i])
    back_gap_len = int(data[len(data) - 3 - i])

    for j in range(back_file_len):
        right.append(highest_id)
    for j in range(back_gap_len):
        right.append(".")

    local_id_repeat.append(back_file_len)
    highest_id -= 1
    file_id += 1

seen_counter = 0

for n, num in enumerate(right):
    print(num)

    if num != ".":
        seen_counter += 1

    if n + 1 < len(right):
        next_num = right[n + 1]
    else:
        next_num = "."

    if next_num != num and num != ".":
        # fix locs to have index of the left correct array
        all_locs = [len(left) - i - 1 for i, x in enumerate(right) if x == num]

        block = {"w": seen_counter, "val": num, "loc": all_locs}
        # print(f"block: {block}")

        # block 00 can never move
        if block["val"] == 0:
            break

        updated_list = left
        gap_count = 0

        for j, num_l in enumerate(left):
            if updated_list[j] == ".":
                gap_count += 1
            else:
                gap_count = 0

            if gap_count == block["w"]:
                start_pos = j - block["w"] + 1
                end_pos = j + 1

                if end_pos <= min(block["loc"]):
                    # print(f"found gap at {j}")
                    # place block
                    for k in range(start_pos, end_pos):
                        updated_list[k] = block["val"]
                    # overwrite old block positions with '.'
                    for o in block["loc"]:
                        updated_list[o] = "."
                    # print(updated_list)
                    break

        seen_counter = 0

ans = 0
for i, id in enumerate(updated_list):
    if id != ".":
        ans += i * id

print("--")
print(f"ans: {ans}:")
print("--")
# print(updated_list)
print("--")
print("")
print("=======================================")
print(f"--- {(time.time() - start_time)}s seconds ---")
print("=======================================")
