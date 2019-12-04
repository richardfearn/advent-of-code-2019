#! /usr/bin/python3


def is_valid_password(number):

    if not is_six_digit_number(number):
        return False

    digits = list(map(int, str(number)))

    if not two_adjacent_digits_the_same(digits):
        return False

    if not digits_never_decrease(digits):
        return False

    return True


def is_six_digit_number(number):
    return 100000 <= number <= 999999


def two_adjacent_digits_the_same(digits):
    (a, b, c, d, e, f) = digits
    return (a == b) or (b == c) or (c == d) or (d == e) or (e == f)


def digits_never_decrease(digits):
    (a, b, c, d, e, f) = digits
    return (a <= b) and (b <= c) and (c <= d) and (d <= e) and (e <= f)
