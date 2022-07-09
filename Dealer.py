import Players
import Card


class Dealer(Players.Player):

    def __init__(self):
        self.deck = Card.Deck()

    def deal(self):
        return self.deck.deal()
