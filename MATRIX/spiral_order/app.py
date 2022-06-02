###########################################################################################
# leetcode problem https://leetcode.com/problems/spiral-matrix/
###########################################################################################
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    x, y = 0, 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    result = []
    while True:
        result.append(matrix[x][y])
        matrix[x][y] = None

        # determine next valid candidate
        fail_count = 0
        while fail_count < 4:
            x_inc, y_inc = direction[direction_index]
            xc, yc = x + x_inc, y + y_inc
            if 0 <= xc < len(matrix) and 0 <= yc < len(matrix[0]) and matrix[xc][yc] is not None:
                x = xc  # candidate is found
                y = yc
                break
            else:
                direction_index = (direction_index + 1) % 4
                fail_count += 1

        if fail_count == 4:
            return result






