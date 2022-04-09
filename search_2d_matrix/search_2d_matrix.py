###########################################################################################
# leetcode problem https://leetcode.com/problems/search-a-2d-matrix/
###########################################################################################
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    def binary_search(m: List[int], t: int) -> bool:
        if len(m) == 0:
            return False
        l, r = 0, len(m) - 1
        while l <= r:
            mid = (l + r) // 2
            if m[mid] == t:
                return True
            if m[mid] < t:
                l = mid + 1
            else:
                r = mid - 1
        return False

    # corner cases
    if len(matrix) == 0:
        return False

    if len(matrix) == 1:
        return binary_search(matrix[0], target)

    if len(matrix[0]) == 0:
        return False

    block_mins = [m[0] for m in matrix]
    block_maxx = [m[-1] for m in matrix]
    if not (min(block_mins) <= target <= max(block_maxx)):
        return False

    # block binary search
    block_mins.append(float('inf'))
    l, r = 0, len(block_mins) - 2
    while l <= r:
        mid = (l + r) // 2
        if block_mins[mid] <= target < block_mins[mid + 1]:
            return binary_search(matrix[mid], target)
        if target < block_mins[mid]:
            r = mid - 1
        if target >= block_mins[mid + 1]:
            l = mid + 1

    return False
