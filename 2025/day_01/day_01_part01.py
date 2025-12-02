with open("input.txt") as f:
    input = f.read()

# input = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

input: list[str] = input.split()


def parse_direction(code: str) -> int:
    if code[0] == "R":
        return int(code[1::])
    elif code[0] == "L":
        return -1 * int(code[1::])
    else:
        return 0


def main(input: list[str], start_val: int = 50) -> int:
    spin_values = list(range(0, 100))
    current_position = start_val
    counter = 0

    for code in input:
        spin_val = (parse_direction(code) + current_position) % 100
        current_position = spin_values[spin_val]

        if current_position == 0:
            counter += 1

    return counter


print(f"Landed on 0: {main(input, 50)} times")
