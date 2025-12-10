with open("input.txt") as f:
    data = f.read().strip()

# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

data = data.split("\n")


def find_joltage(
    to_flip: int,
    line: str,
)-> int:

    # init spaces
    start_search_pos = 0
    end_search_pos = len(line) - to_flip + 1
    exclusion_space = line[:start_search_pos]
    search_space = line[start_search_pos:end_search_pos]
    buffer_space = line[end_search_pos:]

    current_joltage = ""

    for i in range(len(line)):
        max_num = max(search_space)
        for idx, num in enumerate(search_space):
            if max_num == num:
                max_num_pos = idx
                break

        # update spaces 
        start_search_pos = max_num_pos + 1 + len(exclusion_space)
        end_search_pos += 1
        current_joltage = current_joltage + max_num

        exclusion_space = line[:start_search_pos]
        search_space = line[start_search_pos:end_search_pos]
        buffer_space = line[end_search_pos - 1 :]

        # condtion to break
        # run out of search space
        if search_space == "":
            break

        # next max number at the boundry of the buffer start
        if start_search_pos + 1 == end_search_pos:
            current_joltage = current_joltage + buffer_space
            break

    # trim output when max number at boundty of buffer if buffer and current joltage exeed to_flip
    if len(current_joltage) > to_flip:
        current_joltage = current_joltage[:to_flip]

    return int(current_joltage)


total_joltage = 0
for line in data:
    total_joltage += find_joltage(to_flip=12, line=line)

print(f"The total joltage is: {total_joltage}")
