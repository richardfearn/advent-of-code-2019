#! /usr/bin/python3

import unittest
import utils
from day2 import part1, part2


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(part1.run_program([1,9,10,3,2,3,11,0,99,30,40,50]), [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])

    def test_example_2(self):
        self.assertEqual(part1.run_program([1,0,0,0,99]), [2,0,0,0,99])

    def test_example_3(self):
        self.assertEqual(part1.run_program([2,3,0,3,99]), [2,3,0,6,99])

    def test_example_4(self):
        self.assertEqual(part1.run_program([2,4,4,5,99,0]), [2,4,4,5,99,9801])

    def test_example_5(self):
        self.assertEqual(part1.run_program([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])

    def test_with_input(self):
        lines = utils.read_input()
        program = [int(i) for i in lines[0].split(",")]
        program[1:3] = (12, 2)
        program = part1.run_program(program)
        self.assertEqual(program[0], 3790645)


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(part2.run_program([1,9,10,3,2,3,11,0,99,30,40,50]), [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])

    def test_example_2(self):
        self.assertEqual(part2.run_program([1,0,0,0,99]), [2,0,0,0,99])

    def test_example_3(self):
        self.assertEqual(part2.run_program([2,3,0,3,99]), [2,3,0,6,99])

    def test_example_4(self):
        self.assertEqual(part2.run_program([2,4,4,5,99,0]), [2,4,4,5,99,9801])

    def test_example_5(self):
        self.assertEqual(part2.run_program([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])

    def test_with_input(self):
        lines = utils.read_input()
        program = [int(i) for i in lines[0].split(",")]
        (noun, verb) = (65, 77)
        program[1:3] = (noun, verb)
        self.assertEqual(part2.run_program(program)[0], 19690720)


if __name__ == '__main__':
    unittest.main()
