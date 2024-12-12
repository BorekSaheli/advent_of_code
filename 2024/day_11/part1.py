import time
start_time = time.time()

with open("input.txt", "r") as file:
    data = file.read()

data = data.split()
# print(f"data: {data}")


def process_stone(stone):
    # print(len(stone))
    if stone == '0':
        stone = ['1']
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

        stone = [stone[:int(len(stone)/2)] , leading_0_removed]
    else:
        # print(stone)
        stone = [str(int(stone)*2024)]


    return stone

# print(process_stone('1036288'))
def new_arr(curr_arr):
    new_stone_arr = []
    for stone in curr_arr:
        # print(stone) 
        new_stones = process_stone(stone)
        # print(new_stones)
        for ns in new_stones:
            new_stone_arr.append(ns)
    return new_stone_arr


no_blinks = 75

new_array = data

for blink in range(no_blinks):
    # print(new_array)
    # trakc time how long eacht ireation takes
    start_time2 = time.time()
    
    

    print(f"blinked {blink} times")
    new_array = new_arr(new_array)
    
    print(f"--- {(time.time() - start_time2)}s seconds ---")
# print(f" after {no_blinks} blinks: {new_array}")

print(f"after {no_blinks} blinks of stones:{len(new_array)}")
# print(int(001)
# for stone in data:
#     print(stone)

print("")
print("=======================================")
print(f"--- {(time.time() - start_time)}s seconds ---")
print("=======================================")
