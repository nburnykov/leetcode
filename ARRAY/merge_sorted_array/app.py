###########################################################################################
# leetcode problem https://leetcode.com/problems/merge-sorted-array/
###########################################################################################

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # if not nums1 or not nums2:  # edge case
    #     return

    p1 = 0
    for num in nums2:
        while nums1[p1] < num and m > 0:
            p1 += 1
            m -= 1

        if m > 0:
            nums1[p1 + 1: p1 + m + 1] = nums1[p1: p1 + m]

        nums1[p1] = num
        p1 += 1

