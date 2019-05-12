from typing import *
import random

def list_str(L: List) -> str:
  return "[" + ", ".join(str(elt) for elt in L) + "]"

def list_rotate(L: List, n: int) -> List:
  assert n in range(len(L))
  return L[n:] + L[:n]

def maybe() -> bool:
  return random.choice([True, False])
