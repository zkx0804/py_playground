from typing import List
import numpy as np
from collections import defaultdict, deque
from heapq import heappop, heappush


# problem set 1
# Sudoku
class Problem:

  def canFinish(self, n, flights, src, dst, k):
    dp_map = defaultdict(dict)
    for d, a, p in flights:
      dp_map[d][a] = p
    q = deque([(0, src, k + 1)])
    while q:
      s, d, k = heappop(q)
      if d == dst:
        return s
      if k > 0:
        for j in dp_map[d]:
          heappush(q, (p + dp_map[d][j], j, k - 1))

    return -1

    pass

  def longgest_string(self, s: str):
    if not s:
      return '';


if __name__ == "__main__":
  start = 'hit'
  end = 'cog'

  lib = ["hot", "dot", "dog", "lot", "log", "cog"]
  pass
