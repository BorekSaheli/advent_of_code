with open("/home/borek/advent_of_code/2024/day_01/input.txt", "r") as file:
    data = file.read()


# data = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

clean_data: list[str] = data.replace("   ", ",").replace("\n", ",").split(",")[0:-1]

left_data: list[int] = sorted([int(x) for x in clean_data[0::2]])

right_data: list[int] = sorted([int(x) for x in clean_data[1::2]])

# print(left_data)
distance = [1] * len(left_data)

for i in range(len(distance)):
    distance[i] = abs(left_data[i] - right_data[i])
    # print(left_data[i],"-",right_data[i])

print(len(left_data), len(right_data))

print(sum(distance))
