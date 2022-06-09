###########################################################################################
# leetcode problem https://leetcode.com/problems/range-sum-query-2d-immutable/
###########################################################################################

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sum_matrix = [[None] * len(self.matrix[0]) for _ in matrix]
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                a = self.sum_matrix[x - 1][y] if x - 1 >= 0 else 0
                b = self.sum_matrix[x][y - 1] if y - 1 >= 0 else 0
                c = self.sum_matrix[x - 1][y - 1] if (x - 1 >= 0) and (y - 1 >= 0) else 0
                self.sum_matrix[x][y] = a + b - c + self.matrix[x][y]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.sum_matrix[row2][col2]
        b = self.sum_matrix[row1 - 1][col2] if row1 - 1 >= 0 else 0
        c = self.sum_matrix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        d = self.sum_matrix[row1 - 1][col1 - 1] if (col1 - 1 >= 0) and (row1 - 1 >= 0) else 0
        return a - b - c + d
