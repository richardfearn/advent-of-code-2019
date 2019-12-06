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

    def path_to_root(self, node):
        path = [node]
        while node != "COM":
            node = self.links[node]
            path.append(node)
        return path

    def calc_min_orbital_transfers(self):

        you_path = self.path_to_root("YOU")
        san_path = self.path_to_root("SAN")

        lowest_common_ancestor = None
        for n in you_path:
            if n in san_path:
                lowest_common_ancestor = n
                break

        you_to_common = you_path.index(lowest_common_ancestor) - 1
        san_to_common = san_path.index(lowest_common_ancestor) - 1

        return you_to_common + san_to_common
