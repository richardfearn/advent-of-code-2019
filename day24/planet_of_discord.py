BUG = '#'
EMPTY_SPACE = '.'


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
