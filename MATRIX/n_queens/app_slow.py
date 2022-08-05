###########################################################################################
# leetcode problem  https://leetcode.com/problems/n-queens/
###########################################################################################
import random
from functools import lru_cache
from typing import List, Tuple, Optional


def place_queen(x, y, n) -> set:
    result = {(x, i) for i in range(0, n)}
    result |= {(i, y) for i in range(0, n)}

    qx, qy = x, y
    while qx >= 0 or qy < n:
        result.add((qx, qy))
        qx -= 1
        qy += 1

    qx, qy = x, y
    while qx < n or qy < n:
        result.add((qx, qy))
        qx += 1
        qy += 1

    qx, qy = x, y
    while qx >= 0 or qy >= 0:
        result.add((qx, qy))
        qx -= 1
        qy -= 1

    qx, qy = x, y
    while qx < n or qy >= 0:
        result.add((qx, qy))
        qx += 1
        qy -= 1

    return result


def recursion(board: set, queens: set, n: int) -> list:
    solutions = []
    if len(queens) == n:
        solutions.append(list(queens))
        return solutions
    if len(board) == 0:
        return []

    while len(board) > 0:
        x, y = board.pop()
        queen_range = place_queen(x, y, n)
        r = recursion(board - queen_range, queens | {(x, y)}, n)
        if r:
            solutions.extend(r)

    return solutions


def solveNQueens(n: int) -> List[List[str]]:
    board = {(x, y) for x in range(n) for y in range(n)}

    queen_coord =  recursion(board, set(), n)

    result = []

    for line in queen_coord:
        b = [['.'] * n for _ in range(n)]
        for x, y in line:
            b[x][y] = 'Q'

        result.append(["".join(l) for l in b])

    return result
