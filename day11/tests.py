#! /usr/bin/python3

import unittest
from day11 import part1
import utils


class Part1Tests(unittest.TestCase):

    def test_example(self):

        program = FakeProgram()

        robot = part1.Robot(program)
        self.assertEqual(part1.Point(0, 0), robot.current_pos)
        self.assertEqual(part1.UP, robot.direction)

        program.outputs = [1, 0]
        robot.step()
        self.assertEqual(part1.Point(-1, 0), robot.current_pos)
        self.assertEqual(part1.LEFT, robot.direction)
        self.assertEqual({part1.Point(0, 0): part1.WHITE}, robot.colours)
        self.assertEqual({part1.Point(0, 0)}, robot.painted)

        program.outputs = [0, 0]
        robot.step()
        self.assertEqual(part1.Point(-1, 1), robot.current_pos)
        self.assertEqual(part1.DOWN, robot.direction)
        self.assertEqual({part1.Point(0, 0): part1.WHITE, part1.Point(-1, 0): part1.BLACK}, robot.colours)
        self.assertEqual({part1.Point(0, 0), part1.Point(-1, 0)}, robot.painted)

        program.outputs = [1, 0]
        robot.step()
        robot.step()
        self.assertEqual(part1.Point(0, 0), robot.current_pos)
        self.assertEqual(part1.UP, robot.direction)
        self.assertEqual({part1.Point(0, 0): part1.WHITE, part1.Point(-1, 0): part1.BLACK,
                          part1.Point(-1, 1): part1.WHITE, part1.Point(0, 1): part1.WHITE}, robot.colours)
        self.assertEqual({part1.Point(0, 0), part1.Point(-1, 0), part1.Point(-1, 1), part1.Point(0, 1)}, robot.painted)

        program.outputs = [0, 1]
        robot.step()
        program.outputs = [1, 0]
        robot.step()
        program.outputs = [1, 0]
        robot.step()
        self.assertEqual(part1.Point(0, -1), robot.current_pos)
        self.assertEqual(part1.LEFT, robot.direction)
        self.assertEqual({part1.Point(-1, 0): part1.BLACK, part1.Point(-1, 1): part1.WHITE,
                          part1.Point(0, 1): part1.WHITE, part1.Point(0, 0): part1.BLACK,
                          part1.Point(1, 0): part1.WHITE, part1.Point(1, -1): part1.WHITE}, robot.colours)
        self.assertEqual({part1.Point(-1, 0), part1.Point(-1, 1), part1.Point(0, 1), part1.Point(0, 0),
                          part1.Point(1, 0), part1.Point(1, -1)}, robot.painted)

        self.assertEqual(6, len(robot.painted))

    def test_with_input(self):
        program = part1.Program(read_input())
        robot = part1.Robot(program)
        robot.run()
        self.assertEqual(1934, len(robot.painted))


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        program = part1.Program(read_input())
        robot = part1.Robot(program)
        robot.colours[part1.Point(0, 0)] = part1.WHITE
        robot.run()
        print(robot.registration_identifier())


class FakeProgram:

    def __init__(self):
        self.outputs = []

    def run(self, *_):
        return self.outputs


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
