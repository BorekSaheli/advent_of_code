import time

start_time = time.time()

with open("example1.txt", "r") as file:
    data = file.readlines()


print(data)


print("")
print("=======================================")
print(f"--- {(time.time() - start_time)}s seconds ---")
print("=======================================")
