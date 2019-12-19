#! /usr/bin/python3

import unittest
from day19.tractor_beam import TextDrone, ProgramDrone, Point, STATIONARY, PULLED
import utils

PART_1_EXAMPLE = """
#.........
.#........
..##......
...###....
....###...
.....####.
......####
......####
.......###
........##
"""

PART_2_EXAMPLE = """
#.......................................
.#......................................
..##....................................
...###..................................
....###.................................
.....####...............................
......#####.............................
......######............................
.......#######..........................
........########........................
.........#########......................
..........#########.....................
...........##########...................
...........############.................
............############................
.............#############..............
..............##############............
...............###############..........
................###############.........
................#################.......
.................########OOOOOOOOOO.....
..................#######OOOOOOOOOO#....
...................######OOOOOOOOOO###..
....................#####OOOOOOOOOO#####
.....................####OOOOOOOOOO#####
.....................####OOOOOOOOOO#####
......................###OOOOOOOOOO#####
.......................##OOOOOOOOOO#####
........................#OOOOOOOOOO#####
.........................OOOOOOOOOO#####
..........................##############
..........................##############
...........................#############
............................############
.............................###########
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        drone = TextDrone(PART_1_EXAMPLE)
        self.assertEqual(PULLED, drone.deploy(Point(0, 0)))
        self.assertEqual(STATIONARY, drone.deploy(Point(1, 0)))
        self.assertEqual(27, drone.find_affected_points())

    def test_with_input(self):
        program = read_input()
        drone = ProgramDrone(program, 50, 50)
        print(drone.get_map(50, 50))
        self.assertEqual(PULLED, drone.deploy(Point(0, 0)))
        self.assertEqual(PULLED, drone.deploy(Point(0, 0)))
        self.assertEqual(147, drone.find_affected_points())


class Part2Tests(unittest.TestCase):

    def test_example(self):
        drone = TextDrone(PART_2_EXAMPLE.replace("O", "#"))
        self.assertEqual(PULLED, drone.deploy(Point(0, 0)))
        self.assertEqual(STATIONARY, drone.deploy(Point(1, 0)))
        top_left = drone.find_square_top_left(10)
        self.assertEqual(250020, top_left.x * 10000 + top_left.y)

    def test_with_input(self):
        program = read_input()
        drone = ProgramDrone(program, 10000, 10000)
        top_left = drone.find_square_top_left(100)
        self.assertEqual(13280865, top_left.x * 10000 + top_left.y)


def read_program(line):
    return [int(i) for i in line.split(",")]


def read_input():
    lines = utils.read_input()
    return read_program(lines[0])


if __name__ == '__main__':
    unittest.main()
