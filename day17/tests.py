#! /usr/bin/python3

import unittest
from day17.set_and_forget import Program, Cameras, View
import utils

PART_1_EXAMPLE_1 = """
..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        view = View(PART_1_EXAMPLE_1)
        print(view.text)
        intersections = view.find_intersections()
        alignment_parameters = [p[0] * p[1] for p in intersections]
        self.assertEqual(76, sum(alignment_parameters))

    def test_with_input(self):
        program = Program(read_input())
        cameras = Cameras(program)
        view = cameras.get_view()
        print(view.text)
        intersections = view.find_intersections()
        alignment_parameters = [p[0] * p[1] for p in intersections]
        self.assertEqual(4800, sum(alignment_parameters))


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
