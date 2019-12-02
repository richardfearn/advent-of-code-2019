#! /usr/bin/python3

import sys


def fuel_required(mass):
    return (mass // 3) - 2


def main():

    masses = sys.stdin.readlines()
    masses = list(map(int, masses))

    fuel = list(map(fuel_required, masses))

    print(sum(fuel))


if __name__ == "__main__":
    main()
