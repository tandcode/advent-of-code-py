from adventofcode.util.utils import *
from adventofcode.util.grid import *


def towel_can_be_accessed(c) -> bool:
    return c.v == '@' and len(c.neighbors('@')) < 4


def part1(inp) -> int:
    return sum(1 for c in Grid(inp) if c.v == '@' and len(c.neighbors('@')) < 4)


def part2(inp) -> int:
    def helper(grid, total):
        to_remove = [c.pos for c in grid if towel_can_be_accessed(c)]
        if not to_remove:
            return total
        for pos in to_remove:
            grid[pos] = '.'
        return helper(grid, total + len(to_remove))

    return helper(Grid(inp), 0)


if __name__ == "__main__":
    test_input = """
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.
    """
    act_input = read_file()

    test(part1(test_input), 13)
    test(part1(act_input), 1393)

    test(part2(test_input), 43)
    test(part2(act_input), 8643)

    print("All tests passed.")
