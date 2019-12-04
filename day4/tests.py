#! /usr/bin/python3

import unittest
from day4 import part1, part2


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertTrue(part1.is_valid_password(111111))

    def test_example_2(self):
        self.assertFalse(part1.is_valid_password(223450))

    def test_example_3(self):
        self.assertFalse(part1.is_valid_password(123789))

    def test_with_input(self):
        (lowest, highest) = (353096, 843212)
        valid_passwords = [i for i in range(lowest, highest+1) if part1.is_valid_password(i)]
        self.assertEqual(len(valid_passwords), 579)


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertTrue(part2.is_valid_password(112233))

    def test_example_2(self):
        self.assertFalse(part2.is_valid_password(123444))

    def test_example_3(self):
        self.assertTrue(part2.is_valid_password(111122))

    def test_with_input(self):
        (lowest, highest) = (353096, 843212)
        valid_passwords = [i for i in range(lowest, highest+1) if part2.is_valid_password(i)]
        self.assertEqual(len(valid_passwords), 358)


if __name__ == '__main__':
    unittest.main()
