from adventofcode.util.utils import *


def part1(inp) -> int:
    ranges = [tuple(a_range.strip().split("-")) for a_range in inp.split(',') if a_range.strip()]
    total = 0
    for start, end in ranges:
        if len(start) % 2 != 0 and len(start) == len(end):
            continue
        next_v = int(start) - 1
        while next_v <= int(end):
            if next_v != int(start) - 1:
                total += next_v
            next_v = next_number(next_v)

    return total


def next_number(num):
    num_str = str(num)
    num_len = len(num_str)

    if num_len % 2 != 0:
        return 10 ** num_len + 10 ** (num_len // 2)
    first = num_str[:num_len // 2]
    second = num_str[num_len // 2:]
    if int(second) < int(first):
        return int(f'{first}{first}')
    new_first = str(int(first) + 1)
    if len(new_first) > len(first):
        return next_number(int(f'{new_first}{second}'))
    return int(f'{new_first}{new_first}')


def part2(inp) -> int:
    ranges = [tuple(a_range.strip().split("-")) for a_range in inp.split(',') if a_range.strip()]
    total = 0
    for start, end in ranges:
        for num in range(int(start), int(end) + 1):
            if is_invalid(num):
                total += num

    return total


def is_invalid(num):
    num_str = str(num)
    for pairs in range(2, len(num_str) + 1):
        if len(num_str) % pairs != 0:
            continue
        window_size = len(num_str) // pairs
        invalid = True
        for digit_i in range(window_size):
            for pair_i in range(pairs - 1):
                i1 = num_str[pair_i * window_size + digit_i]
                i2 = num_str[((pair_i + 1) * window_size) + digit_i]
                if i1 != i2:
                    invalid = False
                    break
            if not invalid:
                break
        if invalid:
            return True
    return False


if __name__ == "__main__":
    test_input = """
    11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,
    824824821-824824827,2121212118-2121212124
    """
    act_input = read_file()

    test(part1(test_input), 1227775554)
    test(part1(act_input), 5398419778)

    test(part2(test_input), 4174379265)
    test(part2(act_input), 15704845910)

    print("All tests passed.")
