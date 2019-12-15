#! /usr/bin/python3

import collections
import math

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

                if len(output_values) == 1:
                    break

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

        return output_values


(NORTH, SOUTH, WEST, EAST) = range(1, 5)

OPPOSITE_DIR = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    WEST: EAST,
    EAST: WEST,
}

(WALL, EMPTY, OXYGEN_SYSTEM) = range(0, 3)

Point = collections.namedtuple("Point", ("x", "y"))

START_POS = Point(0, 0)


def new_pos(position, direction):
    if direction == NORTH:
        return Point(position.x, position.y - 1)
    elif direction == SOUTH:
        return Point(position.x, position.y + 1)
    elif direction == WEST:
        return Point(position.x - 1, position.y)
    elif direction == EAST:
        return Point(position.x + 1, position.y)


class RepairDroid:

    def __init__(self, program):
        self.program = program
        self.grid = None
        self.oxygen_system_pos = None

    def explore(self):

        current_pos = START_POS
        self.grid = {current_pos: EMPTY}
        path = []
        to_explore = [(new_pos(current_pos, d), current_pos, d) for d in (NORTH, SOUTH, WEST, EAST)]

        while len(to_explore) > 0:

            next_exploration = to_explore.pop(0)
            (next_pos, start_pos, direction) = next_exploration

            # Backtrack to start position, if necessary
            while current_pos != start_pos:
                undo = path.pop(-1)
                undo_dir = OPPOSITE_DIR[undo[0]]
                self.program.run([undo_dir])
                current_pos = new_pos(current_pos, undo_dir)

            # Attempt to move in the specified direction
            output = self.program.run([direction])[0]
            self.grid[next_pos] = output

            if output != WALL:
                current_pos = next_pos
                path.append((direction, next_pos))

            if output == OXYGEN_SYSTEM:
                self.oxygen_system_pos = current_pos

            elif output == EMPTY:

                for direction in (NORTH, SOUTH, WEST, EAST):
                    next_pos = new_pos(current_pos, direction)
                    if next_pos not in self.grid:
                        to_explore.insert(0, (next_pos, current_pos, direction))

    def grid_as_text(self):

        min_x = min(p.x for p in self.grid.keys())
        max_x = max(p.x for p in self.grid.keys())
        min_y = min(p.y for p in self.grid.keys())
        max_y = max(p.y for p in self.grid.keys())

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        grid = [row[:] for row in [["?"] * width] * height]

        for (pos, what) in self.grid.items():

            char = "?"

            if what == WALL:
                char = "█"

            elif what == OXYGEN_SYSTEM:
                char = "O"

            elif what == EMPTY:
                char = " "

            if pos == START_POS:
                char = "S"

            grid[pos.y - min_y][pos.x - min_x] = str(char)

        grid = ["".join(row) for row in grid]
        grid = "\n".join(grid)
        return grid

    def min_moves_to_oxygen_system(self):
        distances = self.shortest_path(START_POS)
        return distances[self.oxygen_system_pos]

    def time_to_fill_with_oxygen(self):
        distances = self.shortest_path(self.oxygen_system_pos)
        times = [t for t in distances.values() if t is not math.inf]
        return max(times)

    def shortest_path(self, initial):

        unvisited = set(self.grid.keys())

        distances = {}
        for p in unvisited:
            distances[p] = math.inf
        distances[initial] = 0

        current_node = initial

        while current_node:

            for direction in (NORTH, SOUTH, WEST, EAST):

                neighbour = new_pos(current_node, direction)

                if (neighbour in self.grid) and (self.grid[neighbour] != WALL) and (neighbour in unvisited):

                    tentative_distance = distances[current_node] + 1

                    if tentative_distance < distances[neighbour]:
                        distances[neighbour] = tentative_distance

            unvisited.remove(current_node)

            (min_dist_node, min_dist) = (None, None)
            for u in unvisited:
                if (min_dist_node is None) or (distances[u] < min_dist):
                    (min_dist_node, min_dist) = (u, distances[u])
            current_node = min_dist_node

        return distances
