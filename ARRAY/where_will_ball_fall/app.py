###########################################################################################
# leetcode problem  https://leetcode.com/problems/where-will-the-ball-fall/
###########################################################################################
from typing import List


def findBall(grid: List[List[int]]) -> List[int]:
    directions = {1: {'R': "D", "D": "R"}, -1: {"D": "L", "L": "D"}}
    coordinates = {"R": (0, 1), "L": (0, -1), "D": (1, 0)}
    width = len(grid[0])
    result = [-1] * width
    for b in range(width):
        move = "D"
        cell = (0, b)
        while True:
            x, y = cell
            if -1 < y < width:
                if x > len(grid) - 1:
                    result[b] = y
                    break
                cell_val = grid[x][y]
                move = directions[cell_val].get(move)
                if move is None:
                    break
                new_coord = coordinates[move]
                cell = tuple([sum(t) for t in zip(cell, new_coord)])
            else:
                break

    return result