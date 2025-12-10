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
) -> int:
    start_search_pos = 0
    end_search_pos = len(line) - to_flip + 1
    search_space = line[start_search_pos:end_search_pos]

    current_joltage = ""

    while start_search_pos + 1 < end_search_pos and search_space:
        max_num = max(search_space)
        max_num_pos = search_space.find(max_num)

        start_search_pos = max_num_pos + 1 + start_search_pos
        end_search_pos += 1
        search_space = line[start_search_pos:end_search_pos]

        current_joltage = current_joltage + max_num

    current_joltage += line[end_search_pos - 1 :]

    return int(current_joltage[:to_flip])


total_joltage = 0
for line in data:
    total_joltage += find_joltage(to_flip=12, line=line)

print(f"The total joltage is: {total_joltage}")
