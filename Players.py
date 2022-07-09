import Card

class Player:
    def __init__(self, money):
        self.hand = None
        self.money = money
        self.bet = 0

    def return_cards(self):
        tmp = self.hand
        self.hand = None
        return tmp

    def get_cards(self, cards):
        self.hand = Hand(cards)

    def place_bet(self):
        self.bet = self.money/6
        self.money -= self.bet
        return self.bet

    def get_bet(self):
        return self.bet

    def win(self, amount):
        self.money += amount

class Hand:
    def __init__(self, cards):
        self.hand = cards

class Dealer(Player):
    def __init__(self):
        self.deck = Card.Deck()

    def deal(self):
        return self.deck.deal()

