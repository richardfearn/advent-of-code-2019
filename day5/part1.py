#! /usr/bin/python3

ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
HALT = 99

POSITION_PARAMETER_MODE = 0
IMMEDIATE_PARAMETER_MODE = 1


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


def run_program(memory, input_value):

    pc = 0
    output_values = []

    while True:

        instruction = Instruction(memory[pc])

        if instruction.opcode in (ADD, MULTIPLY):

            param1, param2, param3 = memory[pc + 1:pc + 4]

            if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                param1 = memory[param1]

            if instruction.parameter_modes[2] == POSITION_PARAMETER_MODE:
                param2 = memory[param2]

            if instruction.opcode == ADD:
                output = param1 + param2
            else:
                output = param1 * param2

            memory[param3] = output

            pc += 4

        elif instruction.opcode == INPUT:
            param = memory[pc + 1]
            memory[param] = input_value
            pc += 2

        elif instruction.opcode == OUTPUT:

            param1 = memory[pc + 1]

            if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                param1 = memory[param1]

            output_values.append(param1)

            pc += 2

        elif instruction.opcode == HALT:
            break

        else:
            raise Exception("Unknown opcode %d" % instruction.opcode)

    return memory, output_values
