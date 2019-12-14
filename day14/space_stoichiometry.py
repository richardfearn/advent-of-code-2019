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

    def calc_min_ore_required(self):

        chemicals = {FUEL: 1}

        reaction_for_chem = {}
        for r in self.reactions:
            reaction_for_chem[r.output.name] = r

        while True:

            need_converting = [c for c in set(chemicals.keys()) if c != ORE and chemicals[c] > 0]

            if len(need_converting) == 0:
                break

            chem_to_convert = list(need_converting)[0]
            reaction_to_reverse = reaction_for_chem[chem_to_convert]
            chemicals = reaction_to_reverse.reverse(chemicals)

        return chemicals[ORE]
