from player import Player
from player import Deck
    
class Board:

    def __init__(self, players, deck):
        self.players = players
        self.deck = deck

    def deal(self, playersNumbers):
        playersNumbers = playersNumbers
        for player in self.players:
            for i in range(playersNumbers):
                player.give_card(self.draw_card())

    # in python use underscore not camelCase for methods
    def draw_card(self):
        # avoid mutating other object properties in other objects
        return self.deck.get_card()

    def restart_game(self):
        # simply rebuild the deck - it will reshuffle all cards
        self.deck.build()
        for player in self.players:
            player.return_cards()