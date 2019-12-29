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
