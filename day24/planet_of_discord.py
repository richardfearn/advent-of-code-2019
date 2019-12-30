BUG = '#'
EMPTY_SPACE = '.'
UP_OR_DOWN = '?'


class Grid:

    def __init__(self, grid):
        self.grid = grid if isinstance(grid, list) else grid.split("\n")

    def step(self):

        new_grid = []

        for y in range(5):

            new_grid.append([])

            for x in range(5):

                old_state = self.grid[y][x]
                adjacent_bugs = 0

                if (x > 0) and (self.grid[y][x-1] == BUG):
                    adjacent_bugs += 1

                if (x < 4) and (self.grid[y][x+1] == BUG):
                    adjacent_bugs += 1

                if (y > 0) and (self.grid[y-1][x] == BUG):
                    adjacent_bugs += 1

                if (y < 4) and (self.grid[y+1][x] == BUG):
                    adjacent_bugs += 1

                if (old_state == BUG) and (adjacent_bugs != 1):
                    new_state = EMPTY_SPACE

                elif (old_state == EMPTY_SPACE) and (adjacent_bugs in (1, 2)):
                    new_state = BUG

                else:
                    new_state = old_state

                new_grid[-1].append(new_state)

            new_grid[-1] = "".join(new_grid[-1])

        self.grid = new_grid

    def run_until_layout_repeats(self):

        states = set()
        states.add(self.as_text())

        while True:
            self.step()
            if self.as_text() in states:
                break
            else:
                states.add(self.as_text())

    def biodiversity_rating(self):
        layout_rating = 0
        for y in range(5):
            for x in range(5):
                if self.grid[y][x] == BUG:
                    tile_score = 1 << (y * 5 + x)
                    layout_rating += tile_score
        return layout_rating

    def as_text(self):
        return "\n".join(self.grid)


EMPTY = """
.....
.....
..?..
.....
.....
"""


class RecursiveGrid:

    def __init__(self, grid, levels_up_and_down):
        levels = [EMPTY] * levels_up_and_down + [grid] + [EMPTY] * levels_up_and_down
        self.levels = [RecursiveGridLevel(level) for level in levels]
        self.levels_up_and_down = levels_up_and_down
        self.connect_levels()

    def connect_levels(self):
        for i in range(len(self.levels)):
            if i > 0:
                self.levels[i].up = self.levels[i - 1]
            if i < (len(self.levels) - 1):
                self.levels[i].down = self.levels[i + 1]

    def step(self):
        self.levels = [level.step() for level in self.levels]
        self.connect_levels()

    def total_bugs(self):
        return sum(level.total_bugs() for level in self.levels)

    def as_text(self):
        texts = ["Depth %d:\n%s" % ((i - self.levels_up_and_down), self.levels[i].as_text())
                 for i in range(len(self.levels))]
        return "\n\n".join(texts)


class RecursiveGridLevel:

    def __init__(self, grid):
        self.grid = grid.strip().split("\n")
        self.up = None
        self.down = None

    def step(self):

        new_grid = []

        for y in range(5):

            new_row = []

            for x in range(5):

                if (x == 2) and (y == 2):
                    new_state = UP_OR_DOWN

                else:

                    old_state = self.grid[y][x]
                    adjacent_bugs = 0

                    # Left

                    if x == 0:
                        if self.up and self.up.grid[2][1] == BUG:
                            adjacent_bugs += 1

                    elif (x == 3) and (y == 2):
                        if self.down:
                            for dy in range(5):
                                if self.down.grid[dy][4] == BUG:
                                    adjacent_bugs += 1

                    elif self.grid[y][x-1] == BUG:
                        adjacent_bugs += 1

                    # Right

                    if x == 4:
                        if self.up and self.up.grid[2][3] == BUG:
                            adjacent_bugs += 1

                    elif (x == 1) and (y == 2):
                        if self.down:
                            for dy in range(5):
                                if self.down.grid[dy][0] == BUG:
                                    adjacent_bugs += 1

                    elif self.grid[y][x+1] == BUG:
                        adjacent_bugs += 1

                    # Up

                    if y == 0:
                        if self.up and self.up.grid[1][2] == BUG:
                            adjacent_bugs += 1

                    elif (x == 2) and (y == 3):
                        if self.down:
                            for dx in range(5):
                                if self.down.grid[4][dx] == BUG:
                                    adjacent_bugs += 1

                    elif self.grid[y-1][x] == BUG:
                        adjacent_bugs += 1

                    # Down

                    if y == 4:
                        if self.up and self.up.grid[3][2] == BUG:
                            adjacent_bugs += 1

                    elif (x == 2) and (y == 1):
                        if self.down:
                            for dx in range(5):
                                if self.down.grid[0][dx] == BUG:
                                    adjacent_bugs += 1

                    elif self.grid[y+1][x] == BUG:
                        adjacent_bugs += 1

                    # Determine new state

                    if (old_state == BUG) and (adjacent_bugs != 1):
                        new_state = EMPTY_SPACE

                    elif (old_state == EMPTY_SPACE) and (adjacent_bugs in (1, 2)):
                        new_state = BUG

                    else:
                        new_state = old_state

                new_row.append(new_state)

            new_grid.append("".join(new_row))

        return RecursiveGridLevel("\n".join(new_grid))

    def total_bugs(self):
        return sum(row.count(BUG) for row in self.grid)

    def as_text(self):
        return "\n".join(self.grid)
