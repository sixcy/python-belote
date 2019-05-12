from typing import List, Optional
from cards import *
from table import Table
from player import Player

class Gamestate:
  def __init__(self, table: Table, first_player: Player) -> None:
    self.table = table
    self.first_player = first_player
    self.atout : Optional[Color] = None

  @property
  def iter_players(self) -> List[Player]:
    first_player_index = self.table.players.index(self.first_player)
    return list_rotate(self.table.players, first_player_index)

  def __str__(self) -> str:
    return ("{ table: " + str(self.table)
            + ", \nfirst player: " + str(self.first_player.name)
            + ", \natout: " + str(self.atout) + "}")


def init_deck() -> Deck:
  L : List[Card] = []
  for color in Color:
    for rank in Rank:
      L.append(Card(color, rank))
  return Deck(L)

## PLAN
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

  # First player takes it
  assert table.deck.topcard is not None
  state.atout = table.deck.topcard.color
  for player in state.iter_players:
    for j in range(3):
      player.draw(deck)

  print("Final state: ", state)
  print(80*"-")
