###########################################################################################
# leetcode problem https://leetcode.com/problems/rotate-image/
###########################################################################################

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    lvl = 0
    while lvl < n // 2:
        x1, y1 = lvl, lvl
        x2, y2 = lvl, n - 1 - lvl
        x3, y3 = n - 1 - lvl, n - 1 - lvl
        x4, y4 = n - 1 - lvl, lvl

        for i in range(n - 2 * lvl - 1):

            x1_m, y1_m = x1, y1 + i
            x2_m, y2_m = x2 + i, y2
            x3_m, y3_m = x3, y3 - i
            x4_m, y4_m = x4 - i, y4

            matrix[x1_m][y1_m], matrix[x2_m][y2_m], matrix[x3_m][y3_m], matrix[x4_m][y4_m] = \
                matrix[x4_m][y4_m], matrix[x1_m][y1_m], matrix[x2_m][y2_m], matrix[x3_m][y3_m]

        lvl += 1
