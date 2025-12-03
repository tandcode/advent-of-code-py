from adventofcode.util.utils import *


def part1(inp) -> int:
    return total_jolts_with_num(inp, 2)


def part2(inp) -> int:
    return total_jolts_with_num(inp, 12)


def total_jolts_with_num(inp, num) -> int:
    banks = [bank.strip() for bank in inp.split('\n') if bank.strip()]
    total = 0
    for bank in banks:
        prev_v, prev_i = largest_at_range(bank, 0, len(bank) - (num - 1))
        res = str(prev_v)
        for i in range(num - 2, -1, -1):
            next_v, next_i = largest_at_range(bank, prev_i + 1, len(bank) - i)
            prev_v, prev_i = next_v, next_i
            res += str(next_v)
        total += int(res)
    return total


def largest_at_range(bank, range_start, range_end) -> tuple[int, int]:
    maxv = 0
    maxi = 0
    for i in range(range_start, range_end):
        val = int(bank[i])
        if val > maxv:
            maxv = val
            maxi = i
    return maxv, maxi


if __name__ == "__main__":
    test_input = """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    """
    act_input = read_file()

    test(part1(test_input), 357)
    test(part1(act_input), 17383)

    test(part2(test_input), 3121910778619)
    test(part2(act_input), 172601598658203)

    print("All tests passed.")
