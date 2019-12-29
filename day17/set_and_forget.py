#! /usr/bin/python3

from enum import Enum
import collections

SCAFFOLD_CHAR = '#'
OPEN_SPACE_CHAR = '.'
VACUUM_ROBOT_UP_CHAR = '^'
VACUUM_ROBOT_DOWN_CHAR = 'v'
VACUUM_ROBOT_LEFT_CHAR = '<'
VACUUM_ROBOT_RIGHT_CHAR = '>'


class Tile(Enum):

    SCAFFOLD = 0
    OPEN_SPACE = 1


CHAR_TO_TYPE_MAP = {
    SCAFFOLD_CHAR: Tile.SCAFFOLD,
    OPEN_SPACE_CHAR: Tile.OPEN_SPACE,
    VACUUM_ROBOT_UP_CHAR: Tile.SCAFFOLD,
    VACUUM_ROBOT_DOWN_CHAR: Tile.SCAFFOLD,
    VACUUM_ROBOT_LEFT_CHAR: Tile.SCAFFOLD,
    VACUUM_ROBOT_RIGHT_CHAR: Tile.SCAFFOLD,
}


class Direction(Enum):

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def left(self):
        return list(Direction.__members__.values())[(self.value - 1) % 4]

    def right(self):
        return list(Direction.__members__.values())[(self.value + 1) % 4]


ROBOT_DIR_MAP = {
    VACUUM_ROBOT_UP_CHAR: Direction.UP,
    VACUUM_ROBOT_DOWN_CHAR: Direction.DOWN,
    VACUUM_ROBOT_LEFT_CHAR: Direction.LEFT,
    VACUUM_ROBOT_RIGHT_CHAR: Direction.RIGHT,
}

Point = collections.namedtuple("Point", ("x", "y"))


class Cameras:

    def __init__(self, program):
        self.program = program

    def get_view(self):

        view = []

        while True:

            output = self.program.run()

            if output == "halt":
                break

            if output[0] == "output":
                view.append(output[1])

        view = [chr(c) for c in view]
        view = "".join(view)
        return View(view)


class View:

    def __init__(self, text):

        self.text = text

        self.grid = text.strip().split("\n")
        self.grid = [list(line) for line in self.grid]

        self.width = len(self.grid[0])
        self.height = len(self.grid)

        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.grid[y][x] not in (SCAFFOLD_CHAR, OPEN_SPACE_CHAR):
                    self.robot_pos = Point(x, y)
                    self.robot_dir = ROBOT_DIR_MAP[self.grid[y][x]]

        self.grid = [[CHAR_TO_TYPE_MAP[c] for c in line] for line in self.grid]

        self.end_pos = None

    def find_intersections(self):

        intersections = []

        for y in range(1, self.height-1):
            for x in range(1, self.width-1):
                if self.is_scaffold(x, y) and self.is_scaffold(x, y-1) and self.is_scaffold(x, y+1) and \
                        self.is_scaffold(x-1, y) and self.is_scaffold(x+1, y):
                    intersections.append((x, y))

        return intersections

    def is_scaffold(self, x, y):
        return self.grid[y][x] == Tile.SCAFFOLD

    def path_to_other_end(self):

        moves = []

        while self.robot_pos != self.end_pos:

            left_dir = self.robot_dir.left()
            right_dir = self.robot_dir.right()

            left_pos = calc_next_pos(self.robot_pos, left_dir)
            right_pos = calc_next_pos(self.robot_pos, right_dir)

            if self.in_grid(left_pos) and self.grid[left_pos.y][left_pos.x] == Tile.SCAFFOLD:
                self.robot_dir = left_dir
                moves.append("L")

            elif self.in_grid(right_pos) and self.grid[right_pos.y][right_pos.x] == Tile.SCAFFOLD:
                self.robot_dir = right_dir
                moves.append("R")

            moves.append(0)

            while True:

                next_pos = calc_next_pos(self.robot_pos, self.robot_dir)
                if not self.in_grid(next_pos) or self.grid[next_pos.y][next_pos.x] != Tile.SCAFFOLD:
                    break
                moves[-1] += 1
                self.robot_pos = next_pos

        return ",".join([str(x) for x in moves])

    def in_grid(self, pos):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height


def calc_next_pos(pos, direction):
    if direction == Direction.UP:
        return Point(pos.x, pos.y - 1)
    elif direction == Direction.DOWN:
        return Point(pos.x, pos.y + 1)
    elif direction == Direction.LEFT:
        return Point(pos.x - 1, pos.y)
    elif direction == Direction.RIGHT:
        return Point(pos.x + 1, pos.y)
