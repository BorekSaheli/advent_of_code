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
        return -int(code[1::])
    else:
        return 0


def main(input: list[str], start_val: int = 50) -> tuple[int, int]:
    current_position = start_val
    counter = 0
    passed_zero_counter = 0

    for code in input:
        move = parse_direction(code)
        spin_val_not_modded = move + current_position
        spin_val = spin_val_not_modded % 100

        if move > 0:
            extra_spins = (spin_val_not_modded // 100)
        elif move < 0:
            extra_spins = abs((spin_val_not_modded - 1) // 100)
            if current_position == 0:
                extra_spins -= 1
        else:
            extra_spins = 0

        passed_zero_counter += extra_spins

        current_position = spin_val

        if current_position == 0:
            counter += 1

    return counter, passed_zero_counter

landed, passed = main(input=input, start_val = 50)

print(f"Landed on 0: {landed} times")

print(f"Passed 0: {passed} times")
