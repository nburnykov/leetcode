###########################################################################################
# leetcode problem  https://leetcode.com/problems/dungeon-game/
###########################################################################################
from typing import List


def calculateMinimumHP(dungeon: List[List[int]]) -> int:
    h = len(dungeon)
    w = len(dungeon[0])

    health = [[None] * w for _ in range(h)]
    for x in range(h - 1, -1, -1):
        for y in range(w - 1, -1, -1):
            path1 = health[x + 1][y] if (x + 1) < h else float("-inf")  # infinite damage on edges
            path2 = health[x][y + 1] if (y + 1) < w else float("-inf")
            path = max(path1, path2)
            path = path if path != float("-inf") else 0  # right bottom corner case, stop cell, no infinite damage
            path = path + dungeon[x][y]

            # in order to enter cell with positive path balance you need 0 (+1) health
            health[x][y] = path if path < 0 else 0

    return -health[0][0] + 1
