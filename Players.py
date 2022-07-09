import Hand

class Player:

    def __init__(self, money=100):
        self.hand = None
        self.money = money
        self.bet = 0

    def return_cards(self):
        tmp = self.hand
        self.hand = None
        return tmp

    def get_cards(self, cards):
        self.hand = Hand.Hand(cards)

    def place_bet(self):
        self.bet = self.money/6
        self.money -= self.bet
        return self.bet

    def get_bet(self):
        return self.bet

    def win(self, amount):
        self.money += amount
