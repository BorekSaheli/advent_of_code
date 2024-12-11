import time

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.read()


id = 0
if len(data) % 2 != 0:
    data += "0"


highest_id = int(len(data)/2) - 1
# print(highest_id)
left = []
right = []
file_id = 0
gap_len = 0
for i in range(0,len(data),2):
    
    
    for j in range(int(data[i])):
        left.append(file_id)

    for j in range(int(data[i+1])):
        left.append(".")
        gap_len += 1

    for j in range(int(data[len(data) - 2- i])):
        right.append(highest_id)
    for j in range(int(data[len(data)-2 - 1-i])):
        # right.append(".")
        pass

    highest_id -= 1
    file_id += 1
    
#
merged = []
r =0
# print(gap_len)
for l in range(len(left)-gap_len):
    if left[l] != ".":
        merged.append(left[l])
    else:
        merged.append(right[r])
        r += 1

# print(merged)
total = 0
for i, val in enumerate(merged):
    total += val * i 

print(total)


print("")
print("=======================================")
print(f"--- {(time.time() - start_time)}s seconds ---")
print("=======================================")
