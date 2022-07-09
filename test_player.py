import pytest
import Players
import Card


money = 90
player = Players.Player(money)
deck = Card.Deck()

def test_player_construction():
    assert player.money == money

def test_place_bet():
    player.place_bet()
    assert player.money == 90 - player.get_bet()

def test_hand():
    cards = deck.deal()
    player.get_cards(cards)
    assert player.hand.hand == cards

def test_win():
    v = player.money
    player.win(70)
    assert player.money == v + 70
