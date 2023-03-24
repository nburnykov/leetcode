from collections import deque
from typing import List


def removeStones(stones: List[List[int]]) -> int:
    stone_map = dict()
    stones_left = 0
    for row, column in stones:
        stone_map.setdefault(f"r{row}", list()).append(f"c{column}")
        stone_map.setdefault(f"c{column}", list()).append(f"r{row}")

    while len(stone_map) > 0:  # find stone clusters with BFS
        q = deque(stone_map.popitem()[1])
        while len(q) > 0:
            coord = q.popleft()
            line = stone_map.pop(coord, [])
            q.extend(line)
        stones_left += 1

    return len(stones) - stones_left


