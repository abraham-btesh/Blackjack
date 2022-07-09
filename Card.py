import random


class Card:
    def __init__(self, value):
        self.value = value  # < 14

    def get_value(self):
        return self.value

class Suite(Card, ):
    def __init__(self, value, suite):
        self.suite = suite
        self.available = True
        super().__init__(value)

    def is_available(self):
        return self.available

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True


class Deck:
    suites = ["clubs", "hearts", "diamonds", "spades"]

    def __init__(self):
        self.deck = [Suite(val, s) for val in range(2, 14) for s in self.suites]

    def deal(self):
        cards = random.sample(self.deck, 2)
        for card in cards:
            self.deck.remove(card)

    def return_to_deck(self, cards):
        """

        :param cards:
        :return:
        """
        for card in cards:
            self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)


