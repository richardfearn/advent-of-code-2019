class Deck:

    def __init__(self, num_cards):
        self.cards = list(range(num_cards))

    def deal_into_new_stack(self):
        self.cards = list(reversed(self.cards))

    def cut(self, n):
        self.cards = self.cards[n:] + self.cards[:n]

    def deal(self, n):
        after_deal = [-1] * len(self.cards)
        pos = 0
        for i in range(0, len(self.cards)):
            after_deal[pos] = self.cards[i]
            pos = (pos + n) % len(self.cards)
        self.cards = after_deal

    def shuffle(self, techniques):
        for t in techniques:
            if t == "deal into new stack":
                self.deal_into_new_stack()
            elif t.startswith("cut"):
                n = int(t.split()[-1])
                self.cut(n)
            elif t. startswith("deal with increment"):
                n = int(t.split()[-1])
                self.deal(n)
