from aoc_import import get_data

input_txt, example_txt = get_data(year=2024, day=1)

clean_data: list[str] = input_txt.replace("   ", ",").replace("\n", ",").split(",")

left_data: list[int] = [int(x) for x in clean_data[0::2]]

right_data: list[int] = [int(x) for x in clean_data[1::2]]


similarity_list = []
for left_item in left_data:
    count = 0
    for right_item in right_data:
        if left_item - right_item == 0:
            count += 1
    similarity_list.append(left_item * count)


print(sum(similarity_list))
