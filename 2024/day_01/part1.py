from aoc_import import get_data

input_txt, example_txt = get_data(2024, 1)


clean_data: list[str] = input_txt.replace("   ", ",").replace("\n", ",").split(",")
# print(clean_data)
left_data: list[int] = sorted([int(x) for x in clean_data[0::2]])

right_data: list[int] = sorted([int(x) for x in clean_data[1::2]])
# print(left_data)
distance = [1] * len(left_data)

for i in range(len(distance)):
    distance[i] = abs(left_data[i] - right_data[i])
    # print(left_data[i],"-",right_data[i])

print(len(left_data), len(right_data))

print(sum(distance))
