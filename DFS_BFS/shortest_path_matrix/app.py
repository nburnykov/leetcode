###########################################################################################
# leetcode problem https://leetcode.com/problems/shortest-path-in-binary-matrix
###########################################################################################

from collections import deque
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if len(grid) == 0:  # corner cases
        return -1

    if grid[0][0] == 1: # corner cases
        return -1

    if grid == [[0]]: # corner cases
        return 1

    q = deque([(0, 0, 1)])
    grid[0][0] = 1
    while len(q) > 0:
        x, y, d = q.popleft()
        candidates = [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y), (x - 1, y - 1), (x, y - 1),
                      (x + 1, y - 1)]
        for cx, cy in candidates:
            if 0 <= cx < len(grid) and 0 <= cy < len(grid) and not grid[cx][cy]:
                if cx == cy == len(grid) -1:
                    return d + 1
                q.append((cx, cy, d+1))
                grid[cx][cy] = 1

    return -1