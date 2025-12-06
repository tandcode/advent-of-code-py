import re

from adventofcode.util.utils import *


def part1(inp) -> int:
    ids, ranges = parse(inp)
    return len([id for id in ids if any(in_range(id, range) for range in ranges)])


def parse(inp) -> tuple[list[int], list[tuple[int, ...]]]:
    ranges, ids = re.split(r"\s*\n\s*\n\s*", inp.strip())
    ranges = [tuple(int(r) for r in a_range.strip().split("-")) for a_range in ranges.split('\n') if a_range.strip()]
    ids = [int(id.strip()) for id in ids.split('\n') if id.strip()]
    return ids, ranges


def in_range(id, range) -> bool:
    start, end = range
    return start <= id <= end


def part2(inp) -> int:
    ids, ranges = parse(inp)
    merged = []
    for start, end in sorted(ranges):
        if merged and merged[-1][1] >= start:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return sum(end - start + 1 for start, end in merged)


if __name__ == "__main__":
    test_input = """
    3-5
    10-14
    16-20
    12-18
    
    1
    5
    8
    11
    17
    32
    """

    act_input = read_file()

    test(part1(test_input), 3)
    test(part1(act_input), 529)

    test(part2(test_input), 14)
    test(part2(act_input), 344260049617193)

    print("All tests passed.")
