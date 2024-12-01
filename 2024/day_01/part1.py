from aoc_import import get_data

input_txt, example1_txt, example2_txt = get_data(year=2024, day=1)

clean_data: list[str] = input_txt.replace("   ", ",").replace("\n", ",").split(",")
left_data: list[int] = sorted([int(x) for x in clean_data[0::2]])

right_data: list[int] = sorted([int(x) for x in clean_data[1::2]])
distance = [1] * len(left_data)

for i in range(len(distance)):
    distance[i] = abs(left_data[i] - right_data[i])

print(sum(distance))
