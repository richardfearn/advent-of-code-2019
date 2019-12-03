#! /usr/bin/python3

import sys


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Point(self.x + vector.x, self.y + vector.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return "Point[%d, %d]" % (self.x, self.y)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, step_size):
        return Vector(self.x * step_size, self.y * step_size)

    def __repr__(self):
        return "Vector[%d, %d]" % (self.x, self.y)


ORIGIN = Point(0, 0)


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        if (self.is_horizontal() and self.p1.x > self.p2.x) or (self.is_vertical() and self.p1.y > self.p2.y):
            (self.p1, self.p2) = (self.p2, self.p1)

    def is_horizontal(self):
        return self.p1.y == self.p2.y

    def is_vertical(self):
        return self.p1.x == self.p2.x

    def intersections(self, other_lines):

        if self.is_horizontal():
            other_lines = [line for line in other_lines if line.is_vertical()]

        elif self.is_vertical():
            other_lines = [line for line in other_lines if line.is_horizontal()]

        intersections = [self.intersection(other) for other in other_lines]
        intersections = [i for i in intersections if i]
        intersections = [i for i in intersections if i != ORIGIN]

        return set(intersections)

    def intersection(self, other):

        if self.is_horizontal() and other.is_vertical():
            if (other.p1.y <= self.p1.y <= other.p2.y) and (self.p1.x <= other.p1.x <= self.p2.x):
                return Point(other.p1.x, self.p1.y)

        if self.is_vertical() and other.is_horizontal():
            if (other.p1.x <= self.p1.x <= other.p2.x) and (self.p1.y <= other.p1.y <= self.p2.y):
                return Point(self.p1.x, other.p1.y)

        return None

    def __repr__(self):
        return "Line[%s, %s]" % (self.p1, self.p2)


DIRECTION_VECTORS = {
    "U": Vector(0, 1),
    "D": Vector(0, -1),
    "L": Vector(-1, 0),
    "R": Vector(1, 0),
}


def calc_min_distance(wires):

    lines1 = make_lines(calc_points(wires[0]))
    lines2 = make_lines(calc_points(wires[1]))

    intersections = set()
    for line1 in lines1:
        intersections.update(line1.intersections(lines2))

    distances = [p.manhattan_distance() for p in intersections]
    return min(distances)


def calc_points(path):

    steps = path.split(",")

    current_pos = Point(0, 0)
    points = [current_pos]

    for step in steps:
        direction = step[0]
        step_size = int(step[1:])
        step_vector = DIRECTION_VECTORS[direction] * step_size
        new_pos = current_pos + step_vector
        points.append(new_pos)
        current_pos = new_pos

    return points


def make_lines(points):
    return [Line(points[i], points[i+1]) for i in range(0, len(points) - 1)]


def main():

    wires = sys.stdin.readlines()
    wires = [w.rstrip() for w in wires]

    min_distance = calc_min_distance(wires)
    print(min_distance)


if __name__ == "__main__":
    main()
