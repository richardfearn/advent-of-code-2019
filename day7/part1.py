#! /usr/bin/python3

ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
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


def run_program(program, input_values):

    memory = program.copy()
    pc = 0
    input_pos = 0
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
            memory[param] = input_values[input_pos]
            input_pos += 1
            pc += 2

        elif instruction.opcode == OUTPUT:

            param1 = memory[pc + 1]

            if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                param1 = memory[param1]

            output_values.append(param1)

            pc += 2

        elif instruction.opcode in (JUMP_IF_TRUE, JUMP_IF_FALSE):

            param1, param2 = memory[pc + 1:pc + 3]

            if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                param1 = memory[param1]

            if instruction.parameter_modes[2] == POSITION_PARAMETER_MODE:
                param2 = memory[param2]

            if (instruction.opcode == JUMP_IF_TRUE) and (param1 != 0):
                pc = param2
            elif (instruction.opcode == JUMP_IF_FALSE) and (param1 == 0):
                pc = param2
            else:
                pc += 3

        elif instruction.opcode in (LESS_THAN, EQUALS):

            param1, param2, param3 = memory[pc + 1:pc + 4]

            if instruction.parameter_modes[1] == POSITION_PARAMETER_MODE:
                param1 = memory[param1]

            if instruction.parameter_modes[2] == POSITION_PARAMETER_MODE:
                param2 = memory[param2]

            if instruction.opcode == LESS_THAN:
                output = 1 if param1 < param2 else 0
            else:  # EQUALS
                output = 1 if param1 == param2 else 0

            memory[param3] = output

            pc += 4

        elif instruction.opcode == HALT:
            break

        else:
            raise Exception("Unknown opcode %d" % instruction.opcode)

    return memory, output_values


def run_sequence(phase_settings, program):
    current_signal = 0
    for amp in range(0, 5):
        inputs = [phase_settings[amp], current_signal]
        (_, outputs) = run_program(program, inputs)
        current_signal = outputs[0]
    return current_signal
