import time
start_time = time.time()

with open("input.txt", "r") as file:
    data = file.readlines()




print("--- %s seconds ---" % (time.time() - start_time))
