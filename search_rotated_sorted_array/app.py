###########################################################################################
# leetcode problem https://leetcode.com/problems/search-in-rotated-sorted-array/
###########################################################################################

from typing import List


def search(nums: List[int], target: int) -> int:
    """

    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        pivot, right, left = nums[mid], nums[r], nums[l]
        if pivot == target:
            return mid
        if right == target:
            return r
        if left == target:
            return l

        if (target > left) and (pivot >= left) or \
                (target < right) and (pivot <= right):
            # if target and pivot lie on the same slope (left or right)
            if pivot < target:
                l = mid + 1
            else:
                r = mid - 1
            continue

        if pivot < target:  # target and pivot on different slopes
            r = mid - 1
        else:
            l = mid + 1

    return -1

