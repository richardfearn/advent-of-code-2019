#! /usr/bin/python3


def is_valid_password(number):

    if not is_six_digit_number(number):
        return False

    digits = list(map(int, str(number)))

    if not digits_never_decrease(digits):
        return False

    if not two_adjacent_digits_the_same(digits):
        return False

    return True


def is_six_digit_number(number):
    return 100000 <= number <= 999999


def two_adjacent_digits_the_same(digits):

    groups = []
    for i in digits:
        if groups and groups[-1][0] == i:
            groups[-1].append(i)
        else:
            groups.append([i])

    group_lengths = [len(g) for g in groups]

    return 2 in group_lengths


def digits_never_decrease(digits):
    (a, b, c, d, e, f) = digits
    return (a <= b) and (b <= c) and (c <= d) and (d <= e) and (e <= f)
