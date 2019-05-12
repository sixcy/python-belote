from typing import *

def list_str(L: List) -> str:
  return "[" + ", ".join(str(elt) for elt in L) + "]"
