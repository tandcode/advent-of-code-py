import re


class Grid:

    def __init__(self, inp, ignore_spaces=False, strip_lines=True):
        self.ignore_spaces = ignore_spaces
        self.strip_lines = strip_lines
        self.grid = [self.parse_line(line) for line in inp.split('\n') if line.strip()]

    def parse_line(self, line: str) -> list:
        line_formated = line.strip() if self.strip_lines else line
        if self.ignore_spaces:
            return re.split(r'\s+', line_formated)
        return list(line_formated)

    def contains(self, *args) -> bool:
        match args:
            case [(x, y)]: pass
            case (x, y): pass
            case _: raise ValueError("contains expects either (x, y) or a tuple (x, y)")
        return 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid)

    def __getitem__(self, pos):
        if isinstance(pos, tuple) and len(pos) == 2:
            x, y = pos
        else:
            raise ValueError("Indexing expects a tuple (x, y)")
        # Handle valid index ranges
        if self.contains(pos):
            return self.grid[y][x]
        else:
            raise IndexError("Position out of range")

    def cols(self) -> list[list]:
        return [[self.grid[y][x] for y in range(len(self.grid))] for x in range(len(self.grid[0]))]

    def __setitem__(self, pos, value):
        if isinstance(pos, tuple) and len(pos) == 2:
            x, y = pos
        else:
            raise ValueError("Indexing expects a tuple (x, y)")
        # Handle valid index ranges
        if self.contains(pos):
            self.grid[y][x] = value
        else:
            raise IndexError("Position out of range")

    class Cell:
        def __init__(self, grid, v, x, y):
            self.grid = grid
            self.v = v
            self.x = x
            self.y = y
            self.pos = (x, y)

        def __repr__(self):
            return f"Cell('{self.v}' at ({self.x}, {self.y}))"

        def neighbors(self, *args):
            match args:
                case (v,) if isinstance(v, str):
                    filter_v = v
                case ():
                    filter_v = None
                case _:
                    raise ValueError("neighbours expects either filter string or no arguments")
            indexes = [
                (self.x - 1, self.y - 1),
                (self.x, self.y - 1),
                (self.x + 1, self.y - 1),
                (self.x + 1, self.y),
                (self.x + 1, self.y + 1),
                (self.x, self.y + 1),
                (self.x - 1, self.y + 1),
                (self.x - 1, self.y)
            ]
            raw_neighbours = [ind for ind in indexes if self.grid.contains(ind)]
            filtered_neighbours = [ind for ind in raw_neighbours if not filter_v or self.grid[ind] == filter_v]
            return filtered_neighbours

    def __iter__(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                yield Grid.Cell(self, self.grid[y][x], x, y)