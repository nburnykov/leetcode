from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    if len(grid) == 0:
        return 0

    fresh = set()
    rotten = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
             if grid[x][y] == 2:
                rotten.add((x, y))
             if grid[x][y] == 1:
                fresh.add((x, y))

    time = 0
    rotting = True
    while rotting:
        candidates = set()
        for x, y in rotten:
            for x_cand, y_cand in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                candidates.add((x_cand, y_cand))

        new_rot = candidates & fresh
        rotting = len(new_rot) > 0
        fresh -= new_rot
        rotten |= new_rot
        if rotting:
            time += 1

    return time if not fresh else -1

