#! /usr/bin/python3

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

                if len(output_values) == 3:
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


EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

CHARS = [" ", "█", "▒", "―", "●"]

NEUTRAL = 0
TILT_LEFT = -1
TILT_RIGHT = 1


class ArcadeCabinet:

    def __init__(self, program):
        self.program = program
        self.tiles = {}
        self.score = 0
        self.ball_pos = None
        self.paddle_pos = None

    def run(self):

        while True:

            outputs = self.program.run()

            if outputs == "halt":
                break

            (x, y, tile_id) = outputs
            self.update_tiles(x, y, tile_id)

    def update_tiles(self, x, y, tile_id):

        pos = (x, y)
        self.tiles[pos] = tile_id

        if tile_id == BALL:
            self.ball_pos = pos

        elif tile_id == PADDLE:
            self.paddle_pos = pos

    def play(self):

        inputs = []

        while True:

            outputs = self.program.run(inputs)
            inputs = []

            if outputs == "halt":
                break

            elif outputs == "need_input":

                if self.ball_pos[0] < self.paddle_pos[0]:
                    joystick_position = TILT_LEFT
                elif self.ball_pos[0] > self.paddle_pos[0]:
                    joystick_position = TILT_RIGHT
                else:
                    joystick_position = NEUTRAL

                inputs = [joystick_position]

            else:

                (x, y, value) = outputs

                if (x, y) == (-1, 0):
                    self.score = value

                else:
                    self.update_tiles(x, y, value)

    def number_of_block_tiles(self):
        return list(self.tiles.values()).count(BLOCK)

    def grid_as_text(self):
        grid = [[self.tiles[(x, y)] for x in range(35)] for y in range(21)]
        grid = [[CHARS[grid[y][x]] for x in range(35)] for y in range(21)]
        grid = ["".join(row) for row in grid]
        grid = "\n".join(grid)
        return grid
