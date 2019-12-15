#! /usr/bin/python3

import unittest
from day15.oxygen_system import Program, RepairDroid
import utils


class Part1Tests(unittest.TestCase):

    def test_with_input(self):
        program = Program(read_input())
        droid = RepairDroid(program)
        droid.explore()
        print(droid.grid_as_text())
        self.assertEqual(204, droid.min_moves_to_oxygen_system())


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        program = Program(read_input())
        droid = RepairDroid(program)
        droid.explore()
        self.assertEqual(340, droid.time_to_fill_with_oxygen())


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
