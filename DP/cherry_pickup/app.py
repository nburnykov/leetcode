###########################################################################################
# leetcode problem  https://leetcode.com/problems/cherry-pickup/
###########################################################################################
from functools import lru_cache
from typing import List, Union


def gridpassoneperson(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[n - 1][n - 1] == -1:  # corner case
        return 0

    cherries = [[None] * n for _ in range(n)]
    path_map = dict()

    for x in range(n - 1, -1, -1):
        for y in range(n - 1, -1, -1):
            if x == y == n - 1:
                cherries[x][y] = grid[x][y]
                continue

            if grid[x][y] == -1:
                cherries[x][y] = -1
                continue

            ch1 = cherries[x + 1][y] if (x + 1) < n else -1
            ch2 = cherries[x][y + 1] if (y + 1) < n else -1

            path1 = (ch1, (x + 1, y))
            path2 = (ch2, (x, y + 1))
            path_weight, next_cell = max(path1, path2)

            if path_weight == -1:  # dead end
                cherries[x][y] = -1
                continue

            cherries[x][y] = path_weight + grid[x][y]
            path_map[(x, y)] = next_cell

    if cherries[0][0] == -1:
        return 0

    step = (0, 0)
    while step is not None:  # remove cherries
        grid[step[0]][step[1]] = 0
        step = path_map.get(step)

    return cherries[0][0]


def cherryPickupGreedy(grid: List[List[int]]) -> int:
    """
    incorrect solution
    """
    result = 0
    result += gridpassoneperson(grid)
    if result == 0:  # no cherries found on forward pass
        return result

    n = len(grid)
    for x in range(n):  # grid rotate around secondary diagonal
        for y in range(0, n - x):
            grid[x][y], grid[n - y - 1][n - x - 1] = grid[n - y - 1][n - x - 1], grid[x][y]

    result += gridpassoneperson(grid)

    return result


def cherryPickup(grid: List[List[int]]) -> int:
    @lru_cache(None)
    def cherrypickuptwopersons(x1: int, y1: int, x2: int, y2: int) -> Union[int | float]:
        # to prefer paths that not cross the edges and thorns we need to add a penalty
        n = len(grid)
        if x1 == n or y1 == n or x2 == n or y2 == n or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return float("-inf")  # discard this path

        if x1 == x2 and y1 == y2:  # on the same cell

            if x1 == n - 1 and y1 == n - 1:  # two persons reached the end - stop the process
                return grid[x1][y1]

            result = grid[x1][y1]  # to avoid double count
        else:
            result = grid[x1][y1] + grid[x2][y2]

        result += max([cherrypickuptwopersons(x1 + 1, y1, x2 + 1, y2),  # DOWN DOWN
                       cherrypickuptwopersons(x1, y1 + 1, x2, y2 + 1),  # RIGHT RIGHT
                       cherrypickuptwopersons(x1 + 1, y1, x2, y2 + 1),  # DOWN RIGHT
                       cherrypickuptwopersons(x1, y1 + 1, x2 + 1, y2)])  # RIGHT DOWN

        return result

    result = cherrypickuptwopersons(0, 0, 0, 0)
    return max(0, result)
