#! /usr/bin/python3

import unittest
from day10 import part1, part2
import utils
import itertools


PART1_EXAMPLE1 = """
.#..#
.....
#####
....#
...##
"""

PART1_EXAMPLE1_VISIBLE = [
    [None, 7, None, None, 7],
    [None, None, None, None, None],
    [6, 7, 7, 7, 5],
    [None, None, None, None, 7],
    [None, None, None, 8, 7]
]

PART1_LARGER_EXAMPLE_1 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""

PART1_LARGER_EXAMPLE_2 = """
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
"""

PART1_LARGER_EXAMPLE_3 = """
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
"""

PART1_LARGER_EXAMPLE_4 = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""

PART_2_EXAMPLE_1 = """
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##
"""


class Part1Tests(unittest.TestCase):

    def test_example1(self):

        asteroid_map = part1.Map(read_map(PART1_EXAMPLE1))

        visible = asteroid_map.determine_visible()
        self.assertEqual(PART1_EXAMPLE1_VISIBLE, visible)

        (location, num_visible) = asteroid_map.find_best_location()
        self.assertEqual(part1.Point(3, 4), location)
        self.assertEqual(8, num_visible)

    def test_larger_example_1(self):
        asteroid_map = part1.Map(read_map(PART1_LARGER_EXAMPLE_1))
        (location, num_visible) = asteroid_map.find_best_location()
        self.assertEqual(part1.Point(5, 8), location)
        self.assertEqual(33, num_visible)

    def test_larger_example_2(self):
        asteroid_map = part1.Map(read_map(PART1_LARGER_EXAMPLE_2))
        (location, num_visible) = asteroid_map.find_best_location()
        self.assertEqual(part1.Point(1, 2), location)
        self.assertEqual(35, num_visible)

    def test_larger_example_3(self):
        asteroid_map = part1.Map(read_map(PART1_LARGER_EXAMPLE_3))
        (location, num_visible) = asteroid_map.find_best_location()
        self.assertEqual(part1.Point(6, 3), location)
        self.assertEqual(41, num_visible)

    def test_larger_example_4(self):
        asteroid_map = part1.Map(read_map(PART1_LARGER_EXAMPLE_4))
        (location, num_visible) = asteroid_map.find_best_location()
        self.assertEqual(part1.Point(11, 13), location)
        self.assertEqual(210, num_visible)

    def test_with_input(self):
        asteroid_map = part1.Map(utils.read_input())
        (location, num_visible) = asteroid_map.find_best_location()
        self.assertEqual(347, num_visible)


class Part2Tests(unittest.TestCase):

    def test_convert_offset_to_angle(self):
        self.assertEqual(0, part2.Map.convert_offset_to_angle(part2.Point(0, -1)))
        self.assertEqual(45, part2.Map.convert_offset_to_angle(part2.Point(1, -1)))
        self.assertEqual(90, part2.Map.convert_offset_to_angle(part2.Point(1, 0)))
        self.assertEqual(135, part2.Map.convert_offset_to_angle(part2.Point(1, 1)))
        self.assertEqual(180, part2.Map.convert_offset_to_angle(part2.Point(0, 1)))
        self.assertEqual(225, part2.Map.convert_offset_to_angle(part2.Point(-1, 1)))
        self.assertEqual(270, part2.Map.convert_offset_to_angle(part2.Point(-1, 0)))
        self.assertEqual(315, part2.Map.convert_offset_to_angle(part2.Point(-1, -1)))

    def test_example1(self):
        asteroid_map = part2.Map(read_map(PART_2_EXAMPLE_1))
        rotations = asteroid_map.calc_vaporization_rotations()
        self.assertEqual(3, len(rotations))

    def test_larger_example_from_part_1(self):

        asteroid_map = part2.Map(read_map(PART1_LARGER_EXAMPLE_4))
        asteroid_map.set_station()
        self.assertEqual(part2.Point(11, 13), asteroid_map.station)

        rotations = asteroid_map.calc_vaporization_rotations()
        order = list(itertools.chain.from_iterable(rotations))

        self.assertEqual(299, len(order))

        order = [None] + order
        self.assertEqual(part2.Point(11, 12), order[1])
        self.assertEqual(part2.Point(12, 1), order[2])
        self.assertEqual(part2.Point(12, 2), order[3])
        self.assertEqual(part2.Point(12, 8), order[10])
        self.assertEqual(part2.Point(16, 0), order[20])
        self.assertEqual(part2.Point(16, 9), order[50])
        self.assertEqual(part2.Point(10, 16), order[100])
        self.assertEqual(part2.Point(9, 6), order[199])
        self.assertEqual(part2.Point(8, 2), order[200])
        self.assertEqual(part2.Point(10, 9), order[201])
        self.assertEqual(part2.Point(11, 1), order[299])

    def test_with_input(self):

        asteroid_map = part2.Map(utils.read_input())
        asteroid_map.set_station()

        rotations = asteroid_map.calc_vaporization_rotations()
        order = list(itertools.chain.from_iterable(rotations))

        asteroid = order[199]
        self.assertEqual(829, asteroid.x * 100 + asteroid.y)


def read_map(text):
    return text.strip().split("\n")


if __name__ == '__main__':
    unittest.main()
