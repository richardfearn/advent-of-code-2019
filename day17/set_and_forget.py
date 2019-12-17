#! /usr/bin/python3

from enum import Enum
import collections

ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
RELATIVE_BASE_OFFSET = 9
HALT = 99

POSITION_PARAMETER_MODE = 0
IMMEDIATE_PARAMETER_MODE = 1
RELATIVE_PARAMETER_MODE = 2


class Instruction:

    def __init__(self, opcode):
        self.opcode = (opcode % 100)
        self.parameter_modes = self.determine_modes(opcode)

    @staticmethod
    def determine_modes(opcode):
        modes = ("0000" + str(opcode))[-5:-2]
        modes = modes[::-1]  # reverse
        modes = [int(i) for i in modes]
        modes = dict(zip((1, 2, 3), modes))
        return modes


class Program:

    def __init__(self, program, input_values=None):
        self.memory = 10000 * [0]
        self.memory[:len(program)] = program
        self.input_values = input_values.copy() if input_values is not None else []
        self.pc = 0
        self.relative_base = 0

    def run(self, input_values=None):

        if input_values is not None:
            self.input_values.extend(input_values)

        output_values = []

        while True:

            instruction = Instruction(self.memory[self.pc])

            if instruction.opcode in (ADD, MULTIPLY):

                param1, param2, param3 = self.memory[self.pc + 1:self.pc + 4]

                if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                    param1 = self.memory[param1]
                elif instruction.parameter_modes[1] == RELATIVE_PARAMETER_MODE:
                    param1 = self.memory[self.relative_base + param1]

                if instruction.parameter_modes[2] == POSITION_PARAMETER_MODE:
                    param2 = self.memory[param2]
                elif instruction.parameter_modes[2] == RELATIVE_PARAMETER_MODE:
                    param2 = self.memory[self.relative_base + param2]

                if instruction.opcode == ADD:
                    output = param1 + param2
                else:
                    output = param1 * param2

                if instruction.parameter_modes[3] == POSITION_PARAMETER_MODE:
                    self.memory[param3] = output
                elif instruction.parameter_modes[3] == RELATIVE_PARAMETER_MODE:
                    self.memory[self.relative_base + param3] = output

                self.pc += 4

            elif instruction.opcode == INPUT:

                if len(self.input_values) == 0:
                    return "need_input"

                param = self.memory[self.pc + 1]

                input_value = self.input_values.pop(0)

                if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                    self.memory[param] = input_value
                elif instruction.parameter_modes[1] == RELATIVE_PARAMETER_MODE:
                    self.memory[self.relative_base + param] = input_value

                self.pc += 2

            elif instruction.opcode == OUTPUT:

                param1 = self.memory[self.pc + 1]

                if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                    param1 = self.memory[param1]
                elif instruction.parameter_modes[1] == RELATIVE_PARAMETER_MODE:
                    param1 = self.memory[self.relative_base + param1]

                output_values.append(param1)

                self.pc += 2

                return "output", param1

            elif instruction.opcode in (JUMP_IF_TRUE, JUMP_IF_FALSE):

                param1, param2 = self.memory[self.pc + 1:self.pc + 3]

                if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                    param1 = self.memory[param1]
                elif instruction.parameter_modes[1] == RELATIVE_PARAMETER_MODE:
                    param1 = self.memory[self.relative_base + param1]

                if instruction.parameter_modes[2] == POSITION_PARAMETER_MODE:
                    param2 = self.memory[param2]
                elif instruction.parameter_modes[2] == RELATIVE_PARAMETER_MODE:
                    param2 = self.memory[self.relative_base + param2]

                if (instruction.opcode == JUMP_IF_TRUE) and (param1 != 0):
                    self.pc = param2
                elif (instruction.opcode == JUMP_IF_FALSE) and (param1 == 0):
                    self.pc = param2
                else:
                    self.pc += 3

            elif instruction.opcode in (LESS_THAN, EQUALS):

                param1, param2, param3 = self.memory[self.pc + 1:self.pc + 4]

                if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                    param1 = self.memory[param1]
                elif instruction.parameter_modes[1] == RELATIVE_PARAMETER_MODE:
                    param1 = self.memory[self.relative_base + param1]

                if instruction.parameter_modes[2] == POSITION_PARAMETER_MODE:
                    param2 = self.memory[param2]
                elif instruction.parameter_modes[2] == RELATIVE_PARAMETER_MODE:
                    param2 = self.memory[self.relative_base + param2]

                if instruction.opcode == LESS_THAN:
                    output = 1 if param1 < param2 else 0
                else:  # EQUALS
                    output = 1 if param1 == param2 else 0

                if instruction.parameter_modes[3] == POSITION_PARAMETER_MODE:
                    self.memory[param3] = output
                elif instruction.parameter_modes[3] == RELATIVE_PARAMETER_MODE:
                    self.memory[self.relative_base + param3] = output

                self.pc += 4

            elif instruction.opcode == RELATIVE_BASE_OFFSET:

                param = self.memory[self.pc + 1]

                if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                    param = self.memory[param]
                elif instruction.parameter_modes[1] == RELATIVE_PARAMETER_MODE:
                    param = self.memory[self.relative_base + param]

                self.relative_base += param

                self.pc += 2

            elif instruction.opcode == HALT:
                return "halt"

            else:
                raise Exception("Unknown opcode %d" % instruction.opcode)


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
