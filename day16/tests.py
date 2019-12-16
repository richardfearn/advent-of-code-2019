#! /usr/bin/python3

import unittest
from day16.flawed_frequency_transmission import FFT
import utils


class Part1Tests(unittest.TestCase):

    def test_example_1(self):

        fft = FFT()

        signal = "12345678"

        signal = fft.calculate(signal)
        self.assertEqual("48226158", signal)

        signal = fft.calculate(signal)
        self.assertEqual("34040438", signal)

        signal = fft.calculate(signal)
        self.assertEqual("03415518", signal)

        signal = fft.calculate(signal)
        self.assertEqual("01029498", signal)

    def test_larger_example_1(self):
        fft = FFT()
        signal = "80871224585914546619083218645595"
        for i in range(100):
            signal = fft.calculate(signal)
        self.assertEqual("24176176", signal[:8])

    def test_larger_example_2(self):
        fft = FFT()
        signal = "19617804207202209144916044189917"
        for i in range(100):
            signal = fft.calculate(signal)
        self.assertEqual("73745418", signal[:8])

    def test_larger_example_3(self):
        fft = FFT()
        signal = "69317163492948606335995924319873"
        for i in range(100):
            signal = fft.calculate(signal)
        self.assertEqual("52432133", signal[:8])

    def test_with_input(self):
        signal = read_input()
        fft = FFT()
        for i in range(100):
            signal = fft.calculate(signal)
        self.assertEqual("61149209", signal[:8])


def read_input():
    lines = utils.read_input()
    return lines[0]


if __name__ == '__main__':
    unittest.main()
