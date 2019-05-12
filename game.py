from cards import *

def init_deck() -> Deck:
  L : List[Card] = []
  for color in Color:
    for rank in Rank:
      L.append(Card(color, rank))
  return Deck(L)
