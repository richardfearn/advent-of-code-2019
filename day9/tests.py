#! /usr/bin/python3

import unittest
from day9 import part1
import utils


PART1_EXAMPLE1 = """
109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99
"""

PART1_EXAMPLE2 = """
1102,34915192,34915192,7,4,7,99,0
"""

PART1_EXAMPLE3 = """
104,1125899906842624,99
"""


class Part1Tests(unittest.TestCase):

    def test_example_relative_base(self):
        program = part1.Program(read_program("109,19,99"))
        program.relative_base = 2000
        program.run()
        self.assertEqual(2019, program.relative_base)

    def test_example1(self):
        memory = read_program(PART1_EXAMPLE1)
        program = part1.Program(memory)
        outputs = program.run()
        self.assertEqual(memory, outputs)

    def test_example2(self):
        program = part1.Program(read_program(PART1_EXAMPLE2))
        outputs = program.run()
        self.assertEqual(16, len(str(outputs[0])))

    def test_example3(self):
        memory = read_program(PART1_EXAMPLE3)
        program = part1.Program(memory)
        outputs = program.run()
        self.assertEqual(memory[1], outputs[0])

    def test_with_input(self):
        program = part1.Program(read_input())
        outputs = program.run([1])
        self.assertEqual([2399197539], outputs)


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        program = part1.Program(read_input())
        outputs = program.run([2])
        self.assertEqual([35106], outputs)


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
