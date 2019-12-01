#! /usr/bin/python3

import sys

def fuel_required(mass):
    total_fuel = 0
    while mass > 0:
        fuel = (mass // 3) - 2
        if fuel > 0:
            total_fuel += fuel
        mass = fuel
    return total_fuel

masses = sys.stdin.readlines()
masses = list(map(int, masses))

fuel = list(map(fuel_required, masses))
for f in fuel:
    print(f)

print("Total: %d" % sum(fuel))
