#! /usr/bin/python3

import unittest
from day1 import part1, part2


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(part1.fuel_required(12), 2)

    def test_example_2(self):
        self.assertEqual(part1.fuel_required(14), 2)

    def test_example_3(self):
        self.assertEqual(part1.fuel_required(1969), 654)

    def test_example_4(self):
        self.assertEqual(part1.fuel_required(100756), 33583)


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(part2.fuel_required(14), 2)

    def test_example_2(self):
        self.assertEqual(part2.fuel_required(1969), 966)

    def test_example_3(self):
        self.assertEqual(part2.fuel_required(100756), 50346)


if __name__ == '__main__':
    unittest.main()
