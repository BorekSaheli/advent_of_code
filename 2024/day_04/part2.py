import time

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.readlines()

data = [line.strip() for line in data]

word = "MAS"
A_pos = []
xmas_countr = 0

for row in range(len(data) - 0):
    for col in range(len(data[row])):
        to_top_edge = row + 1
        to_bot_edge = len(data) - row
        to_left_edge = col + 1
        to_right_edge = len(data[row]) - col

        # print(f"current_char:={data[row][col]}=")
        # print(
        #     f"top:{to_top_edge},bot:{to_bot_edge}, left:{to_left_edge}, right:{to_right_edge}"
        # )

        if to_bot_edge >= len(word) and to_right_edge >= len(word):  # SE
            counter = 0
            for i in range(len(word)):
                if word[counter] == data[row + i][col + i]:
                    counter += 1
                    # print(f"Matched {word[counter-1]} with {data[row + i][col + i]}")
                    if counter == len(word):
                        xmas_countr += 1
                        print(data[row + 1][col + 1], [row + 1, col + 1], "SE")
                        A_pos.append([row + 1, col + 1])
                        break
                else:
                    break

        if to_bot_edge >= len(word) and to_left_edge >= len(word):  # SW
            counter = 0
            for i in range(len(word)):
                if word[counter] == data[row + i][col - i]:
                    counter += 1
                    # print(f"Matched {word[counter-1]} with {data[row + i][col - i]}")
                    if counter == len(word) - 0:
                        xmas_countr += 1
                        A_pos.append([row + 1, col - 1])
                        print(data[row + 1][col - 1], [row + 1, col - 1], "SW")
                        break
                else:
                    break

        if to_top_edge >= len(word) and to_right_edge >= len(word):  # NE
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row - i][col + i])
                if word[counter] == data[row - i][col + i]:
                    counter += 1
                    # print(f"Matched {word[counter-1]} with {data[row - i][col + i]}")
                    if counter == len(word) - 0:
                        xmas_countr += 1
                        A_pos.append([row - 1, col + 1])
                        print(data[row - 1][col + 1], [row - 1, col + 1], "NE")
                        break
                else:
                    break

        if to_top_edge >= len(word) and to_left_edge >= len(word):  # NW
            counter = 0
            for i in range(len(word)):
                if word[counter] == data[row - i][col - i]:
                    counter += 1
                    # print(f"Matched {word[counter-1]} with {data[row - i][col - i]}")
                    if counter == len(word) - 0:
                        xmas_countr += 1
                        A_pos.append([row - 1, col - 1])
                        print(data[row - 1][col - 1], [row - 1, col - 1], "NW")
                        break
                else:
                    break


literal_x_counter = 0
for i in range(len(A_pos)):
    for j in range(i + 1, len(A_pos)):
        if A_pos[i] == A_pos[j]:
            literal_x_counter += 1

print("Total duplicate pairs:", literal_x_counter)
print("--- %s seconds ---" % (time.time() - start_time))
