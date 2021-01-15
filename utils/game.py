from player import Player
from player import Deck
    
class Board:
    """
    This help build the Board that deal, draw the cards and restart the game
    """
    def __init__(self, players, deck): # inital phase to collect the information
        self.players = players # player name 
        self.deck = deck  # deck .info 

    def deal(self, playersNumbers):
        playersNumbers = playersNumbers
        for player in self.players:
            for i in range(playersNumbers):
                player.give_card(self.draw_card())

    def draw_card(self):
        return self.deck.get_card() # grab the card and place it for the player.

    def restart_game(self):
        self.deck.build() # rebuild the card
        for player in self.players:
            player.return_cards() # return all the cards