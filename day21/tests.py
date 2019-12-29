#! /usr/bin/python3

import unittest
from intcode import Program
from day21.springdroid_adventure import *
import utils


class Part1Tests(unittest.TestCase):

    def test_with_input(self):

        program = Program(read_input())
        programmer = SpringdroidProgrammer(program)

        self.assertEqual("Input instructions:", programmer.get_line())

        programmer.send_line("NOT A J")
        programmer.send_line("NOT B T")
        programmer.send_line("OR T J")
        programmer.send_line("NOT C T")
        programmer.send_line("OR T J")
        programmer.send_line("AND D J")
        programmer.send_line("WALK")

        hull_damage = programmer.get_line()

        self.assertEqual(19360288, hull_damage)


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
