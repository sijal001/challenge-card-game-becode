import random
from collections import deque
from card import Card

class Player:
    def __init__(self, name,turn_count=0):
        self.name = name
        self.cards = []
        self.history = []
        self.turn_count = turn_count
        self.number_of_cards = len(self.cards)

    def give_card(self, card):
        self.cards.append(card)

    def return_cards(self):
        self.cards = []
    
    def play(self):
        pickcard = random.choice(self.cards)
        
        self.history.append(pickcard)
        self.card.remove(pickcard)
        print("{} {} played: {} {}".format(self.name,self.turn_count,
                                           pickcard[0],pickcard[1]))
        return pickcard
        
    def __repr__(self):
        return 'Player: {} - [{}]'.format(self.name, ','.join([str(x) for x in self.cards]))

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
