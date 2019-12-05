#! /usr/bin/python3

import unittest
from day5 import part1, part2
import utils


class Part1Tests(unittest.TestCase):

    def test_opcode_parsing(self):
        self.assertEqual(part1.Instruction(2).parameter_modes, {1: 0, 2: 0, 3: 0})
        self.assertEqual(part1.Instruction(99).parameter_modes, {1: 0, 2: 0, 3: 0})
        self.assertEqual(part1.Instruction(102).parameter_modes, {1: 1, 2: 0, 3: 0})
        self.assertEqual(part1.Instruction(1002).parameter_modes, {1: 0, 2: 1, 3: 0})
        self.assertEqual(part1.Instruction(10002).parameter_modes, {1: 0, 2: 0, 3: 1})

    def test_example1(self):
        program = read_program("3,0,4,0,99")
        (memory, output_values) = part1.run_program(program, 123)
        self.assertEqual([123], output_values)
        self.assertEqual([123, 0, 4, 0, 99], memory)

    def test_example2(self):
        program = read_program("1002,4,3,4,33")
        (memory, output_values) = part1.run_program(program, None)
        self.assertEqual([], output_values)
        self.assertEqual([1002, 4, 3, 4, 99], memory)

    def test_with_input(self):
        program = read_input()
        (memory, output_values) = part1.run_program(program, 1)
        self.assertEqual(output_values[-1], 9006673)


class Part2Tests(unittest.TestCase):

    def test_example_position_mode_equal_to_8(self):

        program = read_program("3,9,8,9,10,9,4,9,99,-1,8")

        (memory, output_values) = part2.run_program(program, 8)
        self.assertEqual([1], output_values)

        (memory, output_values) = part2.run_program(program, 0)
        self.assertEqual([0], output_values)

    def test_example_position_mode_less_than_8(self):

        program = read_program("3,9,7,9,10,9,4,9,99,-1,8")

        (memory, output_values) = part2.run_program(program, 7)
        self.assertEqual([1], output_values)

        (memory, output_values) = part2.run_program(program, 8)
        self.assertEqual([0], output_values)

    def test_example_immediate_mode_equal_to_8(self):

        program = read_program("3,3,1108,-1,8,3,4,3,99")

        (memory, output_values) = part2.run_program(program, 8)
        self.assertEqual([1], output_values)

        (memory, output_values) = part2.run_program(program, 0)
        self.assertEqual([0], output_values)

    def test_example_immediate_mode_less_than_8(self):

        program = read_program("3,3,1107,-1,8,3,4,3,99")

        (memory, output_values) = part2.run_program(program, 7)
        self.assertEqual([1], output_values)

        (memory, output_values) = part2.run_program(program, 8)
        self.assertEqual([0], output_values)

    def test_example_jump_position_mode(self):

        program = read_program("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")

        (memory, output_values) = part2.run_program(program, 0)
        self.assertEqual([0], output_values)

        (memory, output_values) = part2.run_program(program, 1)
        self.assertEqual([1], output_values)

    def test_example_jump_immediate_mode(self):

        program = read_program("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")

        (memory, output_values) = part2.run_program(program, 0)
        self.assertEqual([0], output_values)

        (memory, output_values) = part2.run_program(program, 1)
        self.assertEqual([1], output_values)

    def test_example_larger(self):

        program = read_program("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31," +
                               "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104," +
                               "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")

        (memory, output_values) = part2.run_program(program, 7)
        self.assertEqual([999], output_values)

        (memory, output_values) = part2.run_program(program, 8)
        self.assertEqual([1000], output_values)

        (memory, output_values) = part2.run_program(program, 9)
        self.assertEqual([1001], output_values)

    def test_with_input(self):
        program = read_input()
        (memory, output_values) = part2.run_program(program, 5)
        self.assertEqual([3629692], output_values)


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
