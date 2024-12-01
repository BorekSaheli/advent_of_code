with open("input.txt", "r") as file:
    data = file.read()


# data =  """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# """

clean_data: list[str] = data.replace("   ", ",").replace("\n", ",").split(",")[0:-1]

left_data: list[int] = [int(x) for x in clean_data[0::2]]

right_data: list[int] = [int(x) for x in clean_data[1::2]]


similarity_list = []
for left_item in left_data:
    count = 0
    for right_item in right_data:
        if left_item - right_item == 0:
            count += 1
    similarity_list.append(left_item * count)


print(len(left_data), len(right_data))
# print(similarity_list)

print(sum(similarity_list))
