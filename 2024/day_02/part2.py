from aoc_import import get_data

input_txt, example1_txt, example2_txt = get_data(year=2024, day=2)


lines = input_txt.readlines()
counter = 0

count_real = 0


for line in lines:
    line = [int(x) for x in line.strip().split()]

    possible_pops = [line]
    for i in range(len(line)):
        temp_line = line.copy()
        temp_line.pop(i)
        possible_pops.append(temp_line)

    counter = 0

    for current_line in possible_pops:
        for i in range(len(current_line) - 2):
            element = current_line[i]
            diff = element - current_line[i + 1]
            diff_next = current_line[i + 1] - current_line[i + 2]
            if abs(diff) <= 3 and abs(diff_next) <= 3 and diff != 0 and diff_next != 0:
                if (diff > 0 and diff_next > 0) or (diff < 0 and diff_next < 0):
                    if i + 1 == len(current_line) - 2:
                        # print(f"Safe {current_line}")
                        counter += 1
                else:
                    # print(f"Unsafe {current_line}")
                    break
            else:
                # print(f"Unsafe {current_line}")
                break

    if counter > 0:
        count_real += 1

print(count_real)
