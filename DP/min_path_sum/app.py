###########################################################################################
# leetcode problem  https://leetcode.com/problems/minimum-path-sum/
###########################################################################################

from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    sums = [[None] * n for _ in range(m)]
    for x in range(m - 1, -1, -1):
        for y in range(n - 1, -1, -1):
            sum1 = sums[x + 1][y] if (x + 1) < m else None
            sum2 = sums[x][y + 1] if (y + 1) < n else None
            if sum1 is not None and sum2 is not None:  # both are not None
                sum = min(sum1, sum2)
            elif (sum1 or sum2) is None:  # both are None
                sum = 0
            else:  # one of the sums is None
                sum = sum1 or sum2

            sums[x][y] = grid[x][y] + sum

    return sums[0][0]
