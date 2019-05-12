from player import *

class Table:
  def __init__(self, players: List[Player], deck: Deck) -> None:
    self.players = players
    self.deck = deck
    self.trick = Trick()

  def __str__(self) -> str:
    return ("{ players: " + list_str(self.players) + ", \ntrick: " + str(self.trick) +
              ", \ndeck: " + str(self.deck) + "}")
