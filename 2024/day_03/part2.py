import re

from aoc_import import get_data

input_txt, example1_txt, example2_txt = get_data(year=2024, day=3)
data = input_txt.read()

data = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
data = [r"do()"] + data

sum = 0

for mul in data:
    if mul == r"do()":
        mul_bool = True
    elif mul == r"don't()":
        mul_bool = False

    if mul_bool and mul not in {r"do()", r"don't()"}:
        print(mul)
        a, b = re.findall("[0-9]+,[0-9]+", mul)[0].split(",")

        sum += int(a) * int(b)

print(sum)
