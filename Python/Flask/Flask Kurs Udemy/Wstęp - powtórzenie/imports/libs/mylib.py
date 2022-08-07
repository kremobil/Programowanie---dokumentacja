from typing import List

print(__name__)

def add(*args: List[int]) -> int:
  return sum(args)