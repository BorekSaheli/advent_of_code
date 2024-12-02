from aoc_import import get_data

input_txt, example1_txt, example2_txt = get_data(year=2024, day=2)

lines = input_txt.readlines()
counter = 0
for line in lines:
    line = [int(x) for x in line.strip().split()]

    for i, element in enumerate(line[:-2]):
        diff = element - line[i+1]
        diff_next = line[i+1] - line[i+2]
        if abs(diff) <= 3 and abs(diff_next) <= 3 and diff != 0 and diff_next !=0:
            if (diff > 0 and diff_next > 0) or (diff < 0 and diff_next < 0):
                if i+1 == len(line[:-2]):
                    #print(f"Safe {line}")
                    counter += 1
            else:
                #print(f"Unsafe {line}")
                break
        else:
            #print(f"Unsafe {line}")
            break

print(counter)

