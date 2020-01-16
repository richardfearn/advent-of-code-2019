#! /usr/bin/python3

ORE = "ORE"
FUEL = "FUEL"


class Chemical:

    def __init__(self, amount, name):
        self.amount = amount
        self.name = name

    def __repr__(self):
        return "%d %s" % (self.amount, self.name)

    @staticmethod
    def from_string(s):
        (amount, name) = s.split(" ")
        return Chemical(int(amount), name)


class Reaction:

    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output

    @staticmethod
    def from_line(line):
        (inputs, output) = line.split(" => ")
        inputs = [Chemical.from_string(s) for s in inputs.split(", ")]
        output = Chemical.from_string(output)
        return Reaction(inputs, output)

    def __repr__(self):
        return "%s => %s" % (", ".join([repr(i) for i in self.inputs]), repr(self.output))

    def reverse(self, stock):

        new_stock = stock.copy()

        new_stock[self.output.name] -= self.output.amount
        if new_stock[self.output.name] == 0:
            del new_stock[self.output.name]

        for i in self.inputs:
            if i.name not in new_stock:
                new_stock[i.name] = 0
            new_stock[i.name] += i.amount

        return new_stock


class Nanofactory:

    def __init__(self, lines):
        self.reactions = [Reaction.from_line(line) for line in lines]
        self.reaction_order = self.topological_sort()

    def topological_sort(self):

        nodes = set()
        for r in self.reactions:
            nodes.update([i.name for i in r.inputs])
            nodes.add(r.output.name)

        incoming = {}
        outgoing = {}
        for n in nodes:
            incoming[n] = set()
            outgoing[n] = set()

        for r in self.reactions:
            for i in r.inputs:
                incoming[r.output.name].add(i.name)
                outgoing[i.name].add(r.output.name)

        sorted_elements = []
        no_incoming = {ORE}

        while len(no_incoming) > 0:
            n = no_incoming.pop()
            sorted_elements.append(n)
            while len(outgoing[n]) > 0:
                m = outgoing[n].pop()
                incoming[m].remove(n)
                if len(incoming[m]) == 0:
                    no_incoming.add(m)

        if sum(len(e) for e in outgoing.values()) > 0:
            raise Exception("Graph has cycle")

        sorted_elements.remove(ORE)
        return sorted_elements

    def calc_min_ore_required(self):

        chemicals = {FUEL: 1}

        reaction_for_chem = {}
        for r in self.reactions:
            reaction_for_chem[r.output.name] = r

        for i in reversed(self.reaction_order):
            reaction = reaction_for_chem[i]
            while (i in chemicals) and (chemicals[i] > 0):
                chemicals = reaction.reverse(chemicals)

        return chemicals[ORE]
