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
print("---")
wrong_list: list[list[int]] = []
mid_values: list[int] = []


for pages in pages_list:
    wrong_counter = 0

    for p in range(len(pages)):
        current_page = pages[p]
        pages_after = pages[p + 1 :]
        check_after = all(item in rules[current_page]["after"] for item in pages_after)

        pages_before = pages[:p]
        check_before = all(
            item in rules[current_page]["before"] for item in pages_before
        )
        if not check_before or not check_after:
            wrong_counter += 1

    if wrong_counter != 0:
        wrong_list.append(pages)

print(wrong_list)

fixed_mid = []

for index, pages in enumerate(wrong_list, start=1):
    fixed = pages.copy()
    print(f"current list: index {index}: {fixed}")

    swapped = True
    while swapped:
        swapped = False
        for p in range(len(fixed) - 1):
            current_page = fixed[p]
            next_page = fixed[p + 1]

            if next_page in rules[current_page]["after"]:
                print(f"{current_page} should come after {next_page}")
                fixed[p], fixed[p + 1] = fixed[p + 1], fixed[p]
                swapped = True
                print(f"swapped to: {fixed}")
            # elif next_page in rules[current_page],["before"]:
            #    print(f"{current_page} should come before {next_page}")
            #    continue
        print("---")

    fixed_mid.append(fixed[len(fixed) // 2])

print(f"{sum(fixed_mid)}")
print(f"--- {time.time() - start_time} seconds ---")
