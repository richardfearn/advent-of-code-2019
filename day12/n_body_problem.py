#! /usr/bin/python3

import re
import math

POS_ONLY_REGEX = "<x=\\s*(-?\\d+), y=\\s*(-?\\d+), z=\\s*(-?\\d+)>"
POS_VEL_REGEX = "pos=%s, vel=%s" % (POS_ONLY_REGEX, POS_ONLY_REGEX)


class Vector:

    def __init__(self, x, y, z):
        (self.x, self.y, self.z) = (x, y, z)

    def energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __repr__(self):
        return "<x=%d, y=%d, z=%d>" % (self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)


class Moon:

    def __init__(self, pos, vel=None):
        self.pos = pos
        self.vel = vel if vel is not None else Vector(0, 0, 0)

    @staticmethod
    def from_line(line):

        match = re.fullmatch(POS_ONLY_REGEX, line)
        if match:
            (px, py, pz) = [int(n) for n in match.groups()]
            return Moon(Vector(px, py, pz))

        match = re.fullmatch(POS_VEL_REGEX, line)
        if match:
            (px, py, pz, vx, vy, vz) = [int(n) for n in match.groups()]
            return Moon(Vector(px, py, pz), Vector(vx, vy, vz))

        raise Exception("Could not parse line")

    def energy(self):
        return self.pos.energy() * self.vel.energy()

    def __eq__(self, other):
        return (self.pos == other.pos) and (self.vel == other.vel)

    def __repr__(self):
        return "pos=%s, vel=%s" % (self.pos, self.vel)


class System:

    def __init__(self, moons):
        self.moons = moons

    def run(self):

        all_gravity = [[System.calc_gravity(a.pos, b.pos) for b in self.moons] for a in self.moons]
        all_gravity = list([sum(gravities, Vector(0, 0, 0)) for gravities in all_gravity])

        with_new_vel = [Moon(self.moons[i].pos, self.moons[i].vel + all_gravity[i]) for i in range(4)]

        with_new_pos = [Moon(m.pos + m.vel, m.vel) for m in with_new_vel]

        return System(with_new_pos)

    def total_energy(self):
        return sum([moon.energy() for moon in self.moons])

    def steps_to_return_to_same_state(self):

        getters = (
            lambda p: p.x,
            lambda p: p.y,
            lambda p: p.z,
        )

        steps_per_axis = [self.steps_to_return_to_same_state_one_axis(getter) for getter in getters]
        return lcm3(*steps_per_axis)

    def steps_to_return_to_same_state_one_axis(self, get):

        initial_values = [(get(m.pos), get(m.vel)) for m in self.moons]

        system = self
        steps_run_so_far = 0

        while True:

            system = system.run()
            steps_run_so_far += 1

            current_values = [(get(m.pos), get(m.vel)) for m in system.moons]

            if current_values == initial_values:
                break

        return steps_run_so_far

    def __eq__(self, other):
        return self.moons == other.moons

    def __repr__(self):
        return repr(self.moons)

    @staticmethod
    def calc_gravity(a, b):
        return Vector(cmp(a.x, b.x), cmp(a.y, b.y), cmp(a.z, b.z))


def cmp(a, b):
    if a > b:
        return -1
    if a < b:
        return 1
    return 0


def lcm3(a, b, c):
    return lcm(lcm(a, b), c)


def lcm(a, b):
    return a * b // math.gcd(a, b)
