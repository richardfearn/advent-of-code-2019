#! /usr/bin/python3


class FFT:

    def __init__(self):
        self.pattern = [0, 1, 0, -1]

    def calculate(self, inputs):
        inputs = [int(i) for i in inputs]
        outputs = [self.new_digit(inputs, i) for i in range(len(inputs))]
        return "".join([str(o) for o in outputs])

    def new_digit(self, inputs, out_digit):
        pattern = [self.pattern[self.pattern_index(in_digit, out_digit)] for in_digit in range(len(inputs))]
        parts = [inputs[in_digit] * pattern[in_digit] for in_digit in range(len(inputs))]
        digit = abs(sum(parts)) % 10
        return digit

    def pattern_index(self, in_digit, out_digit):
        return ((in_digit + 1) // (out_digit + 1)) % len(self.pattern)
