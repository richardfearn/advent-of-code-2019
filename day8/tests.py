#! /usr/bin/python3

import unittest
from day8 import part1, part2
import utils

PART1_EXAMPLE1 = "123456789012"

PART2_EXAMPLE1 = "2201"

PART2_EXAMPLE2 = "0222112222120000"


class Part1Tests(unittest.TestCase):

    def test_example1(self):
        image = part1.Image(PART1_EXAMPLE1, width=3, height=2)
        self.assertEqual([1, 2, 3, 4, 5, 6], image.layers[0])
        self.assertEqual([7, 8, 9, 0, 1, 2], image.layers[1])

    def test_with_input(self):
        image = part1.Image(read_input(), width=25, height=6)
        min_layer_num = image.layer_with_fewest_0_digits()
        layer = image.layers[min_layer_num]
        result = layer.count(1) * layer.count(2)
        self.assertEqual(1224, result)


class Part2Tests(unittest.TestCase):

    def test_example1(self):
        image = part2.Image(PART2_EXAMPLE1, width=1, height=1)
        rendered = image.render()
        self.assertEqual([0], rendered)

    def test_example2(self):
        image = part2.Image(PART2_EXAMPLE2, width=2, height=2)
        self.assertEqual([0, 2, 2, 2], image.layers[0])
        self.assertEqual([1, 1, 2, 2], image.layers[1])
        self.assertEqual([2, 2, 1, 2], image.layers[2])
        self.assertEqual([0, 0, 0, 0], image.layers[3])
        rendered = image.render()
        self.assertEqual([0, 1, 1, 0], rendered)

    def test_with_input(self):
        image = part2.Image(read_input(), width=25, height=6)
        print(image.render_as_string())


def read_input():
    lines = utils.read_input()
    return lines[0]


if __name__ == '__main__':
    unittest.main()
