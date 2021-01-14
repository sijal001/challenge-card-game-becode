# Importing important python files

from player import Player
from player import Deck
from card import Card
from game import Board

deck_of_cards = Deck()
player_list = []

while True:
    player = int(input("Number of players between 2-5: "))

    if 2 > player > 5:
        "Please Enter between 2 - 5 players"
        continue
    else:
        for i in range(player):
            player_name = input("Enter name of player {}: ".format(i+1))
            player_list.append(Player("{}".format(player_name)))
        break
    
new_game = Board(player_list, deck_of_cards)  
cardPerPerson = int(52/player)
new_game.deal(cardPerPerson)

for player in player_list:
    print(player)
    
print(new_game.deck)

new_game.restart_game()
for player in player_list:
    print(player)
print(new_game.deck)