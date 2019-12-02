#! /usr/bin/python3

import sys

ADD = 1
MULTIPLY = 2
HALT = 99


def run_program(program):

    pc = 0
    while True:

        opcode = program[pc]

        if opcode in (ADD, MULTIPLY):
            addr1, addr2, addr3 = program[pc+1:pc+4]
            inputs = program[addr1], program[addr2]
            if opcode == ADD:
                output = inputs[0] + inputs[1]
            else:
                output = inputs[0] * inputs[1]
            program[addr3] = output

        if opcode == HALT:
            break

        pc += 4

    return program


def main():

    program = sys.stdin.readline()
    program = program.rstrip()
    program = program.split(",")
    program = list(map(int, program))

    program[1] = 12
    program[2] = 2

    program = run_program(program)
    print(program[0])


if __name__ == "__main__":
    main()
