###########################################################################################
# leetcode problem  https://leetcode.com/problems/search-a-2d-matrix-ii/
###########################################################################################

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    def binary_search(line: List[int], target: int) -> bool:
        l, r = 0, len(line) - 1
        while l <= r:
            mid = (l + r) // 2
            if line[mid] == target:
                return True
            if target < line[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False

    for line in matrix:
        if binary_search(line, target):
            return True

    return False