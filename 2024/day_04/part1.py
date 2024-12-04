with open("input.txt", "r") as file:
    data = file.readlines()

data = [line.strip() for line in data]

word = "XMAS"

xmas_countr = 0

for row in range(len(data) - 0):
    # print(data[row])
    for col in range(len(data[row])):
        # print(data[row][col])
        # positions
        to_top_edge = row + 1
        to_bot_edge = len(data) - row - 0
        to_left_edge = col + 1
        to_right_edge = len(data[row]) - col - 0
        print(f"current_char:={data[row][col]}=")
        print(
            f"top:{to_top_edge},bot:{to_bot_edge}, left:{to_left_edge}, right:{to_right_edge}"
        )

        if to_right_edge >= len(word):  # E
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row][col + i])
                if word[counter] == data[row][col + i]:
                    counter += 1
                    print(f"Matched {word[counter-1]} with {data[row][col + i]}")
                    if counter == len(word) - 0:
                        xmas_countr += 1
                        print(f"found Xmas {xmas_countr}")

                        break
                else:
                    break

        if to_left_edge >= len(word):  # W
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row][col - i])
                if word[counter] == data[row][col - i]:
                    counter += 1
                    print(f"Matched {word[counter-1]} with {data[row][col - i]}")
                    if counter == len(word) - 0:
                        xmas_countr += 1
                        print(f"found Xmas {xmas_countr}")

                        break
                else:
                    break

        if to_bot_edge >= len(word):  # S
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row + i][col])
                if word[counter] == data[row + i][col]:
                    counter += 1
                    print(f"Matched {word[counter-1]} with {data[row + i][col]}")
                    if counter == len(word) - 0:

                        xmas_countr += 1
                        print(f"found Xmas {xmas_countr}")

                        break
                else:
                    break

        if to_top_edge >= len(word):  # N
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row - i][col])
                if word[counter] == data[row - i][col]:
                    counter += 1
                    print(f"Matched {word[counter-1]} with {data[row - i][col]}")
                    if counter == len(word) - 0:


                        xmas_countr += 1
                        print(f"found Xmas {xmas_countr}")

                        break
                else:
                    break

        if to_bot_edge >= len(word) and to_right_edge >= len(word):  # SE
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row + i][col + i])
                if word[counter] == data[row + i][col + i]:
                    counter += 1
                    print(f"Matched {word[counter-1]} with {data[row + i][col + i]}")
                    if counter == len(word) - 0:


                        xmas_countr += 1
                        print(f"found Xmas {xmas_countr}")

                        break
                else:
                    break

        if to_bot_edge >= len(word) and to_left_edge >= len(word):  # SW
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row + i][col - i])
                if word[counter] == data[row + i][col - i]:
                    counter += 1
                    print(f"Matched {word[counter-1]} with {data[row + i][col - i]}")
                    if counter == len(word) - 0:


                        xmas_countr += 1
                        print(f"found Xmas {xmas_countr}")

                        break
                else:
                    break

        if to_top_edge >= len(word) and to_right_edge >= len(word):  # NE
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row - i][col + i])
                if word[counter] == data[row - i][col + i]:
                    counter += 1
                    print(f"Matched {word[counter-1]} with {data[row - i][col + i]}")
                    if counter == len(word) - 0:


                        xmas_countr += 1
                        print(f"found Xmas {xmas_countr}")

                        break
                else:
                    break

        if to_top_edge >= len(word) and to_left_edge >= len(word):  # NW
            counter = 0
            for i in range(len(word)):
                # print(i, "-", data[row - i][col - i])
                if word[counter] == data[row - i][col - i]:
                    counter += 1
                    print(f"Matched {word[counter-1]} with {data[row - i][col - i]}")
                    if counter == len(word) - 0:

                        xmas_countr += 1
                        print(f"found Xmas {xmas_countr}")

                        break
                else:
                    break



print(xmas_countr)
