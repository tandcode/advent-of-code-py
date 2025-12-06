from functools import reduce
from operator import add
from operator import mul
from itertools import groupby
from typing import Callable

from adventofcode.util.grid import *
from adventofcode.util.utils import *


def part1(inp) -> int:
    return sum([reduce(operation(c[-1]), list(map(int, c[:-1]))) for c in Grid(inp, ignore_spaces=True).cols()])


def operation(c: str) -> Callable[[int, int], int]:
    return mul if c == '*' else add


def part2(inp) -> int:
    grid = Grid(inp, strip_lines=False)
    cols = [[cell for cell in col if cell.strip()] for col in grid.cols()]
    groups = [list(group) for k, group in groupby(cols, key=lambda x: x == []) if not k]
    def group_value(g):
        nums = [g[0][:-1]] + [n for n in g[1:]]
        return reduce(operation(g[0][-1]), (int(''.join(n)) for n in nums))
    return sum(group_value(g) for g in groups)


if __name__ == "__main__":
    test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    act_input = read_file()

    test(part1(test_input), 4277556)
    test(part1(act_input), 4693159084994)

    test(part2(test_input), 3263827)
    test(part2(act_input), 11643736116335)

    print("All tests passed.")
