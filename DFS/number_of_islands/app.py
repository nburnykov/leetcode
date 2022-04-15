###########################################################################################
# leetcode problem https://leetcode.com/problems/number-of-islands/
###########################################################################################

from typing import List


def numIslands(grid: List[List[str]]) -> int:
    def dfs(grid, x, y):
        q = [(x, y)]
        while len(q) > 0:
            x, y = q.pop(-1)
            candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for xc, yc in candidates:
                if 0 <= xc < len(grid) and 0 <= yc < len(grid[0]) and grid[xc][yc] == "1":
                    q.append((xc, yc))
                    grid[xc][yc] = "0"

    if len(grid) == 0:  # corner cases
        return 0

    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                result += 1
                dfs(grid, i, j)

    return result
