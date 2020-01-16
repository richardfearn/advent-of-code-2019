#! /usr/bin/python3


class FFT:

    def __init__(self, signal):
        self.pattern = [0, 1, 0, -1]
        self.values = [int(i) for i in signal]
        self.patterns = [self.digit_pattern(out_digit) for out_digit in range(len(self.values))]

    def digit_pattern(self, out_digit):
        return [self.pattern[self.pattern_index(in_digit, out_digit)] for in_digit in range(len(self.values))]

    def pattern_index(self, in_digit, out_digit):
        return ((in_digit + 1) // (out_digit + 1)) % len(self.pattern)

    def calculate(self):
        self.values = [self.new_digit(self.values, i) for i in range(len(self.values))]

    def new_digit(self, inputs, out_digit):
        pattern = self.patterns[out_digit]
        parts = [inputs[in_digit] * pattern[in_digit] for in_digit in range(len(inputs))]
        digit = abs(sum(parts)) % 10
        return digit

    def as_string(self):
        return "".join([str(v) for v in self.values])
