#! /usr/bin/python3

import sys

def fuel_required(mass):
    return (mass // 3) - 2

masses = sys.stdin.readlines()
masses = list(map(int, masses))

fuel = list(map(fuel_required, masses))
for f in fuel:
    print(f)

print("Total: %d" % sum(fuel))
