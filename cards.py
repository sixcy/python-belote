from enum import Enum, unique
from typing import List, Optional
from utils import *
from collections import namedtuple
import random

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


class ListCards:
  def __init__(self, cards: List[Card] = []) -> None:
    self.cards = cards.copy()

  def __str__(self) -> str:
    return list_str(self.cards)


class Deck(ListCards):
  def __init__(self, cards: List[Card] = []) -> None:
    ListCards.__init__(self, cards)
    self.topcard : Optional[Card] = None

  def draw(self) -> Card:
    return self.cards.pop()

  def shuffle(self) -> None:
    random.shuffle(self.cards)

  def reveal(self) -> None:
    self.topcard = self.cards[-1]

  def __str__(self) -> str:
    return "{ \ncards: " + ListCards.__str__(self) + ", \ntopcard: " + str(self.topcard) + "}"


class Hand(ListCards):
  def __init__(self, cards: List[Card] = []) -> None:
    ListCards.__init__(self, cards)

  def add(self, card: Card) -> None:
    self.cards.append(card)


class Trick(ListCards):
  pass


if __name__ == "__main__":
  card = Card(Color.CLUBS, Rank.FIVE)
  print(card)

  card2 = Card(Color.HEARTS, Rank.TEN)
  card3 = Card(Color.DIAMONDS, Rank.TEN)

  deck = Deck([card, card2, card3])
  print(deck)
