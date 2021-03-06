#! /usr/bin/python3

import unittest
from day16.flawed_frequency_transmission import FFT, part2
import utils


class Part1Tests(unittest.TestCase):

    def test_example_1(self):

        signal = "12345678"
        fft = FFT(signal)

        fft.calculate()
        self.assertEqual("48226158", fft.as_string())

        fft.calculate()
        self.assertEqual("34040438", fft.as_string())

        fft.calculate()
        self.assertEqual("03415518", fft.as_string())

        fft.calculate()
        self.assertEqual("01029498", fft.as_string())

    def test_larger_example_1(self):
        signal = "80871224585914546619083218645595"
        fft = FFT(signal)
        for i in range(100):
            fft.calculate()
        self.assertEqual("24176176", fft.as_string()[:8])

    def test_larger_example_2(self):
        signal = "19617804207202209144916044189917"
        fft = FFT(signal)
        for i in range(100):
            fft.calculate()
        self.assertEqual("73745418", fft.as_string()[:8])

    def test_larger_example_3(self):
        signal = "69317163492948606335995924319873"
        fft = FFT(signal)
        for i in range(100):
            fft.calculate()
        self.assertEqual("52432133", fft.as_string()[:8])

    def test_with_input(self):
        signal = read_input()
        fft = FFT(signal)
        for i in range(100):
            fft.calculate()
        self.assertEqual("61149209", fft.as_string()[:8])


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        (signal, message) = ("03036732577212944063491565474664" * 10000, "84462026")
        self.assertEqual(message, part2(signal))

    def test_example_2(self):
        (signal, message) = ("02935109699940807407585447034323" * 10000, "78725270")
        self.assertEqual(message, part2(signal))

    def test_example_3(self):
        (signal, message) = ("03081770884921959731165446850517" * 10000, "53553731")
        self.assertEqual(message, part2(signal))

    def test_with_input(self):
        signal = read_input() * 10000
        self.assertEqual("16178430", part2(signal))


def read_input():
    lines = utils.read_input()
    return lines[0]


if __name__ == '__main__':
    unittest.main()
