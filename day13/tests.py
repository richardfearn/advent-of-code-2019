#! /usr/bin/python3

import unittest
from day13.care_package import Program, ArcadeCabinet
import utils


class Part1Tests(unittest.TestCase):

    def test_with_input(self):
        program = Program(read_input())
        cabinet = ArcadeCabinet(program)
        cabinet.run()
        print(cabinet.grid_as_text())
        self.assertEqual(216, cabinet.number_of_block_tiles())


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        program = Program(read_input())
        program.memory[0] = 2
        cabinet = ArcadeCabinet(program)
        cabinet.play()
        print(cabinet.grid_as_text())
        self.assertEqual(10025, cabinet.score)


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
