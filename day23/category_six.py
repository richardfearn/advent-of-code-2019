from intcode import Program
import collections

Packet = collections.namedtuple("Packet", ["address", "x", "y"])


class Network:

    def __init__(self, instructions):
        self.computers = [Computer(i, Program(instructions)) for i in range(50)]

    def get_first_packet_sent_to_address_255(self):
        while True:
            for c in self.computers:
                sent = c.run()
                for p in sent:
                    if p.address == 255:
                        return p
                    else:
                        self.computers[p.address].deliver(p)


class NetworkWithNAT:

    def __init__(self, instructions):
        self.computers = [Computer(i, Program(instructions)) for i in range(50)]
        self.nat = NAT(self)

    def get_first_y_value_delivered_twice(self):

        y_values_sent_by_nat = set()

        while True:

            for c in self.computers:
                sent = c.run()
                for p in sent:
                    if p.address == 255:
                        self.nat.deliver(p)
                    else:
                        self.computers[p.address].deliver(p)

            packet_sent_by_nat = self.nat.monitor()
            if packet_sent_by_nat is not None:
                if packet_sent_by_nat.y in y_values_sent_by_nat:
                    return packet_sent_by_nat.y
                else:
                    y_values_sent_by_nat.add(packet_sent_by_nat.y)


class Computer:

    def __init__(self, address, program):

        self.address = address
        self.program = program
        self.received = []

        # Set network address
        self.program.run([address])

    def run(self):

        sent = []

        while True:

            if len(self.received) == 0:
                packet = [-1]

            else:
                packet = self.received.pop(0)
                packet = [packet.x, packet.y]

            output = self.program.run(packet)

            if output == "need_input":
                break

            elif output[0] == "output":
                sent.append(output[1])

        return [Packet(*vals) for vals in chunks(sent, 3)]

    def deliver(self, packet):
        self.received.append(packet)


class NAT:

    def __init__(self, network):
        self.network = network
        self.received = None

    def deliver(self, packet):
        self.received = packet

    def monitor(self):
        total_packets = sum(len(c.received) for c in self.network.computers)
        if total_packets == 0:
            self.network.computers[0].deliver(self.received)
            return self.received
        else:
            return None


def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
