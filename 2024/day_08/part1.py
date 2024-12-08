import time

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.readlines()

data = [line.strip() for line in data]

# for line in data:
#     print(line)
#

coords_set = {}
for r, row in enumerate(data):
    for c, col in enumerate(row):
        if data[r][c] != ".":
            # print(r,c)
            key = data[r][c]
            if key in coords_set:
                coords_set[key].append((r, c))
            else:
                coords_set[key] = [(r, c)]


# print(coords_set)

antinodes = set()

keys = list(coords_set.keys())
for key in keys:
    coords = coords_set[key]

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            link = [coords[i], coords[j]]
            dv, dh = link[1][0] - link[0][0], link[1][1] - link[0][1]

            antinode1 = (link[1][0] + dv, link[1][1] + dh)
            antinode2 = (link[0][0] - dv, link[0][1] - dh)

            if (
                antinode1[0] >= 0
                and antinode1[0] < len(data)
                and antinode1[1] >= 0
                and antinode1[1] < len(data[0])
            ):
                print(f"valid antinode1: {antinode1}")
                antinodes.add(antinode1)

            if (
                antinode2[0] >= 0
                and antinode2[0] < len(data)
                and antinode2[1] >= 0
                and antinode2[1] < len(data[0])
            ):
                print(f"valid antinode2: {antinode2}")
                antinodes.add(antinode2)


print(len(antinodes))

for antinode in antinodes:
    r, c = antinode
    data[r] = data[r][:c] + "#" + data[r][c + 1 :]

for line in data:
    print(line)


print("")
print("=======================================")
print(f"--- {(time.time() - start_time)}s seconds ---")
print("=======================================")
