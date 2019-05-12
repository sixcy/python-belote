from typing import List, Optional
from cards import *
from table import Table
from player import Player
from utils import maybe

class Gamestate:
  def __init__(self, table: Table, first_player: Player) -> None:
    self.table = table
    self.first_player = first_player
    self.atout : Optional[Color] = None
    self.preneur : Optional[Player] = None

  @property
  def iter_players(self) -> List[Player]:
    first_player_index = self.table.players.index(self.first_player)
    return list_rotate(self.table.players, first_player_index)

  def __str__(self) -> str:
    return ("{ table: " + str(self.table)
            + ", \nfirst player: " + str(self.first_player.name)
            + ", \natout: " + str(self.atout)
            + ", \npreneur: " + (str(self.preneur.name) if self.preneur else "None") + "}")


def init_deck() -> Deck:
  L : List[Card] = []
  for color in Color:
    for rank in Rank:
      L.append(Card(color, rank))
  return Deck(L)


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
# --> Situation E: <--
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
  state = Gamestate(table, random.choice(table.players))

  print("Initial state:\n", state)
  print(80*"-")

  # Drawing phase
  for i in range(2): # Two draw turns
    for player in state.iter_players:
      n_card = 3 if i == 0 else 2
      for j in range(n_card):
        player.draw(deck)

  # Revealing top card of the deck
  table.deck.reveal()

  # Loop until someone takes the first card
  assert table.deck.topcard is not None
  while not state.preneur:
    for player in state.iter_players:
      if maybe():
        state.atout = table.deck.topcard.color
        state.preneur = player
        player.draw(deck)
        break
    
  # Final distribution
  for player in state.iter_players:
    n_cards = 2 if player is state.preneur else 3
    for j in range(n_cards):
      player.draw(deck)

  print("Final state: ", state)
  print(80*"-")
