#! /usr/bin/python3

import unittest
from day22.slam_shuffle import Deck
import utils


PART_1_EXAMPLE_1 = """
deal with increment 7
deal into new stack
deal into new stack
Result: 0 3 6 9 2 5 8 1 4 7
"""

PART_1_EXAMPLE_2 = """
cut 6
deal with increment 7
deal into new stack
Result: 3 0 7 4 1 8 5 2 9 6
"""

PART_1_EXAMPLE_3 = """
deal with increment 7
deal with increment 9
cut -2
Result: 6 3 0 7 4 1 8 5 2 9
"""

PART_1_EXAMPLE_4 = """
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
Result: 9 2 5 8 1 4 7 0 3 6
"""


class Part1Tests(unittest.TestCase):

    def test_deal_into_new_stack(self):
        deck = Deck(10)
        deck.deal_into_new_stack()
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], deck.cards)

    def test_cut(self):
        deck = Deck(10)
        deck.cut(3)
        self.assertEqual([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], deck.cards)

    def test_cut_negative(self):
        deck = Deck(10)
        deck.cut(-4)
        self.assertEqual([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], deck.cards)

    def test_deal(self):
        deck = Deck(10)
        deck.deal(3)
        self.assertEqual([0, 7, 4, 1, 8, 5, 2, 9, 6, 3], deck.cards)

    def test_example_1(self):
        deck = Deck(10)
        (techniques, result) = read_example(PART_1_EXAMPLE_1)
        deck.shuffle(techniques)
        self.assertEqual(result, deck.cards)

    def test_example_2(self):
        deck = Deck(10)
        (techniques, result) = read_example(PART_1_EXAMPLE_2)
        deck.shuffle(techniques)
        self.assertEqual(result, deck.cards)

    def test_example_3(self):
        deck = Deck(10)
        (techniques, result) = read_example(PART_1_EXAMPLE_3)
        deck.shuffle(techniques)
        self.assertEqual(result, deck.cards)

    def test_example_4(self):
        deck = Deck(10)
        (techniques, result) = read_example(PART_1_EXAMPLE_4)
        deck.shuffle(techniques)
        self.assertEqual(result, deck.cards)

    def test_with_input(self):
        deck = Deck(10007)
        techniques = utils.read_input()
        deck.shuffle(techniques)
        self.assertEqual(4684, deck.cards.index(2019))


def read_example(text):
    lines = text.strip().split("\n")
    techniques = lines[:-1]
    result = lines[-1]
    result = [int(i) for i in result[8:].split()]
    return techniques, result


if __name__ == '__main__':
    unittest.main()
