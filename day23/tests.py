#! /usr/bin/python3

import unittest
from day23.category_six import Network, NetworkWithNAT
import utils


class Part1Tests(unittest.TestCase):

    def test_with_input(self):
        instructions = read_input()
        network = Network(instructions)
        self.assertEqual(22151, network.get_first_packet_sent_to_address_255().y)


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        instructions = read_input()
        network = NetworkWithNAT(instructions)
        self.assertEqual(17001, network.get_first_y_value_delivered_twice())


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
