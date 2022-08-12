###########################################################################################
# leetcode problem  https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
###########################################################################################
from typing import List


def le(matrix: List[List[int]], i: int) -> int:
    n = len(matrix)
    count = 0

    for row in matrix:
        l, r = 0, n - 1

        if i >= row[r]:
            count += n
            continue

        if row[l] <= i:
            while l < r:  # inner binary search
                mid = (l + r) // 2
                a = row[mid]
                b = row[mid + 1] if (mid + 1) <= (n - 1) else float("inf")
                if a <= i < b:
                    count += mid + 1
                    break
                if i < a:
                    r = mid
                    continue
                if i >= a:
                    l = mid + 1

    return count


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    l, r = matrix[0][0], matrix[n - 1][n - 1]
    result = 0
    while l <= r:  # outer binary search
        mid = (l + r) // 2
        count = le(matrix, mid)
        if count >= k:
            result = mid
            r = mid - 1
        if count < k:
            l = mid + 1

    return result
