#! /usr/bin/python3

import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "%d,%d" % (self.x, self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)


class Map:

    def __init__(self, lines):

        self.width = len(lines[0])
        self.height = len(lines)
        self.grid = [list(row) for row in lines]
        self.asteroids = []

        for (y, row) in enumerate(lines):
            for (x, column) in enumerate(row):
                if column == '#':
                    asteroid = Point(x, y)
                    self.asteroids.append(asteroid)

    def determine_visible(self):
        visible = [row[:] for row in [[None] * self.width] * self.height]
        for asteroid in self.asteroids:
            angles = set()
            for other in self.asteroids:
                if other != asteroid:
                    offset = other - asteroid
                    angle = math.degrees(math.atan2(offset.y, offset.x))
                    angles.add(angle)
            visible[asteroid.y][asteroid.x] = len(angles)
        return visible

    def find_best_location(self):

        visible = self.determine_visible()

        (location, max_visible) = (None, None)

        for x in range(0, self.width):
            for y in range(0, self.height):
                if visible[y][x] is not None:
                    if (max_visible is None) or (visible[y][x] > max_visible):
                        (location, max_visible) = (Point(x, y), visible[y][x])

        return location, max_visible
