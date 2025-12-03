from adventofcode.util.utils import *

up_to = 100


def part1(inp) -> int:
    return calc_all_zeros(inp, calc_zeros1)


def part2(inp) -> int:
    return calc_all_zeros(inp, calc_zeros2)


def calc_all_zeros(inp, calc_fn) -> int:
    lines = inp.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    position = 50
    zero_count = 0
    for op in lines:
        append_v, new_pos = calc_fn(op, position)
        position = new_pos
        zero_count += append_v
    return zero_count


def calc_zeros1(op: str, position: int) -> tuple[int, int]:
    sign = 1 if op[0] == "R" else -1
    value = int(op[1:])
    new_pos_raw = (position + (value * sign))
    new_pos = new_pos_raw % up_to
    if new_pos < 0:
        new_pos = up_to + new_pos
    zeros = 1 if position == 0 else 0
    return zeros, new_pos


def calc_zeros2(op: str, position: int) -> tuple[int, int]:
    sign = 1 if op[0] == "R" else -1
    value = int(op[1:])
    new_pos_raw = (position + (value * sign))
    new_pos = new_pos_raw % up_to
    if new_pos < 0:
        new_pos = up_to + new_pos
    zeros = abs(new_pos_raw) // up_to
    if new_pos_raw == 0 or new_pos_raw < 0 < position:
        zeros += 1
    return zeros, new_pos


if __name__ == "__main__":
    test_input = """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
        """
    act_input = read_file()

    test(part1(test_input), 3)
    test(part1(act_input), 1120)

    test(part2(test_input), 6)
    test(part2(act_input), 6554)

    print("All tests passed.")
