#! /usr/bin/python3

import math
from operator import itemgetter


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
                elif column == 'X':
                    self.station = Point(x, y)

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

    def set_station(self):

        (location, max_visible) = self.find_best_location()

        self.station = location
        self.asteroids.remove(location)

        return location, max_visible

    def calc_vaporization_rotations(self):
        lines = self.determine_lines()
        rotations = self.determine_rotations(lines)
        return rotations

    def determine_lines(self):

        lines = {}

        for asteroid in self.asteroids:

            offset = asteroid - self.station
            angle = self.convert_offset_to_angle(offset)
            distance = math.sqrt(offset.x * offset.x + offset.y * offset.y)
            asteroid_and_distance = (asteroid, distance)

            if angle not in lines:
                lines[angle] = []
            lines[angle].append(asteroid_and_distance)

        for angle in lines.keys():
            lines[angle] = sorted(lines[angle], key=itemgetter(1))
            lines[angle] = [v[0] for v in lines[angle]]

        return lines

    @staticmethod
    def determine_rotations(lines):

        rotations = []

        while lines:
            rotations.append([])
            for angle in sorted(lines.keys()):
                asteroid = lines[angle].pop(0)
                rotations[-1].append(asteroid)
                if not lines[angle]:
                    del lines[angle]

        return rotations

    @staticmethod
    def convert_offset_to_angle(offset):

        angle = 90 + math.degrees(math.atan2(offset.y, offset.x))

        while angle < 0:
            angle += 360

        while angle > 360:
            angle -= 360

        return angle
