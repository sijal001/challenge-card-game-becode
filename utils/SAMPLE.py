from collections import deque
import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # good practice is to include repr and str magic methods - that way you can print meaningful info
    def __repr__(self):
        return '<{} {}>'.format(self.value, self.suit)


class Deck:
    def __init__(self):
        # use deque - it's more efficient to pop from left than from a list -> good advice -> learn build in types :)
        self.cards = deque()
        self.build()

    def build(self):
        self.cards.clear()
        for i in ['♥', '♦', '♣', '♠']:
            for j in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(i, j))
        # need to shuffle in order to have random order of cards
        random.shuffle(self.cards)

    def length(self):
        return len(self.cards)

    def get_card(self):
        return self.cards.popleft()

    def __repr__(self):
        return 'Deck: [{} Cards]'.format(self.length())


class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck

    def deal(self):
        for player in self.players:
            for i in range(1):
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


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def give_card(self, card):
        self.cards.append(card)

    def return_cards(self):
        self.cards = []

    def __repr__(self):
        return 'Player: {} - [{}]'.format(self.name, ','.join([str(x) for x in self.cards]))


deck_of_cards = Deck()
player_one = Player("sijal")
player_two = Player("joshi")

for i in range(int(52/2)):
    new_game = Game([player_one, player_two], deck_of_cards)
    new_game.deal()
    print(player_one, player_two)
    print(new_game.deck)

new_game.restart_game()
print(player_one, player_two)
print(new_game.deck)