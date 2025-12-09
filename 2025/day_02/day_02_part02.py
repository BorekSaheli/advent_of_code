with open("input.txt") as f:
    data = f.read().replace("\n", "").strip()


# data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""

data = data.split(",")

data = [[int(num_pair) for num_pair in num_range.split("-")] for num_range in data]


def list_divider(value: int, section_size: int, divider) -> list[str]:
    num_str = str(value)
    output_list = []
    for i in range(1, divider + 1):
        output_list.append(num_str[section_size * (i - 1) : section_size * i])

    return output_list


def find_hole_devisions(num: int) -> list[list[str]]:
    num_str = str(num)
    len_str = len(num_str)

    all_possible = []

    for divider in range(2, len_str + 1):
        mod = len_str % divider
        if mod == 0:
            section_size = len_str // divider
            all_possible.append(list_divider(num, section_size, divider))

    return all_possible


def count_repeats(data: list[list[int]]) -> int:
    count_repeats = 0
    for num_range in data:
        full_list = range(num_range[0], num_range[1] + 1)

        for num in full_list:
            possibilities = find_hole_devisions(int(num))

            last_num = ""
            full_num = ""
            for section in possibilities:
                is_repeaded: bool = len(set(section)) == 1

                if is_repeaded:
                    full_num = "".join(section)
                    if full_num != last_num:
                        count_repeats += int(full_num)
                        # print(f" doubles found for ({int(full_num)}) in section{section}")

                last_num = full_num

    return count_repeats


ans = count_repeats(data)
print(f"Ans is: {ans}")
