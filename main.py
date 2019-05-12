#!/usr/bin/python3.6

from game import *
from table import Table
from player import Player

## PLAN
#
# Common ground: the deck is initialized and randomized
# 
# Situation A:
#   1) Each player draws 5 cards from the deck.
#
# Situation B:
#   1) A player is designed as "first player", and players draw 3+2 cards from the deck
#       in that order
#
# Situation C:
#   1) Situation B
#   2) The top card of the deck is revealed and put faceup
#
# Situation D:
#   1) Situation C
#   2) The first player accepts the card, and gets 2 cards - then the others get 3 cards
#
# Situation E:
#   1) Situation C
#   2) The first player may accept the card, same for the rest.
#       It goes clockwise until someone accepts
#
# Situation F:
#   1) Situation C
#   2) The first player may accept for the card, same for the rest. If the end is reached,
#       the deck is cut and we start over.
##

deck = init_deck()
table = Table([Player("South"), Player("West"), Player("North"), Player("East")], deck)

print("Initial state:\n", table)
print(80*"-")

for player in table.players:
  for i in range(5):
    player.draw(deck)

print("Final state: ", table)
print(80*"-")
