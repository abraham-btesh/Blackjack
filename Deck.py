import Suite
import random


class Deck:
    suites = ["clubs", "hearts", "diamonds", "spades"]

    def __init__(self):
        self.deck = [Suite.Suite(val, s) for val in range(2, 14) for s in self.suites]

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
