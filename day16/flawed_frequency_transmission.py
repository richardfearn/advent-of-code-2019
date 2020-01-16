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


def part2(signal):

    """
    The important thing for solving part 2 efficiently is that, for any digit in the 2nd half of the message, the
    pattern to use is some number of 0s followed by some number of 1s.

    The last digit of the output signal is the last digit of the input signal; the 2nd to last digit of the output
    signal is the sum of the last 2 digits (mod 10); and so on.

    We can calculate each digit in the output message by working backwards, starting with the last digit, and keeping
    a running total of the digits so far.

    The offsets in the part 2 examples, and in my input, all place the 8-digit message in the 2nd half of the signal.
    """

    offset = int(signal[0:7])

    if offset < len(signal) / 2:
        raise Exception("Message is not in the 2nd half of the signal")

    signal = [int(c) for c in signal]

    for phase in range(100):
        total = 0
        for i in range(len(signal)-1, offset-1, -1):
            total += signal[i]
            signal[i] = (total % 10)

    message = signal[offset:offset+8]
    message = "".join([str(n) for n in message])
    return message
