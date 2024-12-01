with open("/home/borek/advent_of_code/2024/day_01/input.txt", "r") as file:
    data = file.read()


#data =  """3   4
#4   3
#2   5
#1   3
#3   9
#3   3
#"""

clean_data = data.replace("   ",",").replace("\n",",").split(",")[0:-1]

left_data = clean_data[0::2]
left_data = ([int(x) for x in left_data]) 

right_data = clean_data[1::2]
right_data = ([int(x) for x in right_data]) 


similarity_list = []
for left_item in left_data:
    count = 0
    for right_item in right_data:
        if left_item - right_item == 0:
            count += 1
    similarity_list.append(left_item * count)
        


print(len(left_data),len(right_data))
#print(similarity_list)

print(sum(similarity_list))
