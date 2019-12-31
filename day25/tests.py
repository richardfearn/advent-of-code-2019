#! /usr/bin/python3

import unittest
from intcode import Program
from day25.cryostasis import *
import utils


class Part1Tests(unittest.TestCase):

    def test_with_input(self):
        program = Program(read_input())
        droid = Droid(program)
        password = droid.get_password()
        self.assertEqual("4206594", password)


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
