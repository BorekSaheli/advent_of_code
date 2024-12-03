import re

from aoc_import import get_data

input_txt, example1_txt, example2_txt = get_data(year=2024, day=3)
data = input_txt.read()

data = re.findall(r"mul[(]\d+,\d+[)]", data)

sum = 0
for mul in data:
    a, b = re.findall("[0-9]+,[0-9]+", mul)[0].split(",")
    sum += int(a) * int(b)

print(sum)
