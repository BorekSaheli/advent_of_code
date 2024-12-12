

import time
from functools import lru_cache

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.read()

data = data.split()
# print(f"data: {data}")

@lru_cache(maxsize=None)
def process_stone(stone):
    # print(len(stone))
    if stone == '0':
        stone = ('1')
    elif len(stone) > 1 and len(stone) % 2 == 0:
        second_stone = stone[int(len(stone)/2):]
        leading_0_removed = ""
        counter = 0
        # print(second_stone)
        for i in range(len(second_stone)):
            if second_stone[i] == "0":
                if counter > 0 or (counter == 0 and i == len(second_stone) - 1):
                    leading_0_removed += second_stone[i]
            else:
                counter += 1
                leading_0_removed += second_stone[i]
        # print(leading_0_removed)
        stone = (stone[:int(len(stone)/2)], leading_0_removed)
    else:
        # print(stone)
        stone = (str(int(stone)*2024),)
    return stone

def new_arr_frequency(curr_freq):
    new_freq = {}
    for stone, count in curr_freq.items():
        # print(stone)
        new_stones = process_stone(stone)
        for ns in new_stones:
            if ns in new_freq:
                new_freq[ns] += count
            else:
                new_freq[ns] = count
    return new_freq

no_blinks =75 

curr_freq = {} # herw next time use defaultdict
for stone in data:
    if stone in curr_freq:
        curr_freq[stone] += 1
    else:
        curr_freq[stone] = 1

# print(f"initial freq: {curr_freq}")



for blink in range(no_blinks):
    print(f"blinked {blink+1} times")
    curr_freq = new_arr_frequency(curr_freq)
    # print(f"new freq: {curr_freq}")
#
total_stones = sum(curr_freq.values())
print(f"after {no_blinks} blinks of stones: {total_stones}")

print("")
print("=======================================")
print(f"--- {(time.time() - start_time)}s seconds ---")
print("=======================================")

