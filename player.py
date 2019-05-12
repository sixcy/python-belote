from cards import *

class Player:
  def __init__(self, name: str) -> None:
    self.name = name
    self.hand: Hand = Hand()

  def __str__(self) -> str:
    return "{ name: " + str(self.name) + ", \nhand: " + str(self.hand) + "}"

  def draw(self, deck: Deck) -> None:
    card = deck.draw()
    self.hand.add(card)


class Team:
  def __init__(self, name: str, players: List[Player]) -> None:
    self.name = name

    if len(players) != 2:
      raise Exception("Expected a team of 2 players, got {} instead".format(len(players)))
    self.players = players.copy()
    self.score = 0

  def __str__(self) -> str:
    return ("{ name: " + str(self.name) + ", players: " + list_str(self.players)
              + ", score: " + str(self.score) + "}")
