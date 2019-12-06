#! /usr/bin/python3

import unittest
from day6 import part1, part2
import utils


PART1_EXAMPLE1 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

PART2_EXAMPLE1 = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""


class Part1Tests(unittest.TestCase):

    def test_example1(self):
        tree = part1.Tree(split_text_into_lines(PART1_EXAMPLE1))
        self.assertEqual(3, tree.depth("D"))
        self.assertEqual(7, tree.depth("L"))
        self.assertEqual(0, tree.depth("COM"))
        self.assertEqual(42, tree.number_of_orbits())

    def test_with_input(self):
        tree = part1.Tree(utils.read_input())
        self.assertEqual(0, tree.depth("COM"))
        self.assertEqual(241064, tree.number_of_orbits())


class Part2Tests(unittest.TestCase):

    def test_example1(self):
        tree = part2.Tree(split_text_into_lines(PART2_EXAMPLE1))
        self.assertEqual(4, tree.calc_min_orbital_transfers())

    def test_with_input(self):
        tree = part2.Tree(utils.read_input())
        self.assertEqual(418, tree.calc_min_orbital_transfers())


def split_text_into_lines(text):
    return text.strip().split("\n")


if __name__ == '__main__':
    unittest.main()
