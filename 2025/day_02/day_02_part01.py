with open("input.txt") as f:
    data = f.read().replace("\n", "").strip()


# data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""

data = data.split(",")

data = [[int(num_pair) for num_pair in num_range.split("-")] for num_range in data]


def count_repeats(data: list[list[int]]) -> int:
    count_repeats = 0
    for num_range in data:
        full_list = range(num_range[0], num_range[1] + 1)

        for num in full_list:
            num_str = str(num)

            if len(num_str) % 2 == 0 and len(num_str) > 1:
                num_len = len(num_str)
                first_half = num_str[0 : num_len // 2]
                second_half = num_str[num_len // 2 :]

                if first_half == second_half:
                    count_repeats += num
                    # print(f"repeded: pattern: {first_half} in {num}")
    return count_repeats


ans = count_repeats(data)
print(f"Ans is: {ans}")
