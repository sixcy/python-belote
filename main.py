#!/usr/bin/python3.6

from enum import Enum, unique
from typing import List

@unique
class Color(Enum):
  CLUBS, DIAMONDS, HEARTS, SPADES = range(4)


@unique
class Rank(Enum):
  ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING = range(13)


class Card:
  def __init__(self, color: Color, rank: Rank) -> None:
    self.color = color
    self.rank = rank

  def __str__(self) -> str:
    return "(" + str(self.color) + ", " + str(self.rank) + ")"


class Deck:
  def __init__(self, cards: List[Card]) -> None:
    self.cards = cards.copy()

  def __str__(self) -> str:
    return "[" + ", ".join([str(card) for card in self.cards]) + "]"

card = Card(Color.CLUBS, Rank.FIVE)
print(card)

card2 = Card(Color.HEARTS, Rank.TEN)
card3 = Card(Color.DIAMONDS, Rank.TEN)

deck = Deck([card, card2, card3])
print(deck)
