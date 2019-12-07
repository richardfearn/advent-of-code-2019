#! /usr/bin/python3

import unittest
from day7 import part1, part2
import utils
import itertools


PART1_EXAMPLE1 = """
3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
"""

PART1_EXAMPLE2 = """
3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0
"""

PART1_EXAMPLE3 = """
3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
"""

PART2_EXAMPLE1 = """
3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
"""

PART2_EXAMPLE2 = """
3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
"""


class Part1Tests(unittest.TestCase):

    def test_example1(self):
        phase_settings = [4, 3, 2, 1, 0]
        program = read_program(PART1_EXAMPLE1)
        signal = part1.run_sequence(phase_settings, program)
        self.assertEqual(43210, signal)

    def test_example2(self):
        phase_settings = [0, 1, 2, 3, 4]
        program = read_program(PART1_EXAMPLE2)
        signal = part1.run_sequence(phase_settings, program)
        self.assertEqual(54321, signal)

    def test_example3(self):
        phase_settings = [1, 0, 4, 3, 2]
        program = read_program(PART1_EXAMPLE3)
        signal = part1.run_sequence(phase_settings, program)
        self.assertEqual(65210, signal)

    def test_with_input(self):
        program = read_input()
        max_signal = None
        for phase_settings in itertools.permutations([0, 1, 2, 3, 4]):
            signal = part1.run_sequence(phase_settings, program)
            if (max_signal is None) or (signal > max_signal):
                max_signal = signal
        self.assertEqual(46248, max_signal)


class Part2Tests(unittest.TestCase):

    def test_example1(self):
        phase_settings = [9, 8, 7, 6, 5]
        program = read_program(PART2_EXAMPLE1)
        signal = part2.run_sequence(phase_settings, program)
        self.assertEqual(139629729, signal)

    def test_example2(self):
        phase_settings = [9, 7, 8, 5, 6]
        program = read_program(PART2_EXAMPLE2)
        signal = part2.run_sequence(phase_settings, program)
        self.assertEqual(18216, signal)

    def test_with_input(self):
        program = read_input()
        max_signal = None
        for phase_settings in itertools.permutations([5, 6, 7, 8, 9]):
            signal = part2.run_sequence(phase_settings, program)
            if (max_signal is None) or (signal > max_signal):
                max_signal = signal
        self.assertEqual(54163586, max_signal)


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
