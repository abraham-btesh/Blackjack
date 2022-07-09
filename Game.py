import Players
import numpy

class Game:
    """
    Handles the game logic
    """
    def __init__(self, num_players):
        self.players = [Players.Player() for _ in range(num_players)]
        self.dealer = Players.Dealer()


    def play_round(self):
        """
        plays a hand of blackjack
        :return:
        """
        #play a round
        self.deal_round()
        self.place_bets()

        #calculate the players wins and losses
        self.calculate_win_loss()

        #returns cards to the deck and removes players who are out of money
        self.reset_game()
        self.remove_busted_players()

    def remove_busted_players(self):
        for player in self.players:
            if player.money == 0:
                self.players.remove(player)

    def add_player(self, player):
        self.players.append(player)

    def reset_game(self):
        self.dealer.return_cards()
        for player in self.players:
            player.return_cards()

    def calculate_win_loss(self):
        dealer_card_val = self.dealer.get_cards()
        for player in self.players:

            card1, card2 = player.get_cards()
            val = card1.get_value() + card2.get_value()

            if dealer_card_val > 21:
                player.win(player.get_bet() * 2)

            elif dealer_card_val < val or val == 21:
                player.win(player.get_bet() * 2)

    def place_bets(self):
        for player in self.players:
            player.place_bet()

    def deal_round(self):
        self.dealer.get_cards(self.dealer.deal())
        for player in self.players:
            player.get_cards(self.dealer.deal())
