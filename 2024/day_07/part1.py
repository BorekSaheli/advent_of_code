import itertools
import time

start_time = time.time()

with open("input.txt", "r") as file:
    data = file.readlines()

data = [line.strip().split(":") for line in data]
ans = [int(line[0].strip()) for line in data]
nums = [list(map(int, line[1].split())) for line in data]

data = []
for i, ans in enumerate(ans):
    data.append([ans, nums[i]])


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


signs = ["+", "*"]
ans_sum = 0


for eq_index, eq in enumerate(data):
    lhs, rhs_num = eq[0], eq[1]
    gap_count = len(rhs_num) - 1
    possible_signs = itertools.product(signs, repeat=gap_count)

    expressions = []

    for sign_tuple in possible_signs:
        expression = []
        for i, num in enumerate(rhs_num):
            expression.append(num)
            if i < gap_count:
                expression.append(sign_tuple[i])
        expressions.append(expression)

    print(f"\neq: {eq_index + 1}: LHS = {lhs}")
    for expr in expressions:
        print(expr)

    for expr in expressions:
        total = expr[0]
        for i in range(1, len(expr), 2):
            operator = expr[i]
            num = expr[i + 1]
            if operator == "+":
                total = add(total, num)
            elif operator == "*":
                total = multiply(total, num)
        if total == lhs:
            ans_sum += lhs
            print(f"matching expr: {expr} = {lhs}")
            break 
print(f"ans: {ans_sum}")

print("\n=======================================")
print(f"--- {time.time() - start_time:.4f} seconds ---")
print("=======================================")
