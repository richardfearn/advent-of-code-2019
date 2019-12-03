#! /usr/bin/python3

import unittest
import utils
from day3 import part1, part2


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(
            part1.calc_min_distance([
                "R8,U5,L5,D3",
                "U7,R6,D4,L4"]),
            6)

    def test_example_2(self):
        self.assertEqual(
            part1.calc_min_distance([
                "R75,D30,R83,U83,L12,D49,R71,U7,L72",
                "U62,R66,U55,R34,D71,R55,D58,R83"]),
            159)

    def test_example_3(self):
        self.assertEqual(
            part1.calc_min_distance([
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]),
            135)

    def test_with_input(self):
        lines = utils.read_input()
        self.assertEqual(part1.calc_min_distance(lines), 1264)


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(
            part2.calc_min_steps([
                "R8,U5,L5,D3",
                "U7,R6,D4,L4"]),
            30)

    def test_example_2(self):
        self.assertEqual(
            part2.calc_min_steps([
                "R75,D30,R83,U83,L12,D49,R71,U7,L72",
                "U62,R66,U55,R34,D71,R55,D58,R83"]),
            610)

    def test_example_3(self):
        self.assertEqual(
            part2.calc_min_steps([
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]),
            410)

    def test_with_input(self):
        lines = utils.read_input()
        self.assertEqual(part2.calc_min_steps(lines), 37390)


if __name__ == '__main__':
    unittest.main()
