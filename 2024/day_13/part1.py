import math
import re
import time

import numpy as np

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.read().splitlines()

eq_data = {}
id = 0
for i in range(0, len(data), 4):
    current_eq = data[i : i + 4]

    match = re.search(r"X([+-]?\d+), Y([+-]?\d+)", current_eq[0])
    x1_1 = int(match.group(1))
    x1_2 = int(match.group(2))

    match = re.search(r"X([+-]?\d+), Y([+-]?\d+)", current_eq[1])
    x2_1 = int(match.group(1))
    x2_2 = int(match.group(2))

    match = re.search(r"X=([+-]?\d+), Y=([+-]?\d+)", current_eq[2])
    ans1 = int(match.group(1))
    ans2 = int(match.group(2))

    eq_data[id] = {"eq1": [x1_1, x2_1, ans1], "eq2": [x1_2, x2_2, ans2]}
    id += 1

ans = 0
for i in eq_data:
    b = np.matrix([[eq_data[i]["eq1"][2]], [eq_data[i]["eq2"][2]]])

    A = np.matrix(
        [
            [eq_data[i]["eq1"][0], eq_data[i]["eq1"][1]],
            [eq_data[i]["eq2"][0], eq_data[i]["eq2"][1]],
        ]
    )

    x1, x2 = np.linalg.solve(A, b)
    x1 = x1.item()
    x2 = x2.item()
    # print(x1, x2)

    x1_rounded = int(round(x1))
    x2_rounded = int(round(x2))

    tol = 1e-4

    if (
        abs(x1 - x1_rounded) <= tol
        and abs(x2 - x2_rounded) <= tol
        and x1_rounded <= 100
        and x2_rounded <= 100
        and x1_rounded >= 0
        and x2_rounded >= 0
    ):
        ans += 3 * x1_rounded + 1 * x2_rounded

print(ans)
print("=======================================")
print(f"--- {(time.time() - start_time)} seconds ---")
print("=======================================")
