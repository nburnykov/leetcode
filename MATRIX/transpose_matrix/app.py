###########################################################################################
# leetcode problem https://leetcode.com/problems/transpose-matrix/
###########################################################################################

from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    result = [[] for _ in range(len(matrix[0]))]

    for row in matrix:
        for i, el in enumerate(row):
            result[i].append(el)

    return result
