###########################################################################################
# leetcode problem  https://leetcode.com/problems/pascals-triangle-ii/
###########################################################################################

from typing import List


def getRow(rowIndex: int) -> List[int]:
    result = [0, 1, 0]
    for i in range(rowIndex):
        candidate = []
        for j in range(len(result) - 1):
            candidate.append(result[j] + result[j + 1])
        result = [0] + candidate + [0]
    return result[1: -1]
