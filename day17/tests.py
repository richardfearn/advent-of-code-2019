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

PART_2_EXAMPLE_1 = """
#######...#####
#.....#...#...#
#.....#...#...#
......#...#...#
......#...###.#
......#.....#.#
^########...#.#
......#.#...#.#
......#########
........#...#..
....#########..
....#...#......
....#...#......
....#...#......
....#####......
"""

PART_2_EXAMPLE_1_PATH = """R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2"""

PART_2_INPUT_PATH = "L,12,L,12,L,6,L,6,R,8,R,4,L,12,L,12,L,12,L,6,L,6,L,12,L,6,R,12,R,8,R,8,R,4,L,12,L,12,L,12,L,6," + \
    "L,6,L,12,L,6,R,12,R,8,R,8,R,4,L,12,L,12,L,12,L,6,L,6,L,12,L,6,R,12,R,8"


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


class Part2Tests(unittest.TestCase):

    def test_example(self):
        view = View(PART_2_EXAMPLE_1)
        print(view.text)
        view.end_pos = (0, 2)
        self.assertEqual(PART_2_EXAMPLE_1_PATH, view.path_to_other_end())

    def test_with_input(self):
        program = Program(read_input())
        cameras = Cameras(program)
        view = cameras.get_view()
        print(view.text)
        view.end_pos = (32, 42)
        self.assertEqual(PART_2_INPUT_PATH, view.path_to_other_end())


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
