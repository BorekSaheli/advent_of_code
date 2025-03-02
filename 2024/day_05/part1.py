import time
from typing import Dict, List

start_time = time.time()

with open("input.txt", "r") as file:
    data: List[str] = [line.strip() for line in file.readlines()]

rules: Dict[int, Dict[str, List[int]]] = {}
pages_list: List[List[int]] = []
pages_bool: bool = False

for item in data:
    if item == "":
        pages_bool = True
        continue

    if pages_bool:
        values_str: List[str] = item.split(",")
        values: List[int] = [int(val) for val in values_str]
        pages_list.append(values)
    else:
        key_str, value_str = item.split("|")
        key: int = int(key_str)
        value: int = int(value_str)

        if key not in rules:
            rules[key] = {"after": [], "before": []}
        rules[key]["after"].append(value)

        if value not in rules:
            rules[value] = {"after": [], "before": []}
        rules[value]["before"].append(key)

print(rules)

correct_list = []
mid_values = []


for pages in pages_list:
    wrong_counter = 0

    for p in range(len(pages)):
        current_page = pages[p]
        print(current_page)
        pages_after = pages[p + 1 :]
        check_after = all(item in rules[current_page]["after"] for item in pages_after)

        # print(f"after {pages_after}")

        pages_before = pages[:p]
        check_before = all(
            item in rules[current_page]["before"] for item in pages_before
        )

        # print(f"before {pages_before}")

        print(f"b={check_before},after={check_after}")

        if not check_before or not check_after:
            wrong_counter += 1

    if wrong_counter == 0:
        correct_list.append(pages)
        mid_values.append(pages[len(pages) // 2])

print(correct_list)
print(sum(mid_values))


print(f"--- {time.time() - start_time} seconds ---")
