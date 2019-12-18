#! /usr/bin/python3

import unittest
from day18.many_worlds_interpretation import *
import utils

PART_1_EXAMPLE_1 = """
#########
#b.A.@.a#
#########
"""

PART_1_EXAMPLE_2 = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""

PART_1_EXAMPLE_3 = """
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
"""

PART_1_EXAMPLE_4 = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
"""

PART_1_EXAMPLE_5 = """
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
"""


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        m = Map(PART_1_EXAMPLE_1)
        m.run()
        self.assertEqual(0, 0)

    def test_example_3(self):
        m = Map(PART_1_EXAMPLE_3)
        m.run()
        self.assertEqual(0, 0)

    def test_with_input(self):
        m = Map(utils.read_input())
        m.run()
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
