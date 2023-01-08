from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    An O(1) space complexity solution
    """
    first_row_zero, first_col_zero = False, False

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 0:
                if x == 0:
                    first_col_zero = True
                if y == 0:
                    first_row_zero = True
                matrix[x][0] = 0
                matrix[0][y] = 0

    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[0])):
            if matrix[x][0] == 0 or matrix[0][y] == 0:
                matrix[x][y] = 0

    if first_row_zero:
        for x in range(len(matrix)):
            matrix[x][0] = 0

    if first_col_zero:
        for y in range(len(matrix[0])):
            matrix[0][y] = 0