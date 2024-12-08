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
            print(f"link{link} dv: {dv}, dh: {dh}")

            for z in range(50):
                antinode_all_f = (link[1][0] + dv*z, link[1][1] + dh*z)
                antinode_all_b = (link[0][0] - dv*z, link[0][1] - dh*z)

                print(f"antinode_all_f: {antinode_all_f}, antinode_all_b: {antinode_all_b}")

                if antinode_all_f[0] >= 0 and antinode_all_f[0] < len(data) and antinode_all_f[1] >= 0 and antinode_all_f[1] < len(data[0]):
                    antinodes.add(antinode_all_f)
                if antinode_all_b[0] >= 0 and antinode_all_b[0] < len(data) and antinode_all_b[1] >= 0 and antinode_all_b[1] < len(data[0]): 
                    antinodes.add(antinode_all_b)

print(len(antinodes))

for antinode in antinodes:
    r, c = antinode
    data[r] = data[r][:c] + "#" + data[r][c + 1 :]

for line in data:
    print(line)
