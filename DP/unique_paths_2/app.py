###########################################################################################
# leetcode problem
###########################################################################################
from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    paths = [[None] * n for _ in range(m)]
    paths[m - 1][n - 1] = 1

    for x in range(m - 1, -1, -1):
        for y in range(n - 1, -1, -1):
            if obstacleGrid[x][y] == 1:
                paths[x][y] = 0
                continue

            path1 = paths[x + 1][y] if x + 1 < m else 0
            path2 = paths[x][y + 1] if y + 1 < n else 0
            if paths[x][y] is None:
                paths[x][y] = path1 + path2

    return paths[0][0]

