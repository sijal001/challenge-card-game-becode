import random
from collections import deque
from card import Card

class Player:
    """
    In this class we set user to get the required card.
    """
    def __init__(self, name,turn_count=0):
        self.name = name # name od the player
        self.cards = [] # lis of the cards of the player
        self.history = [] # history of th ecard played by the player
        self.turn_count = turn_count # record what it is playing
        self.number_of_cards = len(self.cards) # length of the card that player holds

    def give_card(self, card): # dristibute the card to the player
        self.cards.append(card)

    def return_cards(self):
        self.cards = []
    
    def play(self): # set a gaming style and play the game 
        pickcard = random.choice(self.cards)
        
        self.history.append(pickcard)
        self.card.remove(pickcard)
        print("{} {} played: {} {}".format(self.name,self.turn_count,
                                           pickcard[0],pickcard[1]))
        return pickcard
        
    def __repr__(self): # print the player with its card.
        return 'Player: {} - [{}]'.format(self.name, ','.join([str(x) for x in self.cards]))

class Deck:
    def __init__(self):
        self.cards = deque() # it's more efficient to pop from left than from a list
        self.build() # call the method that creates deck

    def build(self): # method to build the cards for the deck
        self.cards.clear()
        for i in ['♥', '♦', '♣', '♠']:
            for j in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(i, j))
                
        # need to shuffle in order to have random order of cards
        random.shuffle(self.cards)

    def length(self):
        return len(self.cards)

    def get_card(self): # take the card from deck 
        return self.cards.popleft()

    def __repr__(self): # print the numbers of the cards present in the deck
        return 'Deck: [{} Cards]'.format(self.length())
