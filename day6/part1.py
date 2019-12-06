#! /usr/bin/python3


class Tree:

    def __init__(self, lines):

        self.links = {}
        self.nodes = set()

        for line in lines:
            (parent, child) = line.split(")")
            self.links[child] = parent
            self.nodes.add(child)
            self.nodes.add(parent)

    def depth(self, node):
        d = 0
        while node != "COM":
            d += 1
            node = self.links[node]
        return d

    def number_of_orbits(self):
        return sum([self.depth(n) for n in self.nodes])
