from cards import *
from table import Table
from player import Player

def init_deck() -> Deck:
  L : List[Card] = []
  for color in Color:
    for rank in Rank:
      L.append(Card(color, rank))
  return Deck(L)

## PLAN
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

def game_loop() -> None:
  deck = init_deck()
  deck.shuffle()
  table = Table([Player("South"), Player("West"), Player("North"), Player("East")], deck)

  first_player_i = random.randint(0, len(table.players))

  print("Initial state:\n", table)
  print(80*"-")
  print("First player:", table.players[first_player_i], "\n")
  print(80*"-")

  # Drawing phase
  iter_players = list_rotate(table.players, first_player_i)
  for i in range(2): # Two draw turns
    for player in iter_players:
      n_card = 3 if i == 0 else 2
      for j in range(n_card):
        player.draw(deck)

  # Revealing top card of the deck
  table.deck.reveal()

  print("Final state: ", table)
  print(80*"-")
