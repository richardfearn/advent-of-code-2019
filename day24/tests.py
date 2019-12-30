#! /usr/bin/python3

import unittest
from day24.planet_of_discord import *
import utils

PART_1_EXAMPLE = """
Initial state:
....#
#..#.
#..##
..#..
#....

After 1 minute:
#..#.
####.
###.#
##.##
.##..

After 2 minutes:
#####
....#
....#
...#.
#.###

After 3 minutes:
#....
####.
...##
#.##.
.##.#

After 4 minutes:
####.
....#
##..#
.....
##...
"""

PART_1_EXAMPLE_REPEATED_STATE = """
.....
.....
.....
#....
.#...
"""

PART_2_EXAMPLE_INITIAL_STATE = """
....#
#..#.
#.?##
..#..
#....
"""

PART_2_EXAMPLE_AFTER_10_MINS = """
Depth -5:
..#..
.#.#.
..?.#
.#.#.
..#..

Depth -4:
...#.
...##
..?..
...##
...#.

Depth -3:
#.#..
.#...
..?..
.#...
#.#..

Depth -2:
.#.##
....#
..?.#
...##
.###.

Depth -1:
#..##
...##
..?..
...#.
.####

Depth 0:
.#...
.#.##
.#?..
.....
.....

Depth 1:
.##..
#..##
..?.#
##.##
#####

Depth 2:
###..
##.#.
#.?..
.#.##
#.#..

Depth 3:
..###
.....
#.?..
#....
#...#

Depth 4:
.###.
#..#.
#.?..
##.#.
.....

Depth 5:
####.
#..#.
#.?#.
####.
.....
"""


class Part1Tests(unittest.TestCase):

    def test_with_example_first_few_minutes(self):
        example_states = read_example(PART_1_EXAMPLE)
        grid = Grid(example_states[0])
        self.assertEqual(example_states[0], grid.as_text())
        for i in range(1, 5):
            grid.step()
            self.assertEqual(example_states[i], grid.as_text())

    def test_with_example_run_until_layout_repeated(self):
        example_states = read_example(PART_1_EXAMPLE)
        grid = Grid(example_states[0])
        grid.run_until_layout_repeats()
        self.assertEqual(PART_1_EXAMPLE_REPEATED_STATE.strip(), grid.as_text())

    def test_biodiversity_rating(self):
        grid = Grid(PART_1_EXAMPLE_REPEATED_STATE.strip())
        self.assertEqual(2129920, grid.biodiversity_rating())

    def test_with_input(self):
        grid = Grid(utils.read_input())
        grid.run_until_layout_repeats()
        self.assertEqual(28778811, grid.biodiversity_rating())


class Part2Tests(unittest.TestCase):

    def test_with_example(self):
        grid = RecursiveGrid(PART_2_EXAMPLE_INITIAL_STATE, 5)
        for i in range(10):
            grid.step()
        self.assertEqual(PART_2_EXAMPLE_AFTER_10_MINS.strip(), grid.as_text())
        self.assertEqual(99, grid.total_bugs())

    def test_with_input(self):
        grid = RecursiveGrid("\n".join(utils.read_input()), 150)
        for i in range(200):
            grid.step()
        self.assertEqual(2097, grid.total_bugs())


def read_example(text):
    lines = text.strip().split("\n")
    states = utils.chunks(lines, 7)
    states = ["\n".join(s[1:6]) for s in states]
    return states


if __name__ == '__main__':
    unittest.main()
