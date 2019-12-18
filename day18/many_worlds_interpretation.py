#! /usr/bin/python3

import collections

PointTuple = collections.namedtuple("Point", ("x", "y"))


class Point(PointTuple):

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


UP = Point(0, -1)
RIGHT = Point(1, 0)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)

ENTRANCE_CHAR = "@"
OPEN_PASSAGE_CHAR = "."
STONE_WALL_CHAR = "#"


class Map:

    def __init__(self, lines):

        if isinstance(lines, list):
            self.grid = lines
        else:
            self.grid = lines.strip().split("\n")

        print(self.grid)

        self.width = len(self.grid[0])
        self.height = len(self.grid)
        print("size: %d × %d" % (self.width, self.height))

        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] == ENTRANCE_CHAR:
                    self.entrance_pos = Point(x, y)
                    break
        print("entrance_pos", self.entrance_pos)

    def run(self):
        current_pos = self.entrance_pos
        to_visit = [(current_pos, [])]
        paths = {}
        visited = []
        keys = []
        while len(to_visit) > 0:
            (this_pos, path_so_far) = to_visit.pop(0)
            visited.append(this_pos)

            what = self.grid[this_pos.y][this_pos.x]

            if str.islower(what):
                paths[this_pos] = path_so_far
                keys.append((this_pos, what))

            elif what in (OPEN_PASSAGE_CHAR, ENTRANCE_CHAR):
                paths[this_pos] = path_so_far
                next_nodes = []
                for direction in (UP, RIGHT, DOWN, LEFT):
                    next_pos = this_pos + direction
                    if next_pos not in visited:
                        next_nodes.append((next_pos, path_so_far + [next_pos]))
                to_visit = next_nodes + to_visit

        for k in keys:
            print(k, len(paths[k[0]]))

    def in_grid(self, p):
        return (0 <= p.x < self.width) and (0 <= p.y < self.height)
