with open("input.txt") as f:
    data = f.read().strip()

# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""
#
data = data.split("\n")
# data  = [int(line for line in data]

result_dict = {9: [], 8: [], 7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}


def build_dict(line: str) -> dict:
    result_dict = {9: [], 8: [], 7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}

    for idx in range(len(line)):
        char = int(line[idx])

        result_dict[char].append(idx)

    return result_dict


def find_ans(data):
    ans = 0

    for line in data:
        line_result = build_dict(line)

        first_digit = 0
        second_digit = 0
        second_digit_list = []
        for num in range(9, 0, -1):
            if line_result[num] != []:
                first_digit_pos = line_result[num][0]
                first_digit = num

                # if highest number is in last postion use second higest number
                if first_digit_pos == len(line) - 1:
                    continue
                else:
                    line_result[num].remove(first_digit_pos)
                    break

        for num2 in range(9, 0, -1):
            if line_result[num2] != []:
                for pos in line_result[num2]:
                    if pos >= first_digit_pos:
                        second_digit_list.append(num2)

        second_digit = max(second_digit_list)

        ans += int(str(first_digit) + str(second_digit))

    return ans


print(find_ans(data))
